# -*- coding: utf-8 -*-
label cs_day03_153:
    $ save_name = "Чужая смена — День 3: До следующей главы"
    $ cs_director_scene("cs_house_lena_darya_ext_sunset")
    scene cs_house_lena_darya_ext_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5
    $ cs_day03_darya_destination = "dining_hall"
    cs_narrator "Мы вышли на крыльцо. Вечерний воздух оказался гораздо приятнее дневной жары. Я остановилась. Посмотрела на дорожку."
    cs_narrator "Потом на Дашу. Она всё ещё немного улыбалась."
    cs_ls "Что?"
    cs_narrator "Даша покачала головой."
    cs_da "Ничего."
    cs_narrator "Я прищурилась."
    cs_ls "Подозрительно."
    cs_narrator "Она рассмеялась."
    cs_da "Ты сегодня сама несколько раз так отвечала."
    cs_ls "Придётся признать, что у слова «ничего» появились слишком широкие полномочия."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша улыбнулась."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "Мы спустились с крыльца."
    if cs_da_day3_music_talk:
        cs_narrator "Даша немного помолчала. Потом сказала:"
        cs_da "Знаешь, я завтра, наверное, снова зайду к Мику."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Поиграть?"
        cs_narrator "Она кивнула."
        cs_da "Да. Если будет время."
        cs_ls "Хорошо. Мне кажется, тебе стоит продолжить."
        cs_narrator "Даша посмотрела на меня."
        cs_da "Ты правда так думаешь?"
        cs_ls "Да. Ты сегодня так рассказывала о музыке, что мне даже захотелось найти собственное пианино."
        cs_da "Ты же говорила, что не умеешь играть."
        cs_ls "Вот именно. Поэтому художественное оформление музыкальных мероприятий мне пока доверять безопаснее."
        cs_narrator "Она улыбнулась."
    elif cs_da_day3_shared_silence:
        cs_narrator "Даша посмотрела на меня."
        cs_da "Лен."
        cs_narrator "Я повернулась."
        cs_ls "Да?"
        cs_narrator "Она немного улыбнулась."
        cs_da "Давай как-нибудь ещё устроим такой спокойный вечер?"
        cs_ls "С книгами и без обязательной культурной программы?"
        cs_narrator "Она кивнула."
        cs_da "Именно."
        cs_ls "С удовольствием."
        cs_narrator "Даша улыбнулась чуть шире."
    cs_narrator "Мы пошли по дорожке. Впереди уже слышались голоса пионеров, направлявшихся на ужин. Я оглянулась на наш домик. В окне отражалось вечернее небо."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Странно. Ещё перед поездкой я даже не знала, что окажусь здесь. А теперь оставляю в этом домике недочитанную книгу, рисунки и вещи, которые уже кажутся своими. И рядом идёт человек, с которым мне не нужно постоянно притворяться интереснее, чем я есть."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на Дашу. Она заметила."
    cs_da "Что?"
    cs_ls "Думаю, сегодня получился хороший день."
    cs_narrator "Она кивнула."
    cs_da "Мне тоже понравилось."
    cs_narrator "Я посмотрела вперёд."
    cs_ls "Главное, чтобы на ужин не пришлось снова выполнять хозяйственные поручения."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша рассмеялась."
    cs_da "Почему?"
    cs_narrator "Я вздохнула."
    cs_ls "Потому что мой рабочий день уже закончился. Я требую соблюдения трудового законодательства."
    cs_narrator "Она покачала головой."
    cs_da "В пионерлагере?"
    cs_ls "Именно. Особенно в пионерлагере."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша улыбнулась."
    cs_da "Тогда пошли, товарищ трудящаяся."
    cs_narrator "Я торжественно выпрямилась."
    cs_ls "Есть, товарищ Еретикова."
    cs_narrator "Мы рассмеялись."
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "И направились к столовой. Сейчас я просто хотела поужинать."
    $ cs_day03_reading_book_location = "house_table"
    $ cs_day03_dinner_arrived = True
    return
