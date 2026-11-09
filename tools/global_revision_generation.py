"""Prove the later narrative layer after replaying the frozen editorial base."""
from pathlib import Path
import json, shutil, subprocess, sys, tempfile


def regenerate_global_layer(root, *, check, rounds, scratch, entry):
    from regenerate_readability import materialize, regenerate_day05_layer, runtime_paths, sha, check_exact
    parent = Path(scratch) if scratch else Path(tempfile.gettempdir())/'chuzhaya_global_generation'
    parent.mkdir(parents=True, exist_ok=True)
    probe = Path(tempfile.mkdtemp(prefix='global-', dir=parent))
    original = {rel:sha(p.read_bytes()) for rel,p in runtime_paths(root).items()}
    materialize(root, probe)
    new_files = ['revision_staging.rpy','new_day05_assets.rpy','bus_scene_audio.rpy']
    new_files += [p.relative_to(root).as_posix() for p in (root/'days/revision20261106').glob('*.rpy')]
    for rel in new_files:
        target=probe/rel
        assert target.resolve().is_relative_to(probe.resolve())
        target.unlink()
    folder=probe/'days/revision20261106'
    folder.rmdir()
    base=root/'source/global_revision_20261106'
    for rel in ('save_return_compat.rpy','day03_location_audio.rpy','opening_credits.rpy','phone.rpy'):
        shutil.copy2(base/('baseline_'+rel+'.txt'),probe/rel)
    # The older wrapper owns exactly the original ledgers and Day 5 layer.
    # It never sees the new documents and cannot apply them a second time.
    shutil.copytree(root/'source/day05',probe/'source/day05')
    for p in (root/'tools').glob('day05*'):
        if p.is_file():shutil.copy2(p,probe/'tools'/p.name)
    for name in ('build_day05.py','global_revision_sfx.py','global_text_paging.py'):
        shutil.copy2(root/'tools'/name,probe/'tools'/name)
    report=regenerate_day05_layer(probe,check=False,rounds=rounds,scratch=parent,entry=entry)
    # The phone UI was revised after the frozen November 1 base.
    shutil.copy2(root/'phone.rpy',probe/'phone.rpy')
    shutil.copytree(base,probe/'source/global_revision_20261106')
    if (root/'source/text_paging_20261108').is_dir():
        shutil.copytree(root/'source/text_paging_20261108',probe/'source/text_paging_20261108',dirs_exist_ok=True)
    for p in (root/'tools').glob('global_*'):
        if p.is_file():shutil.copy2(p,probe/'tools'/p.name)
    shutil.copy2(root/'tools/build_global_revision.py',probe/'tools/build_global_revision.py')
    for n in range(2):
        subprocess.run([sys.executable,'-X','utf8',str(probe/'tools/build_global_revision.py')],cwd=probe,check=True)
        check_exact(probe,original)
    if {rel:sha(p.read_bytes()) for rel,p in runtime_paths(root).items()}!=original:
        raise ValueError('Runtime changed during the isolated global proof')
    report.update(root=str(root),probe=str(probe),runtime_files=len(original),published_files=[],global_layer='PASS',global_replays=2)
    (base/'generation_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report
