# -*- coding: utf-8 -*-
label cs_day01_47:
    $ save_name = "Чужая смена — День 1: Первая развилка"
    show un normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["un", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_th "Может, стоит познакомиться?"
    cs_th "Хотя, с другой стороны, девушка явно никуда не спешит знакомиться с человеком, который только что едва её не сбил."
    label cs_check_day01_part09_choice:
    if cs_part09_choice is None:
        menu:
            "Остановиться и познакомиться":
                $ cs_friend_un += 1
                $ cs_met_un = True
                $ cs_part09_choice = "meet"
            "Извиниться и пройти дальше":
                $ cs_part09_choice = "pass"
    if cs_part09_choice == "meet":
        call cs_day01_48_a from cs_return_7f510a0f65d2e1805289
    else:
        call cs_day01_48_b from cs_return_bcb7eaa58b095bf186f6
    return
