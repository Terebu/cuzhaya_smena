# -*- coding: utf-8 -*-
label cs_day02_41:
    $ save_name = "Чужая смена — День 2: Что мы скажем Семёну?"
    $ cs_part05_live = False
    $ cs_part06_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part06_s41:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда мы почти закончили обедать, Семён отодвинул тарелку."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Значит, идём по дороге, смотрим, что дальше, и возвращаемся?"
    cs_narrator "Я кивнула."
    cs_ls "Примерно."
    cs_sy "А если ничего не найдём?"
    cs_narrator "Я ненадолго задумалась."
    cs_narrator "Перед глазами снова появились ворота."
    cs_narrator "Тот самый автобус, которого больше не было."
    cs_narrator "И воспоминание о зимней Москве."
    cs_narrator "Обычная остановка."
    cs_narrator "Холодный воздух."
    cs_narrator "Люди, занятые своими делами."
    cs_narrator "Ещё два дня назад всё казалось таким понятным."
    cs_narrator "А теперь я сидела в советской столовой и обсуждала, существует ли вообще дорога из пионерского лагеря во внешний мир."
    cs_th "Забавно."
    cs_th "Пока мы разговариваем о маршруте, я даже не могу заставить себя произнести вслух, чего именно боюсь."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Он ждал ответа."
    cs_narrator "Можно было ограничиться обычным планом."
    cs_narrator "Сказать, что мы просто посмотрим дорогу и вернёмся."
    cs_narrator "Или признаться, что боюсь обнаружить нечто гораздо хуже отсутствия указателей."
    return
