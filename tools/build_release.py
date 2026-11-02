"""Clean-source compiler, AST validator and isolated native release tests.

Usage: python tools/build_release.py D:/stean/release_chuzaya_smena/release_NEW
Never uses working RPYC caches. Never uploads or alters installed Workshop files.
"""
from pathlib import Path
import argparse, hashlib, json, os, shutil, subprocess, tempfile, zipfile
from validate_release import validate, base_index, NAMESPACE, MARKER, METADATA

ROOT=Path(__file__).resolve().parent.parent
ENGINE=ROOT.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy_asset(src,dst):
    # Only immutable large assets are linked. Engine scripts/caches are copied.
    if Path(src).suffix.lower() in ('.rpa','.png','.jpg','.ogg','.mp3','.otf','.ttf','.dll','.pyd'):
        try:os.link(src,dst);return dst
        except OSError:pass
    return shutil.copy2(src,dst)

def engine_run(engine, args, log, timeout=240):
    env=os.environ.copy();env.update(SDL_VIDEODRIVER='windows',SDL_AUDIODRIVER='directsound',RENPY_RENDERER='gl2',RENPY_SKIP_SPLASHSCREEN='1')
    cmd=[str(engine/'lib/windows-x86_64/python.exe'),str(engine/'Everlasting Summer.py'),str(engine)]+args+['--savedir',str(engine/'isolated_saves')]
    with Path(log).open('wb') as stream:
        result=subprocess.run(cmd,cwd=engine,env=env,stdout=stream,stderr=subprocess.STDOUT,timeout=timeout)
    if result.returncode:raise RuntimeError('Engine failed (%s), see %s'%(result.returncode,log))

