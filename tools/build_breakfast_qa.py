from pathlib import Path
R=Path(__file__).resolve().parent.parent
out=['# -*- coding: utf-8 -*-']
for score,met in [(0,True),(1,True),(1,False)]:
 name='cs_breakfast_u%d_m%d'%(score,met);friendly=score>=1 and met
 out+=['testcase '+name+':','    pause 1.0','    $ renpy.set_physical_size((1280,720))','    $ _preferences.text_cps = 0','    $ _test.timeout = 40.0','    run Start("cs_qa_breakfast_load")','    pause 1.5','    $ cs_friend_un = '+str(score),'    $ cs_met_un = '+str(met),'    $ cs_darya_known = True','    $ cs_qa_breakfast_audit = True','    run Jump("cs_qa_breakfast_path")','    click until label cs_check_breakfast_table','    pause 1.0','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    assert cs_breakfast_un_here == '+str(friendly),'    $ cs_qa_capture("'+name+'_table")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-table")','    $ cs_friend_un = 99','    $ renpy.load("'+name+'-table")','    pause 1.0','    assert cs_friend_un == '+str(score)]
 if friendly:
  out+=['    click until label cs_check_breakfast_un','    pause 1.0','    assert renpy.showing("un") and not renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_two_lenas")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-un")','    $ cs_friend_un = 99','    $ renpy.load("'+name+'-un")','    pause 1.0','    assert cs_friend_un == '+str(score)]
 out+=['    click until label cs_check_breakfast_private','    pause 1.0','    assert not renpy.showing("un") and not cs_breakfast_un_here','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_private")','    click until label cs_check_breakfast_square','    pause 1.0','    assert renpy.showing("bg ext_square_day")','    $ cs_qa_capture("'+name+'_square")','    click until label cs_check_new_day02_pending','    pause 1.0','    assert cs_friend_un == '+str(score)+' and not cs_day02_done','    assert cs_friend_mz == 1','    $ open(config.gamedir + "/mods/chuzaya_smena/qa/'+name+'_pass.txt", "w").write("PASS")','    run Quit(confirm=False)','']
if (R/'source/day02_part02.md').exists():
 out=[line.replace('cs_check_new_day02_pending','cs_check_part02_s15').replace('renpy.showing("bg ext_square_day")','renpy.showing("bg ext_dining_hall_near_day")') for line in out]
(R/'qa/breakfast_routes_test.rpy').write_text('\n'.join(out),encoding='utf8')
print('Three friendship/knowledge cases generated')
