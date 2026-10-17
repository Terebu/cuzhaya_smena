from pathlib import Path
R=Path(__file__).resolve().parent.parent
out=['# -*- coding: utf-8 -*-']
for mi,sl,se,vi in ((1,1,1,1),(0,1,0,0),(1,0,0,1),(0,0,1,0)):
 name='cs_part05_m%d_s%d_e%d'%(mi,sl,se)
 out+=['testcase '+name+':','    pause 1.0','    $ renpy.set_physical_size((1280,720))','    $ _preferences.text_cps = 0','    $ _test.timeout = 50.0',
 '    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg ext_clubs_day", "bg ext_square_day", "sl normal pioneer far", "cs normal", "cs_cg_lena_darya_hand_in_hand_day"))',
 '    assert __import__("__builtin__").all(renpy.loadable("sound/music/" + x + ".ogg") for x in ("my_daily_life", "lets_be_friends", "get_to_know_me_better", "a_promise_from_distant_days"))',
 '    run Start("cs_qa_part05_load_'+('help' if vi else 'leave')+'")','    pause 1.0','    $ cs_qa_global_audit = True','    $ cs_qa_part05_audit = True',
 '    $ cs_day02_miku_listened = '+str(bool(mi)),'    $ cs_friend_mi = '+str(mi),'    $ cs_helped_sl_day2 = '+str(bool(sl)),'    $ cs_friend_sl = '+str(sl),
 '    $ cs_qa_part05_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)','    $ _history_list = []',
 '    click until label cs_check_part05_s34','    pause 0.5','    assert renpy.showing("cs_cg_poster_planning_day")','    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")','    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"','    $ cs_qa_capture("'+name+'_continuity")',
 '    click until run CSQAwaitMenu()','    pause 0.5','    assert cs_friend_se == 0','    $ cs_qa_capture("'+name+'_menu")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-menu")','    $ cs_friend_se = 99','    $ renpy.load("'+name+'-menu")','    pause 0.5','    assert cs_friend_se == 0',
 '    "'+('Давай сделаем надпись вместе' if se else 'Я закончу рисунок, а ты займись буквами')+'"',
 '    click until label cs_check_part05_poster_finished','    pause 0.5','    assert cs_day02_poster_finished','    assert cs_friend_se == '+str(se)+' and cs_worked_with_se_day2 == '+str(bool(se)),
 '    click until label cs_check_part05_sl_arrived','    pause 0.5','    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_three_clubs")',
 '    click until label cs_check_part05_sl_'+('helped' if sl else 'neutral'),'    pause 0.5','    $ cs_qa_capture("'+name+'_sl_branch")',
 '    click until label cs_check_part05_s37','    pause 0.5','    assert renpy.showing("bg ext_square_day")','    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_three_square")',
 '    click until label cs_check_part05_viola_arrived','    pause 0.5','    assert cs_met_viola and cs_day02_poster_posted','    assert renpy.showing("cs") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_viola")',
 '    click until label cs_check_part05_viola_left','    pause 0.5','    assert not renpy.showing("cs")','    assert renpy.showing("sl") and renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_viola_left")',
 '    click until label cs_check_part05_companions_left','    pause 0.5','    assert not renpy.showing("sl") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_departed")',
 '    click until label cs_check_part05_s38','    pause 0.5','    assert renpy.showing("cs_darya") and not renpy.showing("cs")','    $ cs_qa_capture("'+name+'_private_walk")',
 '    click until label cs_check_part05_hand_in_hand','    pause 1.0','    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")','    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")','    $ cs_qa_capture("'+name+'_hand_in_hand")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-cg")','    $ cs_friend_se = 99','    $ renpy.load("'+name+'-cg")','    pause 0.5','    assert cs_friend_se == '+str(se)+' and renpy.showing("cs_cg_lena_darya_hand_in_hand_day")',
 '    click until label cs_check_part05_pending','    pause 3.0','    assert not cs_day02_done and cs_day02_part05_complete','    assert cs_day02_poster_finished and cs_day02_poster_posted','    assert cs_friend_se == '+str(se),
 '    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part05_prior_friends',
 '    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")','    assert renpy.music.get_playing() is None','    assert renpy.get_screen("cs_day02_walk_continue_screen") is not None',
 '    assert ('+repr('высокую лавку')+' in u" ".join(x.what for x in _history_list)) == '+str(bool(mi)),
 '    assert ('+repr('спасибо ещё раз за помощь с коробками')+' in u" ".join(x.what for x in _history_list)) == '+str(bool(sl)),
 '    $ cs_qa_capture("'+name+'_end")']
 # The game keeps only a limited dialogue history. Check Sl's branch on the
 # square immediately after it, rather than after another 200 dialogue blocks.
 sl_assertion=out.pop(-2)
 out.insert(out.index('    $ cs_qa_capture("'+name+'_three_square")')+1,sl_assertion)
 if se and mi:
  out+=['    run Jump("cs_qa_semen_replay")','    click until run CSQAwaitMenu()','    "Давай сделаем надпись вместе"','    click until label cs_check_part05_pending','    assert cs_friend_se == 1 and cs_se_day2_awarded']
 out+=['    $ open(config.gamedir + "/mods/chuzaya_smena/qa/'+name+'_pass.txt", "w").write("PASS")','    run Quit(confirm=False)','']
(R/'qa/part05_routes_test.rpy').write_text('\n'.join(out),encoding='utf8')
print('Four Semen/Slavya/Miku combinations generated; Viola save variants covered')
