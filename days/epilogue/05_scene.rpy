# -*- coding: utf-8 -*-

label cs_epilogue_05:
    $ cs_ep_lock_route()
    if cs_ep_guest_mode == "choose":
        call cs_epilogue_choose_contact from cs_ep_final_legacy_contact_return
    stop music fadeout 1.0
    cs_narrator "После звонка за дверью на секунду стало тихо, а потом послышалась быстрая возня — знакомый звук человека, который в последний момент пытается задвинуть ногой что-то лишнее подальше от прихожей."
    $ cs_rev_sfx("sound/sfx/lock_close.ogg", 0.17)
    cs_narrator "Щёлкнул верхний замок, потом нижний, и дверь открылась."
    $ cs_d7_hide_portraits()
    show cs_cg_epi_semen_door with dissolve
    cs_narrator "На пороге стоял Семён."
    cs_narrator "В тёмной футболке, слегка лохматый, с неловким и сразу немного защитным видом человека, который вообще не планировал пускать к себе гостей как минимум до весны."
    cs_narrator "Увидев нас обеих в зимних куртках, с красными от мороза щеками и пакетом из пекарни, он на пару секунд просто завис, моргнул, потом посмотрел на меня, на Дашу и снова на меня."

    cs_sy "Э-э… привет."
    cs_narrator "Сказал он наконец, чуть откашлявшись."
    cs_sy "Так вы правда… ну, то есть вы реально здесь."
    cs_sy "Не приснилось."
    cs_ls "Не приснилось, Сёмочка."
    cs_narrator "Спокойно ответила я, поднимая пакет с печеньем."
    cs_ls "Зайти можно, или будем проводить проверку реальности прямо на лестничной клетке?"
    cs_sy "Да, конечно, проходите."
    cs_narrator "Спохватился он, отступая в тесную прихожую и тут же добавляя привычным ворчливым тоном."
    cs_sy "Только сильно по сторонам не смотрите, ладно?"
    cs_sy "Я тут вообще-то собирался разобрать на днях."
    $ cs_ep_found_semen = True
    $ cs_rev_music(cs_music_purrple_calm_waters, 0.11, 2.0)
    $ cs_d7_ambience("sound/sfx/computer_noise.ogg", 0.075)

    if cs_ep_guest == "sl":
        $ cs_d7_scene("cs_bg_epi_semen_clean")
        scene cs_bg_epi_semen_clean with dissolve
        $ cs_ep_room_clean = True
    else:
        if cs_ep_guest_mode == "single":
            $ cs_d7_scene("cs_bg_epi_semen_partial")
            scene cs_bg_epi_semen_partial with dissolve
        else:
            $ cs_d7_scene("cs_bg_epi_semen_dirty")
            scene cs_bg_epi_semen_dirty with dissolve
    $ cs_rev_sfx("sound/sfx/paper_bag.ogg", 0.12)
    cs_narrator "Мы разулись и повесили куртки на перегруженную вешалку."
    cs_narrator "Мы зашли в комнату."
    cs_narrator "Однокомнатная квартира на высоком этаже выглядела до смешного узнаваемо — обычная берлога хиккикомори, только честно дожившая до января две тысячи двадцать шестого года."
    cs_narrator "В углу у шкафа местами отошли старые обои, на полу валялись вещи без всякой системы."
    cs_narrator "Напротив входа, у большого окна с чуть сдвинутыми шторами, за которым белели заснеженные крыши многоэтажек, стоял письменный стол — главный центр всей комнаты."
    cs_narrator "На столе гудел системник, а на широкоформатном мониторе оставался открытым мессенджер."
    cs_narrator "Я узнала своё сообщение про автобус."
    show cs_epi_semen neutral home at cs_ep_actor_right
    show cs_epi_darya soft_smile casual at cs_ep_actor_left
    with dissolve
    cs_da "Ну что ж."
    cs_narrator "Тихо хмыкнула Даша у меня за плечом, оглядывая комнату."
    cs_da "По крайней мере, он точно настоящий."
    show cs_epi_darya soft_smile casual with cs_sprite_change
    cs_da "Такой бардак из головы не выдумаешь."
    show cs_epi_semen angry home with cs_sprite_change
    cs_sy "Я слышу, вообще-то."
    cs_narrator "Буркнул Семён, неловко переминаясь с ноги на ногу."
    jump cs_epilogue_06

label cs_epilogue_choose_contact:
    if cs_ep_guest_mode != 'choose':
        return
    cs_narrator "Прежде чем выезжать, мы заглянули в открытые профили остальных."
    cs_narrator "Оказалось, нескольким нашим знакомым тоже можно было написать."
    cs_da "Хочешь кого-нибудь позвать с нами?"
    $ cs_ep_contact_page = 0
    while cs_ep_guest_mode == "choose":
        menu:
            "Ответить Славе" if 'sl' in cs_ep_guest_ties[cs_ep_contact_page * 3:cs_ep_contact_page * 3 + 3]:
                $ cs_ep_choose_guest('sl')
            "Ответить Алисе" if 'dv' in cs_ep_guest_ties[cs_ep_contact_page * 3:cs_ep_contact_page * 3 + 3]:
                $ cs_ep_choose_guest('dv')
            "Ответить Мику" if 'mi' in cs_ep_guest_ties[cs_ep_contact_page * 3:cs_ep_contact_page * 3 + 3]:
                $ cs_ep_choose_guest('mi')
            "Ответить Жене" if 'mz' in cs_ep_guest_ties[cs_ep_contact_page * 3:cs_ep_contact_page * 3 + 3]:
                $ cs_ep_choose_guest('mz')
            "Ответить Лене Тихоновой" if 'un' in cs_ep_guest_ties[cs_ep_contact_page * 3:cs_ep_contact_page * 3 + 3]:
                $ cs_ep_choose_guest('un')
            "Другие контакты" if len(cs_ep_guest_ties) > 3 and cs_ep_contact_page == 0:
                $ cs_ep_contact_page = 1
            "Назад" if cs_ep_contact_page == 1:
                $ cs_ep_contact_page = 0
    cs_narrator "Я написала, что мы едем к Семёну, и прислала адрес."
    return
