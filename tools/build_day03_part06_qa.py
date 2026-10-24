"""Generate native-only tests. No test script is installed in the mod."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
out='''# -*- coding: utf-8 -*-
init 95 python:
    import __builtin__ as cs_qa_builtin
    def cs_p6_capture(name):
        import json
        if cs_full_frame_cg_showing():
            assert not any(renpy.showing(t) for t in cs_presence_tags), "Portrait over full-frame CG"
        assert cs_qa_builtin.all(cs_p6_opaque(t) for t in cs_presence_tags if renpy.showing(t)), "Unfinished actor fade in settled frame"
        renpy.screenshot(config.basedir + "/p6_%s_%s.png" % (renpy.cs_p6_case,name))
        with open(config.basedir + "/p6_frames.jsonl","a") as f:
            json.dump(dict(case=renpy.cs_p6_case,frame=name,tags=sorted(renpy.get_showing_tags()),bounds={t:renpy.get_image_bounds(t) for t in cs_presence_tags if renpy.showing(t)}),f)
            f.write("\\n")
    def cs_p6_opaque(tag):
        d=renpy.game.context().scene_lists.get_displayable_by_tag("master",tag)
        return d is not None and getattr(getattr(d,"state",None),"alpha",1.0)>=0.999

label cs_qa_day03_p6:
    $ cs_reset_state()
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_slavya_known = True
    $ cs_friend_mi = renpy.cs_p6_mi
    $ cs_friend_un = renpy.cs_p6_un
    $ cs_met_un = cs_un_name_known = bool(cs_friend_un)
    $ cs_mz_map_lead = renpy.cs_p6_map
    $ cs_mz_book_requested_day3 = renpy.cs_p6_book
    $ cs_mz_catalog_checked_day3 = renpy.cs_p6_catalog
    $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else "after_lunch" if cs_mz_book_requested_day3 else None
    $ cs_day03_poster_location = renpy.cs_p6_poster
    $ cs_sl_poster_collected_day3 = bool(cs_day03_poster_location)
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_elbow_injury_day2 = 2
    $ cs_lena_no_sport_day2 = True
    $ cs_viola_spare_bandage = True
    $ cs_day03_documents_delivered = True
    $ cs_day03_documents_location = "administration"
    $ cs_day03_viola_check_done = True
    $ set_mode_adv()
    $ day_time()
    $ persistent.sprite_time = "day"
    jump cs_day03_part06

label cs_qa_p6_costume:
    $ cs_reset_state()
    $ cs_active = cs_darya_known = True
    $ set_mode_adv()
    $ day_time()
    $ persistent.sprite_time = "day"
    call cs_day03_83
    label cs_check_p6_costume_end:
    cs_narrator "Проверка завершена."
    return

label cs_qa_p6_guard:
    $ cs_reset_state()
    $ cs_active = cs_darya_known = True
    $ cs_friend_un = 1
    $ day_time()
    $ set_mode_adv()
    scene bg int_musclub_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show mi normal pioneer at cs_actor_left
    $ cs_presence_stage()
    call cs_day03_miku_arrangement_choice
    call cs_day03_miku_arrangement_choice
    call cs_day03_alice_music_choice
    call cs_day03_alice_music_choice
    call cs_day03_un_art_choice
    call cs_day03_un_art_choice
    label cs_check_p6_guard_end:
    cs_narrator "Проверка завершена."
    return

label cs_qa_p6_phone:
    $ cs_reset_state()
    $ cs_active = cs_darya_known = True
    $ set_mode_adv()
    $ day_time()
    scene bg int_house_of_mt_day
    call cs_day01_12
    return

label cs_qa_p6_legacy_book:
    $ cs_reset_state()
    $ cs_active = cs_darya_known = True
    $ cs_friend_mz = 1
    $ cs_lena_book_returned = False
    $ _history_list = []
    $ set_mode_adv()
    $ day_time()
    call cs_day03_89
    call cs_day03_90
    label cs_check_p6_legacy_book_end:
    cs_narrator "Проверка завершена."
    return

'''
setup='''    pause 0.5
    $ persistent.font_size = "small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _preferences.transitions = 2
    $ _test.force = True
    $ _test.timeout = 60.0
'''
choices=[('Послушать оба варианта и обсудить их с Мику','Не мешать репетиции и просто послушать'),('Спросить Алису о её игре и честно обсудить звучание','Сказать, что звучит хорошо, и не отвлекать'),('Спросить Лену о её рисунке и поделиться опытом','Не мешать Лене заканчивать рисунок')]
# MI, UN, catalog lead, requested book, catalog already checked, poster, choices.
cases=[(0,0,False,False,False,None,(0,0,0)),(1,1,True,True,False,'darya_folder',(1,1,1)),(0,2,True,False,True,'house',(1,0,1)),(1,0,False,True,False,'darya_folder',(0,1,0))]
for n,(mi,un,lead,book,catalog,poster,answers) in enumerate(cases):
 t='testcase cs_day03_p6_%d:\n'%n+setup+''.join('    $ renpy.cs_p6_%s = %r\n'%(k,v) for k,v in dict(case=n,mi=mi,un=un,map=lead,book=book,catalog=catalog,poster=poster).items())
 t+='''    run Start("cs_qa_day03_p6")
    pause 1.0
    assert cs_day03_part06_started
    $ cs_p6_capture("start")
'''
 if lead and not catalog:t+='''    click until label cs_check_day03_113_catalog
    pause 0.4
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya") and not renpy.showing("mz")
    $ cs_p6_capture("catalog")
    click until label cs_check_day03_113_catalog_done
    assert cs_mz_catalog_checked_day3
    click until label cs_check_day03_113_library_left
    assert not renpy.showing("cs_zhenya")
'''
 t+='''    click until label cs_check_day03_114_cast
    pause 0.4
    assert cs_qa_builtin.all(renpy.showing(t) and cs_p6_opaque(t) for t in ("mi","dv","cs_darya"))
    assert renpy.get_image_bounds("mi")[0] < renpy.get_image_bounds("dv")[0] < renpy.get_image_bounds("cs_darya")[0]
    $ cs_p6_capture("music_cast")
    click until label cs_check_day03_114_darya_piano
    pause 0.4
    assert renpy.music.get_playing() is None and renpy.music.get_playing(channel="cs_piano") is None
    $ cs_p6_capture("darya_piano")
'''
 if poster=='darya_folder':t+='    assert cs_day03_poster_location == "music_club_chair"\n'
 for i,num in enumerate(('115','117','119')):
  if i==1:t+='''    pause 0.4
    assert renpy.showing("dv") and not renpy.showing("cs_darya") and not renpy.showing("mi")
    $ cs_p6_capture("alice_focus")
'''
  if i==2:t+='''    click until label cs_check_day03_118_music_left
    assert not renpy.showing("mi") and not renpy.showing("dv")
    click until label cs_check_day03_118_un
    pause 0.4
    assert renpy.showing("un") and renpy.showing("cs_darya")
    $ renpy.cs_p6_un_bounds = renpy.get_image_bounds("un")
    $ cs_p6_capture("un_seated")
'''
  t+='    click until label cs_check_day03_%s_menu\n    "%s"\n'%(num,choices[i][0 if answers[i] else 1])
  if i==2 and un+answers[i]>=2 and answers[i]:t+='''    click until label cs_check_day03_119_invitation
    pause 0.4
    assert renpy.get_image_bounds("un")[1:] == renpy.cs_p6_un_bounds[1:]
    $ cs_p6_capture("art_invitation")
'''
  t+='    click until label cs_check_day03_%s_result\n'%num
  if i==0:t+='''    $ renpy.take_screenshot()
    $ renpy.save("p6_award")
    $ renpy.load("p6_award")
    pause 0.4
'''
  t+='    assert cs_friend_%s == %d\n'%(['mi','dv','un'][i],[mi,0,un][i]+answers[i])
 t+='''    click until label cs_check_day03_120_bench_left
    assert not renpy.showing("un") and renpy.showing("cs_darya")
    click until label cs_check_day03_120_horn
    assert cs_day03_lunch_horn_played
    click until label cs_check_day03_120_sl
    pause 0.4
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_p6_capture("slavya")
    click until label cs_check_day03_120_mz
    pause 0.4
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya") and not renpy.showing("sl")
    $ cs_p6_capture("zhenya")
    click until label cs_check_day03_part06_complete
    pause 0.4
    assert cs_day03_part06_done and cs_day03_lunch_arrived
    assert bool(cs_un_sketch_invite_day3) == '''+str(bool(answers[2] and un+answers[2]>=2))+'''
    assert cs_mi_day3_arrangement_help == '''+str(bool(answers[0]))+'''
    assert cs_dv_music_talk_day3 == '''+str(bool(answers[1]))+'''
    assert cs_un_day3_art_talk == '''+str(bool(answers[2]))+'''
    assert cs_mz_catalog_checked_day3 == '''+str(bool(lead or catalog))+'''
    assert cs_mz_book_requested_day3 == renpy.cs_p6_book
    assert cs_day03_poster_location == renpy.cs_p6_poster
    assert cs_lena_elbow_injury_day2 == 2 and cs_lena_no_sport_day2 and cs_viola_spare_bandage
    assert cs_day03_documents_location == "administration"
    assert renpy.showing("bg int_dining_hall_people_day")
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not any(renpy.showing(t) for t in ("mi","dv","un","sl","cs_semen","cs"))
    $ cs_p6_capture("complete")
    $ open(config.basedir + "/p6_'''+str(n)+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

'''
 out+=t
out+='testcase cs_day03_p6_costume:\n'+setup+'''    $ renpy.cs_p6_case = "costume"
    run Start("cs_qa_p6_costume")
    click until label cs_check_day03_83_underwear
    pause 0.5
    assert renpy.showing("cs_darya neutral underwear normal") and cs_p6_opaque("cs_darya")
    $ renpy.cs_p6_costume_bounds = renpy.get_image_bounds("cs_darya")
    $ cs_p6_capture("neutral")
    $ renpy.take_screenshot()
    $ renpy.save("p6_costume")
    $ renpy.load("p6_costume")
    pause 0.4
    assert renpy.showing("cs_darya neutral underwear normal")
    click until label cs_check_day03_83_hair_touch
    pause 0.4
    assert renpy.showing("cs_darya hair_touch underwear normal")
    $ cs_p6_capture("hair_touch")
    click until label cs_check_day03_83_turned_away
    pause 0.4
    assert not renpy.showing("cs_darya")
    $ cs_p6_capture("turned_away")
    click until label cs_check_day03_83_dressed
    pause 0.5
    assert renpy.showing("cs_darya neutral pioneer normal") and cs_p6_opaque("cs_darya")
    assert renpy.get_image_bounds("cs_darya") == renpy.cs_p6_costume_bounds
    $ cs_p6_capture("dressed")
    click until label cs_check_p6_costume_end
    assert "underwear" not in renpy.get_attributes("cs_darya")
    $ open(config.basedir + "/p6_costume_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

testcase cs_day03_p6_guard:
'''+setup+'''    run Start("cs_qa_p6_guard")
'''
for index,pair in enumerate(choices):
 for attempt in range(2):
  if index or attempt:out+='    click until label cs_check_day03_'+('115','117','119')[index]+'_menu\n'
  out+='    "'+pair[0]+'"\n'
out+='''    click until label cs_check_p6_guard_end
    assert cs_friend_mi == 1 and cs_friend_dv == 1 and cs_friend_un == 2
    assert cs_mi_day3_arrangement_help and cs_dv_music_talk_day3 and cs_un_day3_art_talk and cs_un_sketch_invite_day3
    $ open(config.basedir + "/p6_guard_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
out+='\ntestcase cs_day03_p6_phone:\n'+setup+'''    $ renpy.cs_p6_case = "phone"
    run Start("cs_qa_p6_phone")
    click until label cs_check_day01_part03_phone_off
    pause 0.6
    assert bool(renpy.get_screen("cs_phone"))
    $ cs_p6_capture("off_handset")
    click until label cs_check_day01_part03_calculator
    pause 0.4
    assert not bool(renpy.get_screen("cs_phone"))
    $ open(config.basedir + "/p6_phone_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

testcase cs_day03_p6_credits:
'''+setup+'''    $ renpy.cs_p6_case = "credits"
    run Start("chuzhaya_smena_start")
    pause 6.8
    assert bool(renpy.get_screen("cs_opening_credits_screen"))
    $ cs_p6_capture("three_lines")
    pause 6.2
    assert not bool(renpy.get_screen("cs_opening_credits_screen"))
    $ open(config.basedir + "/p6_credits_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

testcase cs_day03_p6_legacy_book:
'''+setup+'''    $ renpy.cs_p6_case = "legacy_book"
    run Start("cs_qa_p6_legacy_book")
    click until label cs_check_p6_legacy_book_end
    assert not cs_lena_book_returned
    assert not any(u"Наш разговор о книге" in x.what or u"Ты вчера довольно быстро дочитала" in x.what for x in _history_list)
    $ cs_p6_capture("no_invented_loan")
    $ open(config.basedir + "/p6_legacy_book_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_part06_test.rpy.txt').write_text(out,encoding='utf8')
print('Generated four route tests, costume save/load, repeated-choice guards.')

