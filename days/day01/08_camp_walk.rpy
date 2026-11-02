# -*- coding: utf-8 -*-
# Source: source/day01_part02.md.
label cs_day01_08:
    $ save_name = u"Чужая смена — День 1: Территория лагеря"
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    with Dissolve(1.5)
    window show dissolve
    $ renpy.music.set_volume(0.55, delay=1.0, channel="music")
    play music cs_day_music_daily fadeout 2.0 fadein 3.0
    $ renpy.music.set_volume(0.55, delay=1.5, channel="ambience")
    play ambience cs_day_camp_center fadeout 1.0 fadein 2.0
    label cs_check_day01_walk:
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы прошли через ворота."
    # cs_director_begin: REFLECTIVE_SHOT: Living camp panorama
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_4a3e545105:
    # cs_director_end
    cs_narrator "Пока мы стояли у ворот, лагерь ещё можно было принять за декорацию или убедительный сон. Здесь это стало труднее."
    cs_narrator "Свет пробивался сквозь листья, пахло нагретой древесиной. Издалека доносились голоса; в одном из зданий хлопнула дверь."
    cs_narrator "На дорожке лежали мелкие камешки."
    cs_narrator "Я провела подошвой по асфальту. Шероховатый, самый обычный."
    # cs_director_begin: Return to direct interaction: Living camp panorama
    $ cs_frame_focus(["sl", "cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_9a119efd1d:
    # cs_director_end
    cs_narrator "Дарья заметила моё движение."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Проверяешь?"
    cs_ls "Угу."
    cs_da "И как?"
    cs_ls "Пока мир успешно проходит тест на существование."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она чуть улыбнулась."
    show sl normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_dasha_winter smile normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя обернулась."
    cs_sl "Вы что-то сказали?"
    cs_ls "Нет, всё хорошо."
    cs_narrator "Я ускорила шаг."
    # cs_director_begin: REFLECTIVE_SHOT: Map remembered as real space
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_a51ccf619e:
    # cs_director_end
    cs_narrator "Я знала эти места: вот дорожка, там площадь, дальше столовая, клубы, домики, медпункт, библиотека."
    cs_narrator "Но знание карты не помогало принять то, что сейчас я по ней иду."
    # cs_director_begin: Return to direct interaction: Map remembered as real space
    $ cs_frame_focus(["sl", "cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_f4a4f32b11:
    # cs_director_end
    cs_narrator "Я приблизилась к Дарье."
    cs_ls "Знаешь, это очень странное чувство."
    # cs_darya_variety: reaction
    show cs_dasha_winter thinking normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какое?"
    cs_ls "Когда знаешь место, в котором никогда не была."
    cs_narrator "Она посмотрела вперёд."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Как дежавю?"
    cs_narrator "Хорошее слово. Только обычно дежавю длится секунду, а не всю дорогу от ворот."
    cs_ls "Да. Примерно так."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья слегка усмехнулась."
    cs_da "Тогда держись рядом. Вдруг пройдёт."
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show cs_dasha_winter smile normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Некоторое время мы шли молча."
    cs_ls "Хорошо хоть, одна из нас видит всё это впервые."
    # cs_darya_stage: present in story
    show cs_dasha_winter worried normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не уверена, что это преимущество."
    cs_ls "Сейчас проверим."
    cs_narrator "Славя спокойно шагала впереди. Для неё это, вероятно, обычный летний день: странные девушки, непонятный автобус, нелепые объяснения."
    cs_th "Ничего особенного. Рядовая смена в пионерском лагере."
    cs_narrator "Я едва заметно покачала головой."
    return
