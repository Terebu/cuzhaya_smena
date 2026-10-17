# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_19:
    $ save_name = u"Чужая смена — День 1: Столовая"
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_everyday fadeout 1.5 fadein 2.5
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.0 fadein 2.0
    show mt normal pioneer at cs_actor_left
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Через несколько минут впереди показалась столовая."
    cs_narrator "Я узнала её мгновенно."
    cs_ls "Вот она."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Столовая?"
    cs_ls "Угу."
    cs_narrator "Ольга Дмитриевна обернулась."
    cs_mt "Конечно столовая. А что ты ожидала увидеть?"
    cs_ls "Уже ничего."
    cs_narrator "Я посмотрела на знакомый фасад."
    cs_ls "Именно это и настораживает."
    cs_narrator "Ольга Дмитриевна решила не уточнять."
    cs_narrator "Возле входа толпились пионеры."
    cs_narrator "Голоса."
    cs_narrator "Смех."
    cs_narrator "Запах еды."
    cs_narrator "До меня вдруг дошло, что я действительно проголодалась."
    cs_ls "Надеюсь, кормят здесь так же неплохо, как я помню."
    cs_da "Ты знаешь даже меню?"
    cs_ls "Не настолько у меня хорошая память."
    cs_narrator "Пауза."
    cs_ls "Хотя некоторые блюда действительно помню."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Разумеется."
    cs_narrator "Мы поднялись по ступенькам."
    cs_narrator "И тут я заметила знакомую рыжую макушку."
    # cs_presence_keep: hide mt
    # cs_composition: regroup
    show dv normal pioneer far at cs_actor_left
    # cs_composition: regroup
    # cs_darya_stage: present in story
    show cs_darya smile pioneer far at cs_darya_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_th "Алиса."
    # cs_director_begin: Focus on the girls outside the canteen
    $ cs_frame_focus(["dv", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_5d95593d1c:
    # cs_director_end
    cs_narrator "Она стояла возле стены и о чём-то разговаривала с девочкой заметно ниже ростом."
    cs_narrator "Рядом — Ульяна."
    # cs_composition: regroup
    show dv normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show us smile pioneer far at cs_actor_far_right
    # cs_composition: regroup
    show cs_darya smile pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_part04_cameo:
    cs_narrator "Немного дальше прошла Славя."
    cs_narrator "Где-то у входа мелькнули голубые волосы."
    cs_narrator "Я невольно замедлила шаг."
    cs_ls "О."
    cs_narrator "Дарья проследила за моим взглядом."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Опять знакомые персонажи?"
    cs_ls "Ага."
    cs_narrator "Я едва заметно кивнула в сторону девушек."
    cs_ls "Рыжая — Алиса. Рядом Ульяна."
    cs_da "Ты сейчас опять подойдёшь и назовёшь их по именам?"
    cs_ls "Нет."
    cs_da "Почему?"
    cs_ls "Дважды было забавно. На третий раз меня начнут официально допрашивать."
    # cs_camp_emotion: text reaction
    show dv surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "И тут Алиса сама повернулась в нашу сторону."
    cs_narrator "Наши взгляды встретились."
    cs_narrator "Она оценила мои фиолетовые волосы."
    cs_narrator "Затем алые волосы Дарьи."
    cs_narrator "Пионерскую форму."
    cs_narrator "И снова наши лица."
    # cs_camp_emotion: text reaction
    show dv grin pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "С явным интересом что-то сказала Ульяне."
    # cs_camp_emotion: text reaction
    show us grin pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_camp_cameo_reactions:
    cs_narrator "Та моментально обернулась."
    show dv normal pioneer far at cs_actor_far_left
    show us smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Всё. Местная разведка нас заметила."
    cs_narrator "Дарья посмотрела на девушек."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Они кажутся обычными."
    cs_ls "Вот это пока и беспокоит."
    # cs_director_begin: Return to the counsellor calling the newcomers
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_366768875a:
    # cs_director_end
    cs_mt "Девочки! В столовую, обедать!"
    # cs_presence_keep: hide dv
    # cs_composition: regroup
    # cs_presence_keep: hide us
    # cs_composition: regroup
    # cs_presence_keep: hide mt
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Мы вошли внутрь."
    return