def build(output, *, compiled_seed=None, source_root=None, engine_root=None, asset_root=None, stabilize=True):
    global ROOT, ENGINE
    if source_root: ROOT=Path(source_root).resolve()
    if engine_root: ENGINE=Path(engine_root).resolve()
    asset_root=Path(asset_root).resolve() if asset_root else ROOT
    compiled_seed=Path(compiled_seed).resolve() if compiled_seed else None
    if stabilize:
        subprocess.run([__import__('sys').executable,str(ROOT/'tools/stabilize_mod_calls.py')],check=True,cwd=ROOT)
    output=Path(output).absolute()
    if output.exists():raise ValueError('Existing release is preserved. Choose a new directory: '+str(output))
    if not output.parent.is_dir():raise ValueError('Release parent directory must already exist.')
    temp=Path(tempfile.mkdtemp(prefix='.chuzhaya_build_',dir=output.parent))
    print('Clean build workspace:',temp,flush=True)
    native=temp/'validation/steamapps/common/Everlasting Summer';native.mkdir(parents=True)
    for name in ('lib','renpy'):
        shutil.copytree(ENGINE/name,native/name,copy_function=copy_asset,ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copy2(ENGINE/'Everlasting Summer.py',native/'Everlasting Summer.py')
    shutil.copytree(ENGINE/'game',native/'game',copy_function=copy_asset,ignore=shutil.ignore_patterns('mods','saves','cache'))
    work=native/'game/mods/chuzaya_smena';work.mkdir(parents=True)
    scripts=sorted(ROOT.glob('*.rpy'))+sorted((ROOT/'days').rglob('*.rpy'))
    source_provenance={}
    snapshot=temp/'source_snapshot'
    for p in scripts:
        rel=p.relative_to(ROOT);dest=work/NAMESPACE/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
        snap=snapshot/rel;snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
        # Editorial releases retain names from the preceding compiled AST.
        # Ren'Py merges unchanged statement names while compiling new source.
        if compiled_seed:
            seed=compiled_seed/rel.with_suffix('.rpyc')
            if not seed.is_file():raise RuntimeError('Missing published RPYC seed: '+str(seed))
            shutil.copy2(seed,dest.with_suffix('.rpyc'))
        source_provenance[(Path(NAMESPACE)/rel.with_suffix('.rpyc')).as_posix()]=dict(source=rel.as_posix(),source_sha256=sha(p))
    for name in ('audio','bg','cg','fonts','sp','ui'):
        for p in (asset_root/name).rglob('*'):
            if p.is_file() and p.suffix.lower() in ('.png','.jpg','.jpeg','.webp','.ogg','.mp3','.wav','.ttf','.otf','.txt'):
                dest=work/p.relative_to(asset_root);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
    for rel in METADATA+[MARKER]:
        dest=work/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(asset_root/rel,dest)
    print('Compiling',len(scripts),'source files; RPYC seed: '+str(compiled_seed) if compiled_seed else 'current source files, no mod RPYC copied.',flush=True)
    # ES ships original scripts without sources; Ren'Py compile otherwise
    # deletes them as orphans. Only the freshly staged mod is cache-free.
    engine_run(native,['compile','--keep-orphan-rpyc'],temp/'compile.log')
    content=temp/'content';content.mkdir()
    for p in work.rglob('*'):
        if not p.is_file() or p.suffix=='.rpy':continue
        dest=content/p.relative_to(work);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
    files={}
    for p in content.rglob('*'):
        if p.is_file():
            rel=p.relative_to(content).as_posix();files[rel]=dict(sha256=sha(p),**source_provenance.get(rel,{}))
    manifest=temp/'release_manifest.json'
    manifest.write_text(json.dumps(dict(format=1,namespace=NAMESPACE,files=files),ensure_ascii=False,indent=2),encoding='utf8')
    print('Checking loader names, source provenance and internal AST IDs.',flush=True)
    index=base_index(ENGINE/'game')
    result=validate(content,manifest,ENGINE/'game',temp/'validation_static.json',index)
    if result['errors']:raise RuntimeError('Static validation failed: '+repr(result['errors'][:5]))
    # Remove only the sources we just staged, not arbitrary installed files.
    for p in list(work.rglob('*.rpy')):
        assert p.is_relative_to(work) and p.with_suffix('.rpyc').is_file()
        p.unlink()
    checks=native/'game/cs_release_checks';checks.mkdir()
    shutil.copy2(ROOT/'tools/release_smoke.rpy.txt',checks/'release_smoke.rpy')
    assets=[p.relative_to(work).as_posix() for p in work.rglob('*') if p.is_file() and not p.suffix=='.rpyc']
    (work/'qa_asset_manifest.json').write_text(json.dumps(assets,ensure_ascii=False),encoding='utf8')
    print('Native local test: menu, two scenes, all resources.',flush=True)
    engine_run(native,['test','cs_release_smoke'],temp/'local_smoke.log')
    for name in ('release_menu.png','release_second_scene.png','release_sprite.png','release_cg.png','asset_validation.json'):
        shutil.copy2(native/name,temp/('local_'+name))
    workshop=temp/'validation/steamapps/workshop/content/331470/3822308228';workshop.parent.mkdir(parents=True)
    shutil.move(str(work),str(workshop))
    if list((native/'game/mods').iterdir()):raise RuntimeError('Local mod must be absent for Workshop test')
    print('Native compiled-only Workshop test, two successive launches.',flush=True)
    for number in (1,2):engine_run(native,['test','cs_release_smoke'],temp/('workshop_smoke_%d.log'%number))
    for name in ('release_menu.png','release_second_scene.png','release_sprite.png','release_cg.png','asset_validation.json'):
        shutil.copy2(native/name,temp/('workshop_'+name))
    runtime=json.loads((native/'asset_validation.json').read_text())
    if '/3822308228/' not in runtime['root']:raise RuntimeError('Workshop root not used: '+runtime['root'])
    if not any('workshop/content/331470/3822308228' in p.replace('\\','/') for p in runtime['searchpath']):raise RuntimeError('Native Workshop discovery not active')
    # The package, not the QA fixture, is immutable; revalidate before archiving.
    result=validate(content,manifest,ENGINE/'game',temp/'validation_static.json',index)
    if result['errors']:raise RuntimeError('Final validation failed')
    with zipfile.ZipFile(temp/'Chuzhaya_Smena_Vertical_Slice.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(content.rglob('*')):
            if p.is_file():z.write(p,'chuzaya_smena/'+p.relative_to(content).as_posix())
    with zipfile.ZipFile(temp/'Chuzhaya_Smena_Vertical_Slice.zip') as z:
        if z.testzip():raise RuntimeError('ZIP CRC failure')
    (temp/'BUILD_PASS.json').write_text(json.dumps(dict(scripts=len(scripts),static=result,local_exit=0,workshop_exit=[0,0],assets=runtime['count'],compiled_seed=str(compiled_seed) if compiled_seed else None),ensure_ascii=False,indent=2),encoding='utf8')
    temp.rename(output)
    print('VERIFIED RELEASE:',output,flush=True)
    return output

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('output')
    a.add_argument('--seed-rpyc');a.add_argument('--source-root');a.add_argument('--engine-root');a.add_argument('--asset-root');a.add_argument('--skip-stabilize',action='store_true')
    args=a.parse_args();build(args.output,compiled_seed=args.seed_rpyc,source_root=args.source_root,engine_root=args.engine_root,asset_root=args.asset_root,stabilize=not args.skip_stabilize)
