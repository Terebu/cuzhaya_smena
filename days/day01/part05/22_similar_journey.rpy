# -*- coding: utf-8 -*-
# Source: source/day01_part05.md.
label cs_day01_22:
    $ save_name = "Чужая смена — День 1: Похожая дорога"
    $ renpy.music.set_volume(0.35,delay=1.0,channel="music")
    play music cs_day_music_home fadeout 1.5 fadein 2.5
    label cs_check_day01_part05_journey:
    cs_narrator "Я поставила стакан компота подальше от края."
    cs_narrator "Семён к еде пока не притронулся."
    show cs_semen awkward_alt pioneer normal at cs_semen_normal_right
    cs_sy "Я сел в четыреста десятый. В обычный городской автобус. Дальше… не помню."
    show cs_darya thinking pioneer normal at cs_darya_normal_left
    cs_da "Заснул?"
    show cs_semen tie_touch pioneer normal at cs_semen_normal_right
    cs_sy "Похоже. Проснулся уже здесь. Жара, лес, этот лагерь."
    cs_narrator "Я кивнула."
    cs_ls "У нас практически то же самое. Только автобус был современный. А проснулись мы в старом «Икарусе»."
    cs_narrator "Семён перевёл взгляд на Дарью."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_right
    cs_sy "Ты тоже это помнишь?"
    show cs_darya explaining pioneer normal at cs_darya_normal_left
    cs_da "Помню, как села. Помню разговор с Леной. Потом начала засыпать. А дальше — солнце в окно и совсем другой салон."
    cs_narrator "Она слегка сжала пальцы на краю подноса."
    show cs_darya shrug pioneer normal at cs_darya_normal_left
    cs_da "И зимой я точно не была одета в пионерскую форму."
    cs_ls "Форму нам выдали уже здесь. До этого мы ходили по лагерю в куртках."
    cs_narrator "Семён наконец взял ложку."
    cs_narrator "Но сразу положил обратно."
    show cs_semen tie_touch pioneer normal at cs_semen_normal_right
    cs_sy "Вчера я подумал, что сплю."
    show cs_darya worried pioneer normal at cs_darya_normal_left
    cs_da "Мы тоже."
    cs_sy "Теперь так не кажется."
    cs_narrator "Я посмотрела на тарелку."
    cs_narrator "От еды поднимался самый обычный пар."
    cs_ls "Предлагаю пока исходить из того, что происходящее настоящее. Хотя бы потому, что от него можно получить настоящий солнечный удар."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_left
    cs_narrator "Дарья коротко усмехнулась."
    cs_narrator "Семён — нет."
    cs_sy "Ты всё время говоришь так спокойно."
    cs_narrator "Я подняла глаза."
    cs_ls "Не путай спокойный голос с отсутствием вопросов."
    cs_narrator "Он кивнул."
    cs_narrator "Я решила не добавлять, что с отсутствием страха его тоже путать не стоило."
    show cs_darya shrug pioneer normal at cs_darya_normal_left
    cs_da "Автобус. Сон. Пробуждение в лагере. Это совпадает у всех троих."
    cs_ls "И пока ни у кого нет объяснения, что случилось между вторым и третьим пунктом."
    cs_sy "Мне сказали, что автобус обычно приезжает по расписанию."
    cs_ls "Нам тоже. Но наш водитель куда-то исчез."
    cs_da "Мы не видели, как он вышел. Когда пошли смотреть, его уже не было."
    cs_narrator "Я чуть повернулась к ней."
    cs_ls "Да. Именно так. Не будем делать из этого больше, чем знаем."
    cs_narrator "Семён посмотрел на пустой проход между столами."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_right
    cs_sy "А если нас привезли специально?"
    cs_ls "Возможность есть. Доказательств пока нет."
    cs_da "И неизвестно, кто мог бы это сделать."
    cs_narrator "Повисла короткая пауза."
    cs_narrator "Потом я всё-таки взяла ложку."
    cs_th "Расследование расследованием."
    cs_th "А обед лучше съесть, пока он ещё тёплый."
    return
