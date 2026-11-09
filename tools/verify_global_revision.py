"""Check immutable manuscripts, published bodies, assets and sound provenance."""
from pathlib import Path
import hashlib,json,re
from global_revision_tree import tree
from global_revision_sfx import SOUNDS,resource
R=Path(__file__).resolve().parent.parent
S=R/'source/global_revision_20261106'
B=Path('D:/stean/steamapps/common/mod_backups/global_revision_20261106')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
intake=json.loads((S/'intake.json').read_text(encoding='utf-8'))
for name,record in intake.items():
    assert sha(S/(name+'.txt'))==record['sha256']
    assert sha(Path(record['source']))==record['sha256']
coverage=json.loads((S/'integration.json').read_text(encoding='utf-8'))
for name,record in coverage.items():
    P,branches,menus,art,end=tree(R,name)
    assert sorted(art)==record['source_ids']
    assert len(art)==record['paragraphs'] and len(menus)==record['menus']
protected=[]
for p in (B/'days').rglob('*.rpy'):
    rel=p.relative_to(B)
    if 'day05' in rel.parts:continue
    assert sha(p)==sha(R/rel),str(rel)
    protected.append(rel.as_posix())
for rel in ('days/day03/part03/95_scene.rpy','days/day02/part10/74a_scene.rpy'):
    assert sha(R/rel)==sha(B/rel)
renames=json.loads((S/'asset_renames.json').read_text(encoding='utf-8'))
for old,new in renames.items():
    assert (R/new).is_file() and not (R/old).is_file()
    assert sha(R/new)==sha(B/'assets_added'/old)
inventory=set(json.loads((S/'native_sfx_inventory.json').read_text(encoding='utf-8')))
sounds=[]
for day,cues in SOUNDS.items():
    for index,(cue,volume) in cues.items():
        path='sound/sfx/knocking_door_outside.ogg' if cue.startswith('knocks:') else resource(cue).split('>',1)[-1]
        assert path in inventory,path
        sounds.append(dict(document=day,paragraph=index,cue=cue,path=path,volume=volume,origin='Everlasting Summer native archive; referenced, not redistributed'))
stock_path=R/'source/audio_revision_20261107/sources.json'
stock_sources=[x for x in json.loads(stock_path.read_text(encoding='utf-8')) if x.get('used')] if stock_path.is_file() else []
soundproof=dict(status='PASS',cues=sounds,unique_resources=sorted({x['path'] for x in sounds}),external_downloads=stock_sources,credits=('SFX: Everlasting Summer; stock: '+', '.join(sorted({x['author'] for x in stock_sources}))+' (CC0)') if stock_sources else 'SFX: Everlasting Summer original assets')
(S/'sound_usage.json').write_text(json.dumps(soundproof,ensure_ascii=False,indent=2),encoding='utf-8')
runtime=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))
labels={}
for p in runtime:
    for label in re.findall(r'^\s*label (\w+)(?:\([^\n]*\))?\s*:',p.read_text(encoding='utf-8-sig'),re.M):
        assert label not in labels,('Duplicate label',label,p,labels.get(label))
        labels[label]=p.relative_to(R).as_posix()
result=dict(status='PASS',runtime_files=len(runtime),source_coverage={k:v['paragraphs'] for k,v in coverage.items()},
            unchanged_published_day01_to_04_files=protected,protected_95_sha256=sha(R/'days/day03/part03/95_scene.rpy'),
            native_sound_events=len(sounds),native_sound_files=len(soundproof['unique_resources']),new_assets=len(renames),duplicate_labels=0)
(S/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('GLOBAL_STATIC_PASS',len(runtime),'scripts;',len(protected),'published bodies unchanged;',len(sounds),'sound events')
