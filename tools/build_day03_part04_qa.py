from pathlib import Path
R=Path(__file__).resolve().parent.parent
out='''# -*- coding: utf-8 -*-
init 95 python:
    def cs_p4_capture(name):
        renpy.screenshot(config.basedir + "/p4_%s_%s.png" % (renpy.cs_p4_case,name))
    def cs_p4_opaque(tag):
        d=renpy.game.context().scene_lists.get_displayable_by_tag("master",tag)
        return d is not None and getattr(getattr(d,"state",None),"alpha",1.0)>=0.999

label cs_qa_day03_p4:
    $ cs_reset_state()
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_friend_viola = 0 if renpy.cs_p4_real else renpy.cs_p4_v
    $ cs_viola_spare_bandage = bool(renpy.cs_p4_spare)
    $ cs_mz_map_lead = bool(renpy.cs_p4_map)
    $ cs_mz_book_requested_day3 = bool(renpy.cs_p4_map)
    $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else None
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_elbow_injury_day2 = 2
    $ cs_lena_no_sport_day2 = True
    $ set_mode_adv()
    $ day_time()
    $ persistent.sprite_time = "day"
    if renpy.cs_p4_real:
        call cs_day02_viola_choice
        call cs_day02_viola_second_choice
        call cs_day02_concert
    label cs_check_p4_fixture:
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    play music "sound/music/my_daily_life.ogg"
    if renpy.cs_p4_legacy:
        $ cs_day03_part03_done = True
        jump cs_day03_part04_pending
    call cs_day03_95
    $ cs_day03_part03_done = True
    jump cs_day03_part04

'''
cases=[(v,h,(v+int(h))%2,False,False,False) for v in (0,1,2) for h in (False,True)]
cases += [(2,True,True,True,False,False),(1,False,False,False,True,False),(2,True,True,False,False,True)]
for n,(v,help,map,spare,legacy,real) in enumerate(cases):
 t=f'''testcase cs_day03_p4_{n}:
    pause 0.5
    $ renpy.cs_p4_case = {n}
    $ renpy.cs_p4_v = {v}
    $ renpy.cs_p4_help = {help}
    $ renpy.cs_p4_map = {map}
    $ renpy.cs_p4_spare = {spare}
    $ renpy.cs_p4_legacy = {legacy}
    $ renpy.cs_p4_real = {real}
    $ persistent.font_size = "small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 60.0
    run Start("cs_qa_day03_p4")
'''
 if real:t+='''    "Предложить Виоле помощь с материалами"
    click until label cs_check_part07_menu
    "Немного поговорить с Виолой перед уходом"
    click until label cs_check_p4_fixture
    assert cs_friend_viola == 2 and cs_viola_spare_bandage
'''
 if not legacy:t+='''    click until label cs_check_day03_96_semen
    pause 0.4
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    assert cs_p4_opaque("cs_semen")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_p4_capture("semen")
    click until label cs_check_day03_96_semen_left
    assert not renpy.showing("cs_semen")
'''
 t+='''    click until label cs_check_day03_97_aidpost
    pause 0.4
    assert renpy.showing("bg ext_aidpost_day") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_zhenya")
    $ cs_p4_capture("entrance")
    click until label cs_check_day03_98
    pause 2.2
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    assert cs_p4_opaque("cs") and cs_p4_opaque("cs_darya")
    assert renpy.music.get_playing() is None
    $ renpy.cs_p4_viola_bounds = renpy.get_image_bounds("cs")
    $ renpy.cs_p4_darya_bounds = renpy.get_image_bounds("cs_darya")
    $ cs_p4_capture("medical_dialogue")
    click until label cs_check_day03_99_examination
    pause 0.4
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    assert renpy.get_image_bounds("cs")[1:] == renpy.cs_p4_viola_bounds[1:]
    assert renpy.get_image_bounds("cs_darya")[1:] == renpy.cs_p4_darya_bounds[1:]
    $ cs_p4_capture("examination")
    click until label cs_check_day03_99_dressed
    assert cs_day03_viola_check_done
    $ renpy.take_screenshot()
    $ renpy.save("p4_before_choice")
    $ renpy.load("p4_before_choice")
    pause 0.3
    assert cs_friend_viola == renpy.cs_p4_v and not cs_viola_day3_awarded
    click until label cs_check_day03_101_menu
    pause 0.4
    $ cs_p4_capture("choice")
'''
 if help:t+='''    "Предложить Виоле помочь с учётом материалов"
    click until label cs_check_day03_101_inventory_cg
    pause 0.5
    assert renpy.showing("cs_cg_lena_darya_medical_inventory_day")
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    assert cs_friend_viola == renpy.cs_p4_v + 1 and cs_viola_day3_awarded
    $ cs_p4_capture("inventory_cg")
    $ renpy.take_screenshot()
    $ renpy.save("p4_cg")
    $ renpy.load("p4_cg")
    pause 0.4
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_p4_capture("inventory_loaded")
    click until label cs_check_day03_101_inventory_return
    pause 0.4
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_cg_lena_darya_medical_inventory_day")
    $ cs_p4_capture("inventory_return")
'''
 else:t+='''    "Поблагодарить и не задерживать Виолу"
'''
 t+='''    click until label cs_check_day03_101_result
    assert cs_friend_viola == renpy.cs_p4_v + int(renpy.cs_p4_help)
    assert cs_viola_friend_before_day3 == renpy.cs_p4_v
    $ renpy.take_screenshot()
    $ renpy.save("p4_award")
    $ renpy.load("p4_award")
    pause 0.3
    assert cs_friend_viola == renpy.cs_p4_v + int(renpy.cs_p4_help)
    click until label cs_check_day03_103_outside
    pause 0.4
    assert not renpy.showing("cs") and not renpy.showing("cs_semen")
    assert renpy.showing("cs_darya")
    assert cs_viola_day3_bonus_seen == (renpy.cs_p4_v >= 2)
    assert cs_viola_spare_bandage == (renpy.cs_p4_spare or renpy.cs_p4_v >= 2)
    $ cs_p4_capture("outside")
    click until label cs_check_day03_103_reflection
    pause 0.4
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_p4_capture("reflection")
    click until label cs_check_day03_103_dialogue
    pause 0.4
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_p4_capture("dialogue_restored")
    click until label cs_check_day03_part04_complete
    pause 0.4
    assert cs_day03_part04_done and cs_day03_viola_check_done
    assert cs_day03_part05_route == ("library" if renpy.cs_p4_map else "square")
    assert cs_day03_library_visit_time == ("late_morning" if renpy.cs_p4_map else None)
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2 == 2 and cs_lena_no_sport_day2
    assert not renpy.showing("cs") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_p4_capture("next_part")
    $ open(config.basedir + "/p4_%s_PASS.txt" % renpy.cs_p4_case,"w").write("PASS")
    $ cs_reset_state()
    assert not cs_day03_part04_done and cs_viola_friend_before_day3 is None and not cs_viola_day3_awarded and not cs_viola_day3_bonus_seen
    run Quit(confirm=False)

'''
 out+=t
