from pathlib import Path
R=Path(__file__).resolve().parent.parent
out=['# -*- coding: utf-8 -*-']
for help in (False,True):
 name='cs_part04_'+('help' if help else 'leave')
 out+=['testcase '+name+':','    pause 1.0','    $ renpy.set_physical_size((1280,720))','    $ _preferences.text_cps = 0','    $ _test.timeout = 50.0',
 '    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg int_aidpost_day", "bg ext_aidpost_day", "cs normal stethoscope", "cs smile stethoscope", "sh serious pioneer", "el grin pioneer", "cs_cg_poster_planning_day"))',
 '    assert __import__("__builtin__").all(renpy.loadable("sound/" + x + ".ogg") for x in ("music/smooth_machine", "music/my_daily_life", "music/just_think", "music/get_to_know_me_better", "ambiences/medstation_inside_day", "sfx/knock_door7_polite"))',
 '    run Start("cs_qa_part04_load")','    pause 1.0','    $ cs_qa_global_audit = True','    $ cs_qa_part04_audit = True','    assert cs_friend_viola == 0 and not cs_met_viola','    click until run CSQAwaitMenu()','    "Предложить Славе помощь с материалами"',
 '    click until label cs_check_part03_clubs','    pause 0.05','    assert renpy.showing("bg int_clubs_male_day")','    $ cs_qa_capture("'+name+'_boundary")',
 '    click until label cs_check_part04_s26','    pause 3.0','    assert renpy.showing("sh") and renpy.showing("el")','    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")','    assert renpy.music.get_playing() == "sound/music/smooth_machine.ogg"','    $ cs_qa_capture("'+name+'_engineers")',
 '    click until label cs_check_part04_s27','    pause 0.5','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    assert not renpy.showing("sh") and not renpy.showing("el")','    $ cs_qa_capture("'+name+'_outside")',
 '    click until label cs_check_part04_semen_left','    pause 0.5','    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_semen_left")',
 '    click until label cs_check_part04_s29','    pause 0.5','    assert renpy.showing("cs") and renpy.showing("cs_darya")','    assert not renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_viola")',
 '    click until label cs_check_part04_poster_observation','    pause 0.5','    assert cs_met_viola','    assert not renpy.showing("cs") and not renpy.showing("cs_darya")','    assert renpy.showing("bg int_aidpost_day")','    $ cs_qa_capture("'+name+'_anatomy")',
 '    click until label cs_check_part04_viola_restored','    pause 0.5','    assert renpy.showing("cs") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_restored")',
 '    click until run CSQAwaitMenu()','    pause 0.5','    assert cs_friend_viola == 0 and cs_met_viola','    $ cs_qa_capture("'+name+'_menu")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-choice")','    $ cs_friend_viola = 99','    $ renpy.load("'+name+'-choice")','    pause 0.5','    assert cs_friend_viola == 0',
 '    "'+('Предложить Виоле помощь с материалами' if help else 'Поблагодарить Виолу и не задерживаться')+'"',
 '    click until label cs_check_part04_s32','    pause 0.5','    assert cs_friend_viola == '+str(int(help))+' and cs_helped_viola_day2 == '+str(help),'    assert not renpy.showing("cs") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_merged")',
 '    click until label cs_check_part04_s33','    pause 0.5','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    assert not renpy.showing("cs")','    $ cs_qa_capture("'+name+'_returned")',
 '    click until label cs_check_part04_poster_work','    pause 0.5','    assert renpy.showing("cs_cg_poster_planning_day")','    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_poster_work")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-poster")','    $ cs_friend_viola = 99','    $ renpy.load("'+name+'-poster")','    pause 0.5','    assert cs_friend_viola == '+str(int(help))+' and renpy.showing("cs_cg_poster_planning_day")',
 '    click until label cs_check_part05_s34','    pause 0.5','    assert not cs_day02_done and cs_day02_part04_complete','    assert cs_friend_mi == 1 and cs_friend_sl == 1','    assert cs_friend_viola == '+str(int(help)),'    assert renpy.showing("cs_cg_poster_planning_day")','    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"','    assert renpy.showing("cs_cg_poster_planning_day")','    $ cs_qa_capture("'+name+'_end")']
 if help:
  out+=['    run Jump("cs_qa_viola_replay")','    click until run CSQAwaitMenu()','    "Предложить Виоле помощь с материалами"','    click until label cs_check_part05_s34','    assert cs_friend_viola == 1 and cs_viola_day2_awarded']
 out+=['    $ open(config.gamedir + "/mods/chuzaya_smena/qa/'+name+'_pass.txt", "w").write("PASS")','    run Quit(confirm=False)','']
(R/'qa/part04_routes_test.rpy').write_text('\n'.join(out),encoding='utf8')
print('Two Viola routes generated')
