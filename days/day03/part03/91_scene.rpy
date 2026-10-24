# -*- coding: utf-8 -*-
label cs_day03_91:
    $ save_name = "Чужая смена — День 3: Завтрак без чрезвычайных происшествий"
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    show cs_darya shy_smile pioneer normal at Transform(xpos=0.75, xanchor=0.5, ypos=1.60, yanchor=1.0)
    show cs_zhenya normal pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0)
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/dining_hall_full.ogg" fadein 1.5
    $ renpy.music.set_volume(0.20, channel="ambience")
    $ renpy.music.set_volume(0.13, delay=1.5, channel="music")
    label cs_check_day03_91:
    cs_narrator "У раздачи уже выстроилась небольшая очередь."
    cs_narrator "Пахло кашей."
    cs_narrator "Свежим хлебом."
    cs_narrator "И чем-то ещё, что я пока не могла определить."
    cs_th "Так."
    cs_th "Сегодняшняя загадка дня: что именно нам приготовили на завтрак."
    cs_th "Учитывая вчерашний опыт, это пока значительно безопаснее исследования пространственной петли."
    cs_narrator "Мы взяли подносы."
    cs_narrator "Я старалась держать свой так, чтобы не задевать локтем край стойки."
    cs_narrator "Дарья это заметила."
    cs_narrator "Но ничего не сказала."
    cs_narrator "Просто чуть придержала мой поднос, когда я потянулась за стаканом."
    cs_narrator "Я благодарно улыбнулась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya thoughtful pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя посмотрела на повязку."
    cs_mz "Ты сегодня её уже меняла?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Хочу после завтрака зайти к Виоле, чтобы она посмотрела."
    cs_narrator "Женя кивнула."
    cs_mz "Хорошая мысль."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья усмехнулась."
    cs_da "Представляешь, она собирается пойти сама."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Удивительно, да? Человек добровольно выполняет медицинские рекомендации."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя слегка улыбнулась."
    cs_mz "После вчерашнего это действительно неожиданно."
    cs_narrator "Я вздохнула."
    cs_ls "У меня ощущение, что происшествие с корнем уже стало частью лагерного фольклора."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Ты сама всем рассказываешь."
    cs_narrator "Я задумалась."
    cs_ls "Справедливо. Пресс-служба сработала слишком эффективно."
    cs_narrator "Женя покачала головой."
    cs_narrator "Но улыбнулась."
    cs_narrator "Мы получили завтрак."
    cs_narrator "И отошли от раздачи."
    cs_narrator "Я посмотрела на тарелку."
    cs_th "Ну что ж."
    cs_th "Обычная каша."
    cs_th "И никаких интернетных мемов, связанных с её составом, в голове пока не обнаружено."
    cs_th "Хорошее начало дня."
    return