out+='''label cs_qa_day03_p4_guard:
    $ cs_reset_state()
    $ cs_active = True
    $ cs_friend_viola = 2
    $ set_mode_adv()
    $ day_time()
    scene bg int_aidpost_day
    show cs custom warm_smile medical normal at cs_viola_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    call cs_day03_viola_choice
    label cs_check_p4_guard_second:
    call cs_day03_viola_choice
    call cs_day03_102
    label cs_check_p4_guard_consumed:
    cs_narrator "Контроль полученного пакета."
    $ cs_viola_spare_bandage = False
    call cs_day03_102
    label cs_check_p4_guard_done:
    cs_narrator "Проверка завершена."
    return

testcase cs_day03_p4_guard:
    pause 0.5
    $ persistent.font_size = "small"
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 60.0
    run Start("cs_qa_day03_p4_guard")
    "Предложить Виоле помочь с учётом материалов"
    click until label cs_check_p4_guard_second
    "Предложить Виоле помочь с учётом материалов"
    click until label cs_check_p4_guard_consumed
    assert cs_friend_viola == 3 and cs_viola_friend_before_day3 == 2
    assert cs_viola_spare_bandage and cs_viola_day3_bonus_seen
    click until label cs_check_p4_guard_done
    assert not cs_viola_spare_bandage and cs_friend_viola == 3
    $ open(config.basedir + "/p4_guard_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_part04_test.rpy.txt').write_text(out,encoding='utf8')
print('QA template ready:',len(cases)+1,'cases')
