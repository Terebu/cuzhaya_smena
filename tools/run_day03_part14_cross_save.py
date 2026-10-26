"""Load two genuine part13 saves in their original QA context, then continue part14."""
from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);suffix=Path('validation/steamapps/common/Everlasting Summer');engine=stage/suffix
old=Path('D:/stean/release_chuzaya_smena/day03_part13_20261026')/suffix
for p in (old/'game/cs_release_checks').glob('*.rpy'):
 shutil.copy2(p,engine/'game/cs_release_checks'/p.name)
s='''# -*- coding: utf-8 -*-
label cs_qa_p14_load_previous:
    $ renpy.load("p13_"+str(renpy.cs_p14_load_case)+"_end")
    return
'''
for case,friend,confess in ((0,2,True),(1,3,False)):
 s+='''testcase cs_p14_cross_'''+str(case)+''':
    pause 0.5
    $ _test.force=True
    $ _test.timeout=100.0
    $ _preferences.text_cps=0
    $ _preferences.transitions=2
    $ renpy.set_physical_size((1280,720))
    $ renpy.cs_p14_fast=False
    $ renpy.cs_p14_auto=True
    $ renpy.cs_p14_request=True
    $ renpy.cs_p14_confess='''+repr(confess)+'''
    $ renpy.cs_p14_cast=()
    $ renpy.cs_p14_pending=None
    $ renpy.cs_p14_count=0
    $ renpy.cs_p14_visited=[]
    $ renpy.cs_p6_case="p14_cross_'''+str(case)+'''"
    $ renpy.cs_p14_load_case='''+str(case)+'''
    run Start("cs_qa_p14_load_previous")
    pause 1.5
    $ cs_p6_capture("loaded_initial")
    $ renpy.cs_p14_fast=True
    click
    pause 55.0
    assert renpy.get_screen("cs_day04_wait_screen") is not None
    assert renpy.get_screen("main_menu") is None
    assert cs_day03_part13_done and cs_day03_part14_done and cs_day03_completed
    assert cs_da_friend_before_night=='''+str(friend)+'''
    assert cs_friend_da=='''+str(friend+1)+'''
    assert cs_da_shared_bed_day3 and cs_da_shared_sleep_cg_seen_day3
    assert cs_da_love_confession_day3=='''+repr(confess)+'''
    assert cs_da_unspoken_feelings_day3=='''+repr(not confess)+'''
    assert cs_mz_book_finished_day3 and not cs_mz_book_borrowed_day3
    assert cs_day03_reading_book_location=="library"
    assert cs_lena_elbow_injury_day2==2 and cs_lena_elbow_bandaged
    assert cs_day03_sketchbook_location==cs_day03_poster_location=="house_table"
    assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3
    assert "cs_day03_171" not in renpy.cs_p14_visited
    $ cs_p6_capture("complete")
    $ open(config.basedir+"/p14_cross_'''+str(case)+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

'''
(R/'tools/day03_part14_cross_save.rpy.txt').write_text(s,encoding='utf8')
shutil.copy2(R/'tools/day03_part14_cross_save.rpy.txt',engine/'game/cs_release_checks/day03_part14_cross_save.rpy')
results=[]
for case in (0,1):
 print('Native actual part13 save:',case,flush=True)
 saves=list((old/'isolated_saves').glob('p13_'+str(case)+'_end*'));assert saves
 for p in saves:shutil.copy2(p,engine/'isolated_saves'/p.name)
 marker=engine/('p14_cross_'+str(case)+'_PASS.txt')
 if marker.exists():marker.unlink()
 engine_run(engine,['test','cs_p14_cross_'+str(case)],stage/('p14_cross_'+str(case)+'.log'),timeout=220)
 assert marker.exists(),case
 results.append(dict(case=case,status='PASS',previous='day03_part13_20261026',save=saves[0].name))
 (stage/'part14_cross_save_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART14_CROSS_SAVE_PASS')
