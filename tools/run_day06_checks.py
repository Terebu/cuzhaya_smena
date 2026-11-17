"""Prepare an isolated native Ren'Py game; never uses player saves or Workshop installs."""
from pathlib import Path
import argparse,shutil,os,sys,json
from build_release import engine_run,copy_asset
ROOT=Path(__file__).resolve().parent.parent
ENGINE=ROOT.parents[2]

def sync(stage):
    native=stage/'validation/steamapps/common/Everlasting Summer'
    if not native.exists():
        native.mkdir(parents=True)
        for folder in ('lib','renpy'):
            shutil.copytree(ENGINE/folder,native/folder,copy_function=copy_asset,ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(ENGINE/'Everlasting Summer.py',native/'Everlasting Summer.py')
        shutil.copytree(ENGINE/'game',native/'game',copy_function=copy_asset,ignore=shutil.ignore_patterns('mods','saves','cache'))
    work=native/'game/mods/chuzaya_smena';work.mkdir(parents=True,exist_ok=True)
    scripts=work/'cs_scripts_5ea2d086'
    for p in list(ROOT.glob('*.rpy'))+list((ROOT/'days').rglob('*.rpy')):
        rel=p.relative_to(ROOT);dst=scripts/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.with_suffix('.rpyc').exists() and p.with_suffix('.rpyc').exists():shutil.copy2(p.with_suffix('.rpyc'),dst.with_suffix('.rpyc'))
        shutil.copy2(p,dst)
        if rel.as_posix()=="audio_menu_guard.rpy":os.utime(dst,None)
    for folder in ('audio','bg','cg','fonts','sp','ui'):
        for p in (ROOT/folder).rglob('*'):
            if not p.is_file() or p.suffix.lower() not in ('.png','.jpg','.jpeg','.ogg','.mp3','.wav','.ttf','.otf','.json'):continue
            dest=work/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists():copy_asset(p,dest)
    shutil.copy2(ROOT/'cs_assets_5ea2d086_9903_4ff8_a659.identity',work/'cs_assets_5ea2d086_9903_4ff8_a659.identity')
    checks=native/'game/cs_release_checks';checks.mkdir(exist_ok=True)
    shutil.copy2(ROOT/'tools/day06_test.rpy.txt',checks/'day06_test.rpy')
    return native

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('stage');ap.add_argument('actions',nargs='*',default=['compile']);args=ap.parse_args()
    stage=Path(args.stage);stage.mkdir(parents=True,exist_ok=True);native=sync(stage)
    for action in args.actions:
        print('RUN',action,flush=True)
        engine_run(native,['compile','--keep-orphan-rpyc'] if action=='compile' else ['lint'] if action=='lint' else ['test',action],stage/(action+'.log'),timeout=1800)
        print('PASS',action,flush=True)
