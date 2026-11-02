"""Incremental, seeded editorial compilation; assets remain unchanged.

Called inside readability_qa's temporary Q: mapping. Each phase overlays one
completed editorial day on the preceding frozen source snapshot, compiles with
adjacent preceding RPYC files, then materializes a validated compiled package.
"""
from pathlib import Path
import hashlib, json, os, shutil
from build_release import engine_run
from validate_release import validate, base_index, NAMESPACE

ROOT=Path(__file__).resolve().parent.parent
GROUPS=('day04','prologue','day01','day02','day03')

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def run_stage(work, group):
    work=Path(work)
    assert group in GROUPS,group
    previous=work/'native_current_phase.json'
    state=json.loads(previous.read_text()) if previous.is_file() else {'completed':[],'phase':'b0'}
    if group in state['completed']:
        report=work/'stages'/group/'stage_pass.json'
        assert report.is_file(),group
        return json.loads(report.read_text())
    assert group==GROUPS[len(state['completed'])],('Unexpected editorial phase',group,state)
    phase=work/'stages'/group
    phase.mkdir(parents=True,exist_ok=True)
    prior=work/'b0' if not state['completed'] else work/'stages'/state['completed'][-1]
    source=phase/'source_snapshot'
    if not source.exists():shutil.copytree(prior/'source_snapshot',source)
    for p in (ROOT/'days'/group).rglob('*.rpy'):
        q=source/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    engine=work/'b0/validation/steamapps/common/Everlasting Summer'
    runtime=work/'b0/validation/steamapps/workshop/content/331470/3822308228'
    for p in source.rglob('*.rpy'):
        q=runtime/NAMESPACE/p.relative_to(source)
        assert q.with_suffix('.rpyc').is_file(),q
        q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    engine_run(engine,['compile','--keep-orphan-rpyc'],phase/'compile.log')
    # Test the compiled package, as it will be distributed.
    for p in list((runtime/NAMESPACE).rglob('*.rpy')):
        assert p.with_suffix('.rpyc').is_file();p.unlink()
    base=json.loads((work/'b0/release_manifest.json').read_text(encoding='utf8'))
    content=phase/'content';content.mkdir(exist_ok=True)
    files={}
    for rel,original in base['files'].items():
        p=runtime/rel;q=content/rel;q.parent.mkdir(parents=True,exist_ok=True)
        assert p.is_file(),p
        if q.exists():
            assert q.resolve().is_relative_to(content.resolve());q.unlink()
        if p.suffix.lower() in ('.png','.jpg','.jpeg','.ogg','.mp3','.ttf','.otf'):
            try:os.link(p,q)
            except OSError:shutil.copy2(p,q)
        else:shutil.copy2(p,q)
        entry={'sha256':digest(q)}
        if 'source' in original:
            entry.update(source=original['source'],source_sha256=digest(source/original['source']))
        files[rel]=entry
    manifest=phase/'release_manifest.json'
    manifest.write_text(json.dumps({'format':1,'namespace':NAMESPACE,'files':files},ensure_ascii=False,indent=2),encoding='utf8')
    result=validate(content,manifest,ROOT.parents[2]/'game',phase/'validation_static.json',base_index(ROOT.parents[2]/'game'))
    assert not result['errors'],result['errors']
    from readability_ast_audit import audit
    ast=audit(work/'b0',phase,groups=state['completed']+[group])
    (phase/'editorial_ast.json').write_text(json.dumps(ast,ensure_ascii=False,indent=2),encoding='utf8')
    assert not ast['errors'],ast['errors']
    engine_run(engine,['test','cs_release_smoke'],phase/'native_smoke.log')
    report={'group':group,'status':'PASS','scripts':result['scripts'],
            'compiled_seed':str(prior/'content'/NAMESPACE),
            'source_sha256':{p.relative_to(source).as_posix():digest(p) for p in source.rglob('*.rpy')}}
    (phase/'stage_pass.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    state['completed'].append(group);state['phase']=group
    previous.write_text(json.dumps(state,indent=2),encoding='utf8')
    print('EDITORIAL_STAGE_PASS',group,flush=True)
    return report
