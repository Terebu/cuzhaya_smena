# -*- coding: utf-8 -*-
# Source: source/day01_part03.md.
label cs_day01_11:
    $ save_name = u"Чужая смена — День 1: Государственная машина"
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_play fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.28, delay=1.0, channel="ambience")
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show mt normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "sl", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_mt "Какую именно?"
    cs_narrator "Я посмотрела на собственную одежду."
    cs_ls "Например, пионерскую форму."
    cs_narrator "Ольга Дмитриевна приподняла бровь."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Пионерскую?"
    cs_ls "А почему нет? Никогда такую не носила."
    cs_narrator "Я взглянула на Дарью: алые волосы ниже плеч, зелёные глаза, невозмутимое лицо."
    cs_narrator "Представила её в пионерской форме и не смогла сдержать улыбку. Она заметила мгновенно."
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нет."
    cs_ls "Я ещё ничего не сказала."
    cs_da "Я вижу твой взгляд."
    cs_ls "Мне просто стало интересно."
    cs_da "Нет."
    cs_narrator "Я повернулась к Ольге Дмитриевне."
    cs_ls "А вот Дарье, мне кажется, пионерская форма особенно подойдёт."
    # cs_darya_variety: reaction
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_ls "Что?"
    cs_da "Нет."
    cs_ls "Ты слишком рано отказываешься."
    cs_da "Я знаю тебя меньше часа."
    cs_ls "И уже научилась предсказывать мои идеи. Хороший результат."
    # cs_composition: regroup
    show mt normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show sl smile pioneer far at cs_actor_far_right
    # cs_composition: regroup
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя опять рассмеялась."
    cs_narrator "Ольга Дмитриевна устало посмотрела на всех нас."
    # cs_camp_emotion: text reaction
    show mt smile pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Хорошо. Форму вам найдём."
    cs_narrator "Я медленно повернулась к Дарье."
    cs_ls "Ну вот. Государственная машина приняла решение."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я начинаю понимать, почему у этой страны были проблемы."
    cs_narrator "Я бросила на неё выразительный взгляд."
    cs_ls "Осторожнее. Здесь такие высказывания могут вызвать дополнительный интерес к твоей биографии."
    cs_narrator "Ольга Дмитриевна нахмурилась."
    cs_mt "Что вы там обсуждаете?"
    cs_ls "Ничего особенного. Мы исключительно благонадёжные отдыхающие."
    cs_narrator "Дарья посмотрела на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты даже не знаешь, гражданкой какой страны сейчас являешься."
    cs_ls "Вопрос требует дополнительного исследования."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты пять минут назад не знала год."
    cs_ls "Именно поэтому исследование и требуется."
    cs_narrator "Ольга Дмитриевна тяжело вздохнула, подошла к шкафу и повернулась к Славе."
    cs_mt "Славя, сходи на склад. Принеси два комплекта формы. Размеры примерно подберёшь."
    cs_sl "Хорошо!"
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show cs_dasha_winter shrug far at cs_darya_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она развернулась и вышла."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["sl"])
    with cs_sprite_leave
    label cs_director_check_9074a78b49:
    # cs_director_end
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Ну вот."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining far at cs_darya_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Мы официально превращаемся в пионеров."
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed far at cs_darya_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нас никто никуда не принимал."
    cs_ls "Формальность."
    cs_narrator "Ольга Дмитриевна немедленно поправила:"
    # cs_camp_emotion: text reaction
    show mt normal pioneer far at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "В пионеры вас действительно никто не принимал."
    cs_ls "Значит, пионерская форма без лицензии."
    cs_mt "Какой ещё лицензии?"
    cs_ls "Не обращайте внимания. Профессиональная деформация."
    stop music fadeout 2.5
    cs_narrator "Я села на край кровати."
    $ renpy.music.set_volume(0.35, channel="sound")
    play sound cs_day_sfx_bed
    cs_narrator "Пружины тихо скрипнули."
    # cs_director_begin: Private reflection before the next topic
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_8b6ec3e77c:
    # cs_director_end
    cs_narrator "На минуту стало тихо, и я наконец смогла подумать. Передо мной — Ольга Дмитриевна, за окном — «Совёнок» и пионеры."
    cs_narrator "А в кармане — несколько сотен граммов технологий, которые здесь сошли бы за инопланетный артефакт."
    cs_th "Кстати, о технологиях…"
    return
