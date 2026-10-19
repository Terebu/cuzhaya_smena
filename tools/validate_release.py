"""Validate compiled release provenance, loader names and AST identities.

Python 3 data-only inspection; never imports or executes RPYC Python code.
"""
from pathlib import Path
import argparse, hashlib, json, re
from rpyc_audit import inspect, identifiers

NAMESPACE = 'cs_scripts_5ea2d086'
MARKER = 'cs_assets_5ea2d086_9903_4ff8_a659.identity'
METADATA = ['sp/dasha_metadata.json','sp/semen_metadata.json','sp/zhenya/metadata.json','sp/viola/metadata.json']
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def base_index(game):
    ids={}; names=set(); hashes={}; errors=[]
    for p in Path(game).rglob('*.rpyc'):
        rel=p.relative_to(game)
        if 'mods' in rel.parts: continue
        names.add(rel.as_posix()); hashes[sha(p)]=rel.as_posix()
        try:
            for slot in (1,2):
                try: info=inspect(p,slot)
                except ValueError:
                    if slot==2: continue
                    raise
                for i in identifiers(info):ids.setdefault(i,rel.as_posix())
        except Exception as e:errors.append(str(p)+': '+str(e))
    return dict(ids=ids,names=names,hashes=hashes,errors=errors)

def validate(root, manifest, game, output=None, index=None):
    root=Path(root); manifest=json.loads(Path(manifest).read_text(encoding='utf8'))
    errors=[]; warnings=[]; found={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file()}
    expected=manifest['files']; base=index or base_index(Path(game))
    errors.extend(base['errors'])
    if set(found)!=set(expected):
        errors += ['Unexpected file: '+x for x in sorted(set(found)-set(expected))]
        errors += ['Missing file: '+x for x in sorted(set(expected)-set(found))]
    for rel,p in found.items():
        if rel in expected and sha(p)!=expected[rel]['sha256']: errors.append('Changed/unverified file: '+rel)
        if any(x in rel.split('/') for x in ('qa','tools','source','saves','__pycache__')):errors.append('Development/save file in release: '+rel)
    ids={}; definitions={}; script_count=0; node_count=0
    for rel,p in found.items():
        if p.suffix not in ('.rpy','.rpyc'):continue
        if p.suffix=='.rpy':errors.append('Unexpected source in compiled release: '+rel);continue
        script_count+=1
        if not rel.startswith(NAMESPACE+'/'):errors.append('Script outside private loader namespace: '+rel)
        if rel in base['names']:errors.append('Loader virtual-name collision with original: '+rel)
        if sha(p) in base['hashes']:errors.append('Byte-identical original game script: '+rel+' = '+base['hashes'][sha(p)])
        provenance=expected.get(rel,{})
        if not provenance.get('source_sha256') or not provenance.get('source'):errors.append('RPYC without declared source provenance: '+rel)
        try:
            own_ids=set(); own_defs=set()
            for slot in (1,2):
                try: info=inspect(p,slot)
                except ValueError:
                    if slot==2:continue
                    raise
                slot_ids=set();slot_defs={}
                for node in info['nodes']:
                    node_id=repr(node['id'])
                    if node_id in slot_ids:errors.append('Internal ID repeated inside script: '+rel+' -> '+node_id)
                    slot_ids.add(node_id)
                    definition=node['image'] if node['kind']=='Image' else node['screen'] if node['kind']=='Screen' else None
                    if definition:
                        key=(node['kind'],repr(definition))
                        if key in slot_defs:errors.append('Image/screen repeated inside script: '+rel+' -> '+repr(key))
                        slot_defs[key]=node_id
                own_ids.update(slot_ids)
                for node in info['nodes']:
                    filename=str(node['filename']).replace('\\','/')
                    if '/'+NAMESPACE+'/' not in '/'+filename:
                        errors.append('Foreign AST origin: '+rel+' -> '+filename);break
                    if node['kind'] in ('Image','Screen'):
                        value=node['image'] if node['kind']=='Image' else node['screen']
                        if value:own_defs.add((node['kind'],repr(value)))
            node_count+=len(own_ids)
            for key in own_ids:
                if key in base['ids']:errors.append('Internal ID collides with original: '+rel+' -> '+key)
                if key in ids:errors.append('Internal ID defined twice: '+rel+' and '+ids[key]+' -> '+key)
                ids[key]=rel
            for key in own_defs:
                if key in definitions: errors.append('Image/screen defined twice: '+repr(key)+' in '+rel+' and '+definitions[key])
                definitions[key]=rel
        except Exception as e:errors.append('Cannot decode RPYC '+rel+': '+str(e))
    for rel in METADATA+[MARKER]:
        if rel not in found:errors.append('Missing mandatory runtime resource: '+rel)
    for rel in METADATA:
        if rel not in found:continue
        try:
            data=json.loads(found[rel].read_text(encoding='utf8'))
            groups=data.values() if isinstance(data,dict) else [data]
            for group in groups:
                for entry in group:
                    path=entry['path'].replace('mods/chuzaya_smena/','')
                    if path.startswith('/') or ':' in path or '..' in path.split('/') or path not in found:
                        errors.append('Invalid/missing metadata asset: '+path)
        except Exception as e:errors.append('Invalid runtime JSON '+rel+': '+str(e))
    game=Path(game).resolve()
    locations=[game/'mods',game.parents[2]/'workshop/content/331470']
    copies=set()
    for active in locations:
        if not active.exists():continue
        copies.update(str(p.parent) for p in active.rglob(MARKER))
        # Older installed releases do not have the new marker.
        for p in active.rglob('scriot.rpyc'):
            try:
                if repr('chuzhaya_smena_start') in identifiers(inspect(p)):
                    ancestor=next((a for a in p.parents if (a/MARKER).exists()),p.parent)
                    copies.add(str(ancestor))
            except Exception as e:warnings.append('Cannot inspect installed mod '+str(p)+': '+str(e))
    if copies:warnings.append('Installed mod copy/copies detected. Keep only one active for Workshop: '+', '.join(sorted(copies)))
    warnings.append('Static validation does not prove runtime behavior; run the isolated local and Workshop engine tests.')
    report=dict(status='FAIL' if errors else 'PASS',scripts=script_count,internal_ids=node_count,files=len(found),errors=errors,warnings=warnings)
    if output:Path(output).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('content');p.add_argument('manifest');p.add_argument('--game',required=True);p.add_argument('--report')
    a=p.parse_args();result=validate(a.content,a.manifest,a.game,a.report)
    print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(result['errors']))
