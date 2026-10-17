from pathlib import Path
R=Path(__file__).resolve().parent.parent
out=['# -*- coding: utf-8 -*-']
for trust in (0,1):
 name='cs_part06_'+('trust' if trust else 'plan')
 out+=['testcase '+name+':','    pause 1.0','    $ renpy.set_physical_size((1280,720))','    $ _preferences.text_cps = 0','    $ _test.timeout = 50.0','    assert renpy.has_image("bg ext_no_bus") and renpy.loadable("images/bg/ext_no_bus.jpg")','    run Start("cs_qa_part06_load")','    pause 1.0','    $ cs_qa_global_audit = True','    $ cs_qa_part06_audit = True','    $ cs_qa_part06_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)','    assert cs_friend_se == 1',
 '    click until label cs_check_part06_s40','    pause 1.0','    assert not renpy.showing("cs_cg_lena_darya_hand_in_hand_day")','    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_lunch_approach")',
 '    click until label cs_check_part06_semen_arrived','    pause 0.5','    assert renpy.showing("bg int_dining_hall_people_day")','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_lunch")',
 '    click until run CSQAwaitMenu()','    pause 0.5','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_menu")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-menu")','    $ cs_friend_se = 99','    $ renpy.load("'+name+'-menu")','    pause 0.5','    assert cs_friend_se == 1',
 '    "'+('Сказать Семёну, что меня действительно тревожит' if trust else 'Ограничиться планом проверки дороги')+'"',
 '    click until label cs_check_part06_empty_bus_stop','    pause 1.0','    assert cs_friend_se == '+str(1+trust),'    assert renpy.showing("bg ext_no_bus")','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    assert renpy.music.get_playing() is None','    $ cs_qa_capture("'+name+'_empty_bus_stop")',
 '    click until label cs_check_part06_control_created','    pause 0.5','    assert renpy.showing("cs_road_marked_verge_day")','    $ cs_qa_capture("'+name+'_control")']
 for lap in (1,2):
  for key,bg in (('a','powerlines'),('b','left_bend'),('c','right_bend'),('return','marked_verge')):
   out+=['    click until label cs_check_part06_lap'+str(lap)+'_'+key,'    pause 0.5','    assert renpy.showing("cs_road_'+bg+'_day")','    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_lap'+str(lap)+'_'+key+'")']
  if lap==1:
   out+=['    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-loop")','    $ cs_friend_se = 99','    $ renpy.load("'+name+'-loop")','    pause 0.5','    assert cs_friend_se == '+str(1+trust)]
  else:
   out+=['    assert renpy.music.get_playing() == "sound/music/waltz_of_doubts.ogg"']
 out+=['    click until label cs_check_part06_gate_return','    pause 0.5','    assert cs_road_loop_observations == 2','    assert renpy.showing("bg ext_no_bus")','    assert cs_road_visual_trace == ["approach", "control_created", "lap1_a", "lap1_b", "lap1_c", "lap1_return", "lap2_a", "lap2_b", "lap2_c", "lap2_return", "back_c", "back_b", "back_a"]','    $ cs_qa_capture("'+name+'_gate_return")',
 '    click until label cs_check_part06_olga_arrived','    pause 0.5','    assert renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_olga")','    click until label cs_check_part06_olga_left','    pause 0.5','    assert not renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_olga_left")',
 '    click until label cs_check_part06_semen_left','    pause 0.5','    assert cs_road_notes_written','    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_semen_left")',
 '    click until label cs_check_part06_pending','    pause 3.0','    assert cs_day02_part06_complete and not cs_day02_done','    assert cs_friend_se == '+str(1+trust),'    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part06_prior_friends','    assert renpy.showing("cs_darya") and not renpy.showing("mt") and not renpy.showing("cs_semen")','    assert renpy.music.get_playing() is None','    assert renpy.get_screen("cs_day02_road_continue_screen") is not None','    $ cs_qa_capture("'+name+'_end")']
 if trust:
  out+=['    run Jump("cs_qa_road_replay")','    click until run CSQAwaitMenu()','    "Сказать Семёну, что меня действительно тревожит"','    click until label cs_check_part06_pending','    assert cs_friend_se == 2 and cs_se_road_day2_awarded']
 out+=['    $ open(config.gamedir + "/mods/chuzaya_smena/qa/'+name+'_pass.txt", "w").write("PASS")','    run Quit(confirm=False)','']
(R/'qa/part06_routes_test.rpy').write_text('\n'.join(out),encoding='utf8')
print('Two road/trust/save-load routes generated')
