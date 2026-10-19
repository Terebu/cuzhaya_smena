"""Regression cases: validators must reject bad packages, not just accept one."""
from pathlib import Path
import argparse, json, os, shutil
from validate_release import validate, base_index, sha, NAMESPACE

def run(release, game, output):
    release=Path(release);output=Path(output);output.mkdir(parents=True,exist_ok=False)
    index=base_index(Path(game)); results=[]
    for case in ('renamed_original','duplicate_nodes','missing_json','no_provenance','stale_qa'):
        directory=output/case;directory.mkdir();content=directory/'content'
        shutil.copytree(release/'content',content,copy_function=os.link)
        manifest=json.loads((release/'release_manifest.json').read_text(encoding='utf8'))
        files=manifest['files']; source=next(content.rglob('*.rpyc'))
        if case in ('renamed_original','duplicate_nodes'):
            rel=NAMESPACE+'/innocent_name.rpyc';target=content/rel
            shutil.copy2(Path(game)/'resources.rpyc' if case=='renamed_original' else source,target)
            files[rel]=dict(sha256=sha(target),source='innocent_name.rpy',source_sha256='test_provenance')
            expected='original' if case=='renamed_original' else 'defined twice'
        elif case=='missing_json':
            (content/'sp/dasha_metadata.json').unlink();expected='Missing mandatory'
        elif case=='no_provenance':
            files[source.relative_to(content).as_posix()].pop('source_sha256');expected='source provenance'
        else:
            target=content/'qa/old_test.rpyc';target.parent.mkdir();shutil.copy2(source,target);expected='Unexpected file'
        m=directory/'manifest.json';m.write_text(json.dumps(manifest),encoding='utf8')
        result=validate(content,m,Path(game),directory/'result.json',index)
        assert result['errors'] and any(expected in e for e in result['errors']), (case,result)
        results.append(dict(case=case,rejected=True,errors=len(result['errors'])))
    (output/'test_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
    print(json.dumps(results,indent=2))

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('release');a.add_argument('game');a.add_argument('output');v=a.parse_args();run(v.release,v.game,v.output)
