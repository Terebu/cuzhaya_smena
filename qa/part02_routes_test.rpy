# -*- coding: utf-8 -*-
testcase cs_accord_leave:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    assert renpy.has_image("bg ext_musclub_day") and renpy.has_image("bg int_musclub_day")
    assert renpy.loadable(cs_darya_piano_track) and renpy.loadable(cs_miku_piano_track)
    assert renpy.loadable("sound/ambiences/music_club_day.ogg")
    run Start("cs_qa_part02_load")
    pause 1.0
    $ cs_friend_mi = 0
    $ cs_day02_miku_listened = None
    run Jump("cs_qa_part02_path")
    click until label cs_check_part02_japanese
    pause 1.0
    assert renpy.showing("cs_camp_path_day")
    $ cs_qa_capture("cs_accord_leave_japanese")
    click until label cs_check_part02_s17
    pause 2.5
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_accord_leave_club")
    click until label cs_check_d2_piano_darya
    pause 2.0
    assert renpy.showing("cs_cg_darya_piano_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("mi")
    assert renpy.music.get_playing(channel="cs_piano") == cs_darya_piano_track
    $ cs_qa_capture("cs_accord_leave_darya_piano")
    $ renpy.take_screenshot()
    $ renpy.save("cs_accord_leave-piano")
    $ cs_friend_mi = 99
    $ renpy.load("cs_accord_leave-piano")
    pause 1.0
    assert cs_friend_mi == 0 and renpy.showing("cs_cg_darya_piano_day")
    click until label cs_check_part02_menu
    pause 1.0
    assert cs_met_mi and cs_mi_name_known
    assert renpy.music.get_playing(channel="cs_piano") is None
    $ cs_qa_capture("cs_accord_leave_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_accord_leave-menu")
    $ cs_friend_mi = 99
    $ renpy.load("cs_accord_leave-menu")
    pause 1.0
    assert cs_friend_mi == 0
    "Поблагодарить Мику и пойти на линейку"
    click until label cs_check_part02_s20
    assert cs_friend_mi == 0
    pause 1.0
    assert not renpy.showing("mi") and not renpy.showing("cs_semen")
    assert renpy.music.get_playing(channel="cs_piano") is None
    click until label cs_check_part02_square
    pause 1.0
    assert renpy.showing("bg ext_square_day")
    $ cs_qa_capture("cs_accord_leave_square")
    click until label cs_check_part02_pending
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 0
    $ cs_qa_capture("cs_accord_leave_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_accord_leave_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_accord_listen:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    assert renpy.has_image("bg ext_musclub_day") and renpy.has_image("bg int_musclub_day")
    assert renpy.loadable(cs_darya_piano_track) and renpy.loadable(cs_miku_piano_track)
    assert renpy.loadable("sound/ambiences/music_club_day.ogg")
    run Start("cs_qa_part02_load")
    pause 1.0
    $ cs_friend_mi = 0
    $ cs_day02_miku_listened = None
    run Jump("cs_qa_part02_path")
    click until label cs_check_part02_japanese
    pause 1.0
    assert renpy.showing("cs_camp_path_day")
    $ cs_qa_capture("cs_accord_listen_japanese")
    click until label cs_check_part02_s17
    pause 2.5
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_accord_listen_club")
    click until label cs_check_d2_piano_darya
    pause 2.0
    assert renpy.showing("cs_cg_darya_piano_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("mi")
    assert renpy.music.get_playing(channel="cs_piano") == cs_darya_piano_track
    $ cs_qa_capture("cs_accord_listen_darya_piano")
    $ renpy.take_screenshot()
    $ renpy.save("cs_accord_listen-piano")
    $ cs_friend_mi = 99
    $ renpy.load("cs_accord_listen-piano")
    pause 1.0
    assert cs_friend_mi == 0 and renpy.showing("cs_cg_darya_piano_day")
    click until label cs_check_part02_menu
    pause 1.0
    assert cs_met_mi and cs_mi_name_known
    assert renpy.music.get_playing(channel="cs_piano") is None
    $ cs_qa_capture("cs_accord_listen_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_accord_listen-menu")
    $ cs_friend_mi = 99
    $ renpy.load("cs_accord_listen-menu")
    pause 1.0
    assert cs_friend_mi == 0
    "Остаться и послушать репетицию Мику"
    click until label cs_check_d2_piano_miku
    pause 2.0
    assert cs_friend_mi == 1
    assert renpy.showing("cs_cg_miku_piano_day")
    assert not renpy.showing("mi") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing(channel="cs_piano") == cs_miku_piano_track
    $ cs_qa_capture("cs_accord_listen_miku_piano")
    click until label cs_check_d2_piano_miku_again
    pause 2.0
    assert renpy.showing("cs_cg_miku_piano_day")
    $ cs_qa_capture("cs_accord_listen_miku_again")
    click until label cs_check_part02_s20
    assert cs_friend_mi == 1
    pause 1.0
    assert not renpy.showing("mi") and not renpy.showing("cs_semen")
    assert renpy.music.get_playing(channel="cs_piano") is None
    click until label cs_check_part02_square
    pause 1.0
    assert renpy.showing("bg ext_square_day")
    $ cs_qa_capture("cs_accord_listen_square")
    click until label cs_check_part02_pending
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 1
    $ cs_qa_capture("cs_accord_listen_end")
    run Jump("cs_qa_part02_replay")
    click until label cs_check_part02_menu
    "Остаться и послушать репетицию Мику"
    click until label cs_check_part02_pending
    pause 1.0
    assert cs_friend_mi == 1
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_accord_listen_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
