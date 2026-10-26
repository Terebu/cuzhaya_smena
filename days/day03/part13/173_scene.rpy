# -*- coding: utf-8 -*-
label cs_day03_173:
    $ save_name = "Чужая смена — День 3: Честный финал"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    if cs_friend_mz >= 1:
        cs_narrator "Женя отложила карандаш."
        cs_narrator "Подошла ближе к моему столу."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "А что тебе в итоге не понравилось?"
        cs_narrator "Я немного подумала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Если честно, мне стало грустно за Александра."
        cs_narrator "Она приподняла бровь."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Почему?"
        cs_narrator "Я посмотрела на закрытую книгу."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Он получил почти всё, чего можно добиться с его новыми взглядами."
        cs_narrator "Немного помолчала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Но мне кажется, тот человек, который приехал в Петербург в начале истории, вряд ли обрадовался бы подобному будущему."
        cs_narrator "Женя задумалась."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya thoughtful pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "А если бы он остался прежним?"
        cs_narrator "Я посмотрела на неё."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Всё таким же наивным, уверенным в своих мечтах. Было бы лучше?"
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Вот в этом и проблема. Не знаю."
        cs_narrator "Она кивнула."
        cs_narrator "Я продолжила:"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Мне не кажется, что он должен был остаться прежним. Просто не обязательно было превращаться в точную противоположность себе."
        cs_narrator "Женя немного помолчала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Ты считаешь, можно было найти середину?"
        cs_narrator "Я пожала плечами."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Хотелось бы верить."
        cs_narrator "Она слегка улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Мне тоже."
        cs_narrator "Я удивлённо подняла бровь."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Ого. Мы сошлись во мнениях."
        cs_narrator "Женя усмехнулась."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Не привыкай."
        cs_narrator "Я рассмеялась."
        cs_narrator "Потом снова посмотрела на книгу."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "А ещё мне нравится, что конец не пытается всех срочно осчастливить."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Тебе не нравятся счастливые концовки?"
        cs_narrator "Я покачала головой."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Нравятся. Очень."
        cs_narrator "Посмотрела на неё."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Просто счастливый конец должен быть заслуженным. Если персонажи полкниги делали глупости, а в последнем абзаце внезапно всё стало идеально, я чувствую себя немного обманутой."
        cs_narrator "Женя улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "А здесь?"
        cs_narrator "Я задумалась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Здесь никто не приходит и не объясняет героям, как им теперь правильно жить."
        cs_narrator "Пауза."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Они просто остаются с тем, что сделали."
        cs_narrator "Женя кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_mz "Поэтому я и дала тебе эту книгу."
        else:
            cs_mz "Значит, ты сама нашла подходящую книгу."
        cs_narrator "Я подняла глаза."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_ls "Специально?"
        else:
            cs_ls "Значит, не зря сняла её с полки?"
        cs_narrator "Она слегка пожала плечами."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_mz "Ты говорила, что любишь истории, где решения имеют последствия."
        else:
            cs_mz "Ты хорошо объяснила, почему тебе интересна эта история."
        cs_narrator "Я посмотрела на неё."
        cs_th "Надо же."
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_th "Она действительно всё запомнила."
        else:
            cs_th "Она действительно слушала, что я говорю."
    else:
        cs_mz "Хорошо, что книга тебе подошла. А теперь давай её запишем — пора закрывать."
        cs_ls "Конечно. Спасибо, что дала закончить."
    if cs_mz_day3_honest_book_talk:
        cs_narrator "Женя немного улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "После нашего сегодняшнего разговора я примерно представляла, на что ты обратишь внимание."
        cs_narrator "Я прищурилась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "То есть это был литературный эксперимент?"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Можно и так сказать."
        cs_narrator "Я медленно кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "И как результат?"
        cs_narrator "Она задумалась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Интереснее, чем я ожидала."
        cs_narrator "Я приложила здоровую руку к груди."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Высшая похвала от товарища библиотекаря."
        cs_narrator "Женя фыркнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Соколова, не порть момент."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Не буду."
        $ cs_mz_day3_final_discussion = True
    elif cs_friend_mz >= 2:
        cs_narrator "Женя посмотрела на книгу."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_mz "Значит, я не ошиблась с выбором."
        else:
            cs_mz "Значит, ты не ошиблась с выбором."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Не ошиблась."
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Хорошо."
    else:
        cs_narrator "Женя посмотрела на часы."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Рада, что понравилось. Но нам уже пора заканчивать."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Конечно. Извини, что задержала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Ничего страшного. Просто завтра снова рано вставать."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Понимаю."
    cs_narrator "Я ещё раз посмотрела на книгу."
    cs_th "«Обыкновенная история»."
    cs_th "Какое подходящее название для совершенно необычного вечера."
    cs_narrator "Потом встала."
    cs_narrator "Взяла роман."
    cs_narrator "И отнесла к рабочему столу Жени."
    return
