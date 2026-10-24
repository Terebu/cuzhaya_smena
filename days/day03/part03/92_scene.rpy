# -*- coding: utf-8 -*-
label cs_day03_92:
    $ save_name = "Чужая смена — День 3: За одним столом"
    $ cs_day03_mz_breakfast_together = cs_friend_mz >= 1
    if cs_day03_mz_breakfast_together:
        label cs_check_day03_92_together:
        pass
    if cs_friend_mz >= 2:
        cs_narrator "Женя окинула взглядом зал."
        cs_narrator "Потом указала на свободный стол у окна."
        cs_mz "Садитесь туда. Там спокойно."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Вместе?"
        cs_narrator "Она приподняла бровь."
        cs_mz "А я, по-твоему, с кем разговариваю?"
        cs_narrator "Я улыбнулась."
        cs_ls "Уточняю условия приглашения."
        cs_narrator "Женя вздохнула."
        cs_narrator "Но тоже улыбнулась."
        cs_mz "Соколова, просто садись."
        cs_narrator "Дарья тихо рассмеялась."
        cs_narrator "Мы устроились у окна."
        cs_narrator "Женя положила книгу на свободный край стола."
        cs_mz "Только предупреждаю: сначала я хочу нормально позавтракать."
        cs_narrator "Я кивнула."
        cs_ls "Поддерживаю."
        cs_narrator "Некоторое время мы действительно ели молча."
        cs_narrator "И в этой тишине не было ничего странного."
    elif cs_friend_mz == 1:
        cs_narrator "Женя направилась к столу у окна."
        cs_narrator "Я остановилась рядом."
        cs_ls "Можно мы с Дашей сядем здесь?"
        cs_narrator "Женя посмотрела на свободные места."
        cs_narrator "Немного подумала."
        cs_mz "Садитесь."
        cs_narrator "Я улыбнулась."
        cs_ls "Спасибо."
        cs_narrator "Дарья устроилась напротив."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя отложила книгу."
        cs_mz "Только давайте сначала поедим."
        cs_narrator "Я кивнула."
        cs_ls "Разумное предложение."
        cs_narrator "Она слегка улыбнулась."
    else:
        cs_narrator "Женя направилась к свободному столу возле окна."
        cs_narrator "Я не стала следовать за ней."
        cs_narrator "Она явно выбрала место, где можно спокойно позавтракать."
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        label cs_check_day03_92_separate:
        cs_narrator "Мы с Дарьей устроились за соседним столом."
        cs_da "Не хочешь сесть с Женей?"
        cs_narrator "Я слегка покачала головой."
        cs_ls "Пусть спокойно поест."
        cs_narrator "Дарья улыбнулась."
        cs_da "Хорошо."
        cs_narrator "Я взяла ложку."
        cs_th "Ничего страшного."
        cs_th "Мы ведь не обязаны проводить вместе каждый приём пищи."
    label cs_check_day03_92_result:
    return
