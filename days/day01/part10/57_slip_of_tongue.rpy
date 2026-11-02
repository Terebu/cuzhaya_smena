# -*- coding: utf-8 -*-
label cs_day01_57:
    $ save_name = "Чужая смена — День 1: Лишнее слово"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music cs_day_music_doubt fadeout 2.0 fadein 2.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я аккуратно поставила книгу обратно на полку."
    cs_narrator "Раздражение Жени сменялось любопытством. Настороженным, правда."
    # cs_speaker: present
    show cs_zhenya normal pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Значит, вы обе сегодня приехали?"
    cs_ls "Да."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И сразу решили идти в библиотеку?"
    cs_ls "Не сразу. До этого успели познакомиться с половиной лагеря."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "С половиной?"
    cs_ls "Возможно, немного преувеличила."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо улыбнулась."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И что, всё здесь настолько интересно?"
    cs_narrator "Я оглядела полки, окна, стол. Женю."
    cs_th "Вот это вопрос."
    cs_narrator "Меня интересовали и книги, и каталоги. Но сильнее хотелось понять, насколько этот мир похож на игру."
    cs_narrator "И люди в нём — на тех, кого я помнила."
    cs_ls "Скорее непривычно видеть всё это не на экране."
    cs_narrator "Женя нахмурилась."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "На каком экране?"
    cs_narrator "Я замерла."
    cs_th "Соколова снова рассказала лишнее."
    cs_narrator "Дарья медленно повернулась ко мне."
    # cs_darya_variety: reaction
    show cs_darya shy_bend pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен…"
    cs_narrator "Я подняла ладонь."
    cs_ls "Да, я поняла."
    cs_narrator "Женя посмотрела на нас обеих."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что поняла?"
    cs_ls "Что стоило выбрать другое выражение."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А теперь объясни, какое имела в виду."
    cs_narrator "Я закрыла глаза, вздохнула и посмотрела на неё."
    cs_ls "Хорошо."
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music cs_day_music_doubt fadeout 2.0 fadein 2.5
    cs_ls "Только сначала один вопрос."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Какой?"
    cs_ls "Если я расскажу что-то совершенно невероятное, ты хотя бы дослушаешь до конца?"
    # cs_darya_variety: reaction
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она скрестила руки."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Если не будешь тянуть время."
    cs_ls "Справедливо."
    cs_narrator "Дарья посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты уверена?"
    cs_narrator "Я ответила не сразу."
    cs_ls "Нет."
    cs_ls "Но теперь, кажется, всё равно придётся что-нибудь объяснить."
    return
