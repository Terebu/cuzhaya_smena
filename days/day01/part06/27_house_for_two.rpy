# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_27:
    $ save_name = "Чужая смена — День 1: Домик"
    scene cs_house_lena_darya_ext_day
    show sl smile pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    with Dissolve(1.3)
    label cs_check_day01_part06_house_ext:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.5 fadein 2.0
    cs_narrator "Славя остановилась перед небольшим домиком."
    cs_sl "Вот и пришли!"
    cs_narrator "Я подняла взгляд."
    cs_narrator "Деревянные стены."
    cs_narrator "Небольшое крыльцо."
    cs_narrator "Два окна."
    cs_narrator "Ничего необычного."
    cs_narrator "И всё же мысль о том, что здесь нам предстоит провести ближайшую ночь, вызвала какое-то странное чувство."
    cs_th "Новая квартира."
    cs_th "Условия предоставления — временная аномалия."
    cs_th "Срок проживания неизвестен."
    cs_da "Симпатично."
    cs_narrator "Я кивнула."
    cs_ls "Есть такое."
    cs_narrator "Славя поднялась на крыльцо и открыла дверь."
    cs_sl "Проходите."
    $ renpy.music.set_volume(0.45,channel="sound")
    play sound cs_day_sfx_door
    scene cs_house_lena_darya_int_day
    show sl normal pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    with Dissolve(1.4)
    label cs_check_day01_part06_house_int:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_cabin:
        play ambience cs_day_cabin fadeout 1.5 fadein 2.0
    stop music fadeout 2.0
    cs_narrator "Мы вошли."
    cs_narrator "Внутри оказалось довольно уютно."
    cs_narrator "Две кровати."
    cs_narrator "Небольшой стол."
    cs_narrator "Шкаф."
    cs_narrator "Тумбочки."
    cs_narrator "Занавески на окнах."
    cs_narrator "Сквозь стекло пробивались солнечные лучи, ложась светлыми прямоугольниками на деревянный пол."
    cs_narrator "Я огляделась."
    cs_narrator "Никакого компьютера."
    cs_narrator "Никакого холодильника."
    cs_narrator "Никакой розетки возле кровати, в которую можно было бы по привычке воткнуть телефон."
    cs_th "Минимализм."
    cs_th "Причём радикальный."
    cs_narrator "Славя показала на шкаф."
    show sl smile pioneer at cs_actor_left
    cs_sl "Здесь можно хранить вещи. Постельное бельё уже должно быть приготовлено."
    cs_narrator "Дарья подошла к одной из кроватей."
    cs_narrator "Осторожно коснулась покрывала."
    cs_da "Выглядит неплохо."
    cs_narrator "Я посмотрела на вторую кровать."
    cs_ls "Проверим соответствие заявленным характеристикам."
    cs_narrator "Села на край."
    cs_narrator "Пружины негромко скрипнули."
    $ renpy.music.set_volume(0.45,channel="sound")
    play sound cs_day_sfx_bed
    cs_narrator "Я чуть покачалась."
    cs_ls "Конструкция функционирует."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    cs_narrator "Дарья улыбнулась."
    show sl laugh pioneer at cs_actor_left
    cs_narrator "Славя не удержалась от смеха."
    show sl smile pioneer at cs_actor_left
    cs_sl "Вы забавные."
    cs_ls "Спасибо. Хотя пока не уверена, что это официальная характеристика."
    cs_narrator "Славя объяснила, где находятся умывальники и какие правила действуют в лагере."
    cs_narrator "Я старалась слушать внимательно."
    cs_narrator "Не потому, что ничего этого не знала."
    cs_narrator "Просто было бы глупо полагаться исключительно на воспоминания о компьютерной игре."
    cs_sl "Если что-нибудь понадобится, обращайтесь ко мне или к Ольге Дмитриевне."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_da "Хорошо. Спасибо тебе."
    cs_narrator "Я тоже кивнула."
    cs_ls "Правда, спасибо. Ты нам очень помогла."
    cs_narrator "Славя улыбнулась ещё шире."
    cs_sl "Не за что!"
    cs_narrator "Она направилась к двери."
    cs_sl "Тогда я побегу. У меня ещё дела!"
    cs_da "Увидимся."
    cs_ls "Пока, Славя."
    cs_narrator "Дверь закрылась."
    hide sl with Dissolve(0.5)
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_narrator "Мы остались вдвоём."
    pause 1.0
    cs_narrator "Некоторое время никто ничего не говорил."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она посмотрела на меня."
    cs_ls "Ну что."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Что?"
    cs_ls "Кажется, у нас теперь есть недвижимость."
    show cs_darya amused pioneer normal at cs_darya_normal_center
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Временная."
    cs_ls "Уточнение принято."
    return
