# -*- coding: utf-8 -*-
label cs_day02_41a:
    $ save_name = "Чужая смена — День 2: Без шуток"
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
    label cs_check_part06_s41a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я некоторое время смотрела на стакан."
    cs_narrator "Потом подняла глаза."
    cs_ls "Если ничего не найдём, вернёмся. Но, Семён, меня тревожит не это."
    cs_narrator "Он нахмурился."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А что тогда?"
    cs_narrator "Я глубоко вдохнула."
    cs_ls "Меня пугает, что за воротами может вообще ничего не оказаться. Не в смысле пустой дороги. А в смысле, что сколько бы мы ни шли, никуда не придём."
    cs_narrator "Семён перестал улыбаться."
    cs_narrator "Дарья тоже внимательно слушала."
    cs_ls "Вчера я пыталась убедить себя, что это обычный лагерь в необычных обстоятельствах. Что где-нибудь есть город, автобусная станция, железная дорога. Что нужно просто добраться туда — и мы хотя бы сможем понять, где оказались."
    cs_narrator "Я немного помолчала."
    cs_ls "А сегодня увидела, что автобус исчез. И впервые подумала: вдруг у этого места вообще нет нормального выхода?"
    cs_narrator "Семён опустил взгляд."
    cs_narrator "Несколько секунд он молчал."
    cs_narrator "Потом медленно кивнул."
    show cs_semen serious pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я тоже об этом думал."
    cs_narrator "Я посмотрела на него."
    cs_sy "В первый день всё пытался вспомнить, куда ехал, где была остановка, как уснул. Думал, может, пропустил что-то очевидное. Но чем больше вспоминал, тем меньше понимал."
    cs_narrator "Он невесело усмехнулся."
    cs_sy "Наверное, поэтому я так обрадовался, когда вы вчера появились. До этого я вообще не знал, можно ли с кем-нибудь нормально обсудить происходящее."
    cs_narrator "Я вспомнила наше знакомство в столовой."
    cs_narrator "Тогда Семён выглядел растерянным."
    cs_narrator "И я, конечно, почти сразу начала задавать ему вопросы об автобусе."
    cs_th "А ведь он действительно провёл здесь целый день один."
    cs_th "Среди людей, которые не понимали, почему он настолько удивлён происходящим."
    cs_ls "Тогда хорошо, что мы встретились."
    cs_narrator "Семён посмотрел на меня."
    cs_narrator "Затем улыбнулся."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Да. Хорошо."
    cs_narrator "Дарья слегка наклонилась к столу."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И поэтому не будем действовать поодиночке. Что бы там ни было, нам лучше знать, что происходит со всеми троими."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    cs_sy "Договорились."
    cs_th "Надо же."
    cs_th "Оказалось, можно поговорить с человеком совершенно серьёзно — и ничего страшного не случится."
    return
