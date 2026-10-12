# -*- coding: utf-8 -*-
label cs_day01_57:
    $ save_name = "Чужая смена — День 1: Лишнее слово"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music cs_day_music_doubt fadeout 2.0 fadein 2.5
    cs_narrator "Я аккуратно поставила книгу обратно на полку."
    cs_narrator "Женя наблюдала за мной."
    cs_narrator "Кажется, её первоначальное раздражение постепенно уступало место любопытству."
    cs_narrator "Правда, любопытству весьма настороженному."
    show mz normal glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Значит, вы обе сегодня приехали?"
    cs_ls "Да."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И сразу решили идти в библиотеку?"
    cs_ls "Не сразу. До этого успели познакомиться с половиной лагеря."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "С половиной?"
    cs_narrator "Я задумалась."
    cs_ls "Возможно, немного преувеличила."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    cs_narrator "Дарья тихо улыбнулась."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И что, всё здесь настолько интересно?"
    cs_narrator "Я посмотрела на полки."
    cs_narrator "Потом на окна."
    cs_narrator "На стол."
    cs_narrator "На саму Женю."
    cs_th "Вот это вопрос."
    cs_narrator "Я могла бы сказать, что библиотека действительно представляет исторический интерес."
    cs_narrator "Что мне любопытна советская система каталогов."
    cs_narrator "Что хочется узнать, какие книги здесь читают."
    cs_narrator "Всё это было бы правдой."
    cs_narrator "Но существовала и другая причина."
    cs_narrator "Я хотела проверить, насколько знакомый мне мир совпадает с тем, который сейчас вижу перед собой."
    cs_narrator "И насколько его обитатели соответствуют образам из игры."
    cs_ls "Скорее непривычно видеть всё это не на экране."
    cs_narrator "Женя нахмурилась."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "На каком экране?"
    cs_narrator "Я замерла."
    cs_th "Прекрасно."
    cs_th "Соколова снова успешно раскрыла лишнюю информацию."
    cs_narrator "Дарья медленно повернулась ко мне."
    # cs_darya_variety: reaction
    show cs_darya shy_bend pioneer normal at cs_darya_normal_right
    cs_da "Лен…"
    cs_narrator "Я подняла ладонь."
    cs_ls "Да, я поняла."
    cs_narrator "Женя посмотрела на нас обеих."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Что поняла?"
    cs_ls "Что стоило выбрать другое выражение."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "А теперь объясни, какое имела в виду."
    cs_narrator "Я ненадолго закрыла глаза."
    cs_narrator "Вздохнула."
    cs_narrator "И посмотрела на неё."
    cs_ls "Хорошо."
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music cs_day_music_doubt fadeout 2.0 fadein 2.5
    cs_ls "Только сначала один вопрос."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Какой?"
    cs_ls "Если я расскажу что-то совершенно невероятное, ты хотя бы дослушаешь до конца?"
    # cs_darya_variety: reaction
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    cs_narrator "Она скрестила руки."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Если не будешь тянуть время."
    cs_narrator "Я кивнула."
    cs_ls "Справедливо."
    cs_narrator "Дарья посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    cs_da "Ты уверена?"
    cs_narrator "Я ответила не сразу."
    cs_ls "Нет."
    cs_narrator "Немного помолчала."
    cs_ls "Но теперь, кажется, всё равно придётся что-нибудь объяснить."
    return
