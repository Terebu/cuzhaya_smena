"""Two real end-of-day3 saves, with their serialized QA callbacks available."""
from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);suffix=Path('validation/steamapps/common/Everlasting Summer');engine=stage/suffix
old=Path('D:/stean/release_chuzaya_smena/day03_part14_20261026')/suffix
for p in (old/'game/cs_release_checks').glob('*.rpy'):
 shutil.copy2(p,engine/'game/cs_release_checks'/p.name)
# The current full walker is disabled during this load-only check.
for name in ('day03_part06_test','full_render_walkthrough_test','day04_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
s='''# -*- coding: utf-8 -*-
label cs_qa_day04_load_previous:
    $ renpy.load("p14_"+str(renpy.cs_d4_cross_case)+"_end")
    return
'''
for case,shared,confess,friend in ((2,True,True,3),(6,False,False,0)):
 s+='''testcase cs_day04_cross_'''+str(case)+''':
    pause 0.5
    $ _test.force=True
    $ _test.timeout=80.0
    $ _preferences.text_cps=0
    $ renpy.set_physical_size((1280,720))
    $ renpy.cs_d4_cross_case='''+str(case)+'''
    $ renpy.cs_d4_qa=False
    $ renpy.cs_rw_enabled=False
    $ renpy.cs_p14_fast=False
    $ renpy.cs_p6_case="day04_cross_'''+str(case)+'''"
    run Start("cs_qa_day04_load_previous")
    pause 9.0
    assert cs_day04_started and not cs_day04_done
    assert cs_day03_completed and cs_day03_part14_done
    assert cs_da_shared_bed_day3=='''+repr(shared)+'''
    assert cs_da_love_confession_day3=='''+repr(confess)+'''
    assert cs_friend_da=='''+str(friend)+'''
    assert cs_lena_elbow_bandaged
    assert renpy.get_screen("main_menu") is None
    $ cs_p6_capture("loaded_day4")
    $ renpy.take_screenshot()
    $ renpy.save("day04_cross_'''+str(case)+'''")
    $ renpy.load("day04_cross_'''+str(case)+'''")
    pause 0.8
    assert cs_day04_started and cs_friend_da=='''+str(friend)+'''
    $ open(config.basedir+"/day04_cross_'''+str(case)+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(engine/'game/cs_release_checks/day04_cross_save.rpy').write_text(s,encoding='utf8')
results=[]
for case in (2,6):
 saves=list((old/'isolated_saves').glob('p14_'+str(case)+'_end*'));assert saves
 for p in saves:shutil.copy2(p,engine/'isolated_saves'/p.name)
 engine_run(engine,['test','cs_day04_cross_'+str(case)],stage/('day04_cross_'+str(case)+'.log'),timeout=130)
 assert (engine/('day04_cross_'+str(case)+'_PASS.txt')).exists()
 results.append(dict(case=case,status='PASS',save=saves[0].name))
 (stage/'day04_cross_save_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('DAY04_CROSS_SAVE_PASS',flush=True)
