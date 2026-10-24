# -*- coding: utf-8 -*-
label cs_day03_part06:
    if cs_day03_part06_done:
        jump cs_day03_part07_pending
    hide screen cs_day03_part05_wait_screen
    $ cs_day03_part05_done = True
    $ cs_day03_part06_started = True
    if cs_mz_catalog_checked_day3:
        $ cs_day03_library_visit_time = "after_lunch" if cs_mz_book_requested_day3 else None
    $ cs_day03_part06_route = "library_then_music" if cs_mz_map_lead and not cs_mz_catalog_checked_day3 else "music"
    call cs_day03_113 from cs_return_5cb78a528a9f93579615
    if cs_mz_map_lead and not cs_mz_catalog_checked_day3:
        call cs_day03_113a from cs_return_cdd2ec3907bfb3dccf87
    call cs_day03_114 from cs_return_d2c1e79e6bfb9c2a1857
    call cs_day03_115 from cs_return_04b1197de8ed945d2e8b
    call cs_day03_116 from cs_return_49eca1b6384b1506c131
    call cs_day03_117 from cs_return_d33c4de4bdc576d6f4ca
    call cs_day03_118 from cs_return_9f7535b402a3a6cd2d8e
    call cs_day03_119 from cs_return_fbd40e921d9b2bc4a739
    call cs_day03_120 from cs_return_dccd5b48bbeb0f560403
    $ cs_day03_part06_done = True
    jump cs_day03_part07_pending

label cs_day03_miku_arrangement_choice:
    label cs_check_day03_115_menu:
    menu:
        "Послушать оба варианта и обсудить их с Мику":
            if not cs_mi_day3_awarded:
                $ cs_friend_mi += 1
                $ cs_mi_day3_awarded = True
            call cs_day03_115a from cs_return_31aac44972924d2075eb
            $ cs_mi_day3_arrangement_help = True
        "Не мешать репетиции и просто послушать":
            call cs_day03_115b from cs_return_08f82761e3ed47d32357
    label cs_check_day03_115_result:
    return

label cs_day03_alice_music_choice:
    label cs_check_day03_117_menu:
    menu:
        "Спросить Алису о её игре и честно обсудить звучание":
            if not cs_dv_day3_awarded:
                $ cs_friend_dv += 1
                $ cs_dv_day3_awarded = True
            call cs_day03_117a from cs_return_72aa951f1359af5b974b
            $ cs_dv_music_talk_day3 = True
        "Сказать, что звучит хорошо, и не отвлекать":
            call cs_day03_117b from cs_return_fc8e7d5a6da77fd55e30
    label cs_check_day03_117_result:
    return

label cs_day03_un_art_choice:
    label cs_check_day03_119_menu:
    menu:
        "Спросить Лену о её рисунке и поделиться опытом":
            if not cs_un_day3_awarded:
                $ cs_friend_un += 1
                $ cs_un_day3_awarded = True
            call cs_day03_119a from cs_return_13b7df66e0d76ca4aa05
            $ cs_un_day3_art_talk = True
        "Не мешать Лене заканчивать рисунок":
            call cs_day03_119b from cs_return_c81ac4aa3a3f10483a62
    label cs_check_day03_119_result:
    return

label cs_day03_part07_pending:
    label cs_check_day03_part06_complete:
    jump cs_day03_part07

screen cs_day03_part06_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Три творческие натуры и одна Соколова" size 26
            text "Дальше — обед и разговоры в столовой." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
