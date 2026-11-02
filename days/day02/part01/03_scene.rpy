# -*- coding: utf-8 -*-
label cs_day02_03:
    $ save_name = "Чужая смена — День 2: «Совёнок» без пионеров"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day at cs_early_morning
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/feeling_good.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_s03:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Снаружи меня встретили пустые дорожки, роса и прохладный воздух. Ни Алисы с Ульяной, ни Слави с поручениями, ни Ольги Дмитриевны. Даже Семён, похоже, ещё спал."
    cs_th "«Совёнок» без населения. Редкая возможность спокойно осмотреть декорации."
    cs_narrator "Я остановилась на крыльце и глубоко вдохнула. Трава, влажная земля, сосны."
    cs_th "Москва, конечно, прекрасный город. Но в вопросах утренней тишины у неё серьёзная конкуренция."
    cs_narrator "Сошла с крыльца, размяла плечи, колени и голеностоп. Сделала несколько приседаний и наклонов."
    cs_th "Ну что, Соколова. Проверим качество местной дорожной инфраструктуры."
    cs_narrator "Я побежала, привыкая к неровной дорожке. После росы корни и камни оставались скользкими, поэтому спешить не стоило. И неожиданно поняла, насколько мне этого не хватало."
    cs_narrator "Вчера весь день приходилось думать: куда мы попали, почему сюда, кому здесь можно верить. А на бегу думать не нужно. Вдох, выдох, следующий шаг — только дорога под ногами."
    cs_th "Вот за что я люблю бег. Хотя бы полчаса можно не пытаться понять устройство мироздания."
    return
