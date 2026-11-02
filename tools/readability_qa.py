"""Isolated editorial builds with published RPYC seeds and a short Windows path.

The temporary Q: mapping points only at the recorded, writable QA directory.
It is removed in finally, and a pre-existing Q: drive is never replaced.
"""
from pathlib import Path
import argparse, json, os, subprocess, sys

ROOT=Path(__file__).resolve().parent.parent

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('phase')
    parser.add_argument('--operation',choices=('build','stage','create-saves','load-saves'),default='build')
    parser.add_argument('--source',choices=('before','live'),default='live')
    parser.add_argument('--seed',default='before')
    parser.add_argument('--cases',nargs='+')
    parser.add_argument('--timeout',type=int,default=240)
    args=parser.parse_args()
    state=json.loads((ROOT/'source/readability_session.json').read_text(encoding='utf8'))
    target=Path(state['work']).resolve()
    assert target.is_dir() and (target/'before_manifest.json').is_file()
    if Path('Q:/').exists():raise RuntimeError('Q: is already in use; preserving it')
    subprocess.run(['subst','Q:',str(target)],check=True)
    try:
        from build_release import build
        work=Path('Q:/')
        seed=work/'before' if args.seed=='before' else work/args.seed/'content/cs_scripts_5ea2d086'
        source=work/'before' if args.source=='before' else ROOT
        if args.operation=='stage':
            from readability_stages import run_stage
            run_stage(work,args.phase)
        elif args.operation in ('create-saves','load-saves'):
            from readability_cross_save import run, fixture_static_check
            fixture_static_check()
            data=json.loads((ROOT/'source/readability_save_cases.json').read_text(encoding='utf8'))
            if args.operation=='create-saves':
                stage=work/'b0';mode='create';cases=data['cases']
            else:
                stage=work/'stages'/args.phase;mode='load'
                cases=[c for c in data['cases'] if c['group']==args.phase]
            if args.cases:cases=[c for c in cases if c['id'] in args.cases]
            assert cases,'No matching save cases'
            engine=work/'b0/validation/steamapps/common/Everlasting Summer'
            run(stage,engine,mode,cases,work/'readability_save_evidence',args.timeout)
        else:
            build(work/args.phase,compiled_seed=seed,source_root=source,
                  engine_root=ROOT.parents[2],asset_root=ROOT,stabilize=False)
    finally:
        subprocess.run(['subst','Q:','/d'],check=True)

if __name__=='__main__':main()
