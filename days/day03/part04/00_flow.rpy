# -*- coding: utf-8 -*-
label cs_day03_part04:
    hide screen cs_day03_part03_wait_screen
    call cs_day03_96 from cs_return_0f7f319f6cc9d669689e
    jump cs_day03_part04_visit

label cs_day03_part04_legacy:
    # An older save has already finished the previous Semen conversation.
    hide screen cs_day03_part03_wait_screen
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    jump cs_day03_part04_visit

label cs_day03_part04_visit:
    if cs_day03_part04_done:
        jump cs_day03_part05_pending
    if cs_viola_friend_before_day3 is None:
        $ cs_viola_friend_before_day3 = cs_friend_viola
    call cs_day03_97 from cs_return_d6d1a2381f7f25b08b42
    call cs_day03_98 from cs_return_000429083c448316ea3e
    call cs_day03_99 from cs_return_0be75fb647e210207683
    call cs_day03_100 from cs_return_611a48797bff8c0037ac
    call cs_day03_viola_choice from cs_return_7be1c64234260274e964
    call cs_day03_101 from cs_return_3912e7bc1994ace5cdf8
    call cs_day03_102 from cs_return_dc5994431d405fe1d190
    call cs_day03_103 from cs_return_ab4aa3f13ae54db7d220
    $ cs_day03_part04_done = True
    jump cs_day03_part05

label cs_day03_viola_choice:
    if cs_viola_friend_before_day3 is None:
        $ cs_viola_friend_before_day3 = cs_friend_viola
    label cs_check_day03_101_menu:
    menu:
        "Предложить Виоле помочь с учётом материалов":
            if not cs_viola_day3_awarded:
                $ cs_friend_viola += 1
                $ cs_viola_day3_awarded = True
            $ cs_helped_viola_day3 = True
            call cs_day03_100a from cs_return_320a68da95a31e401256
        "Поблагодарить и не задерживать Виолу":
            call cs_day03_100b from cs_return_ba3a102dc3f178183213
    label cs_check_day03_101_result:
    return

label cs_day03_part05_pending:
    label cs_check_day03_part04_complete:
    jump cs_day03_part05_legacy

label cs_check_day03_103_library:
    jump cs_day03_part05_legacy
label cs_check_day03_103_square:
    jump cs_day03_part05_legacy

# Named checkpoints retained for saves from the superseded ending of part 3.
label cs_check_day03_95_semen_return:
    call cs_day03_96 from cs_return_6946917fef666697d8b5
    jump cs_day03_part04_visit
label cs_check_day03_95_semen_left:
    jump cs_day03_part04_legacy
label cs_check_day03_95_reflection:
    jump cs_day03_part04_legacy

screen cs_day03_part04_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Приём по предварительной наглости" size 26
            if cs_day03_part05_route == "library":
                text "Дальше — встреча с Женей в библиотеке." size 22
            else:
                text "Дальше — прогулка по лагерю." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]

label cs_day03_alice_medpoint_choice:
    label cs_check_day03_102_menu:
    menu:
        "Спросить, всё ли в порядке, и не делать из этого представление":
            if not cs_dv_medpoint_day3:
                $ cs_friend_dv += 1
                $ cs_dv_medpoint_day3 = True
            call cs_day03_102a from cs_return_8d528a45fe62ca515bd6
        "Не вмешиваться и пожелать Алисе удачи":
            call cs_day03_102b from cs_return_691653877f93c176e367
    label cs_check_day03_102_result:
    return

# Compatibility with a save at the former end of the medical visit.
label cs_check_day03_102_viola_left:
    $ cs_actor_exit(["cs"])
    return
