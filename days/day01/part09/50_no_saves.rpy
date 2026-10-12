# -*- coding: utf-8 -*-
label cs_day01_50:
    $ save_name = "Чужая смена — День 1: Никаких сохранений"
    scene cs_camp_path_sunset
    # cs_focus_suppressed: show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.14,delay=2.0,channel="music")
    # cs_focus: camera
    hide cs_darya with Dissolve(0.25)
    cs_narrator "Мы вышли на более широкую дорожку."
    cs_narrator "Отсюда открывался вид на деревья и несколько домиков, освещённых вечерним солнцем."
    cs_narrator "Я ненадолго остановилась."
    cs_narrator "Посмотрела назад."
    cs_narrator "Где-то там остались библиотека, клубы, площадь и столовая."
    cs_narrator "Места, которые ещё вчера существовали для меня исключительно внутри компьютерной игры."
    cs_narrator "И люди, которых я знала только по их нарисованным изображениям."
    cs_narrator "Теперь всё это было настоящим."
    cs_narrator "Во всяком случае, достаточно настоящим, чтобы я чувствовала под ногами землю и усталость после целого дня прогулок."
    label cs_check_day01_part09_introspection:
    cs_th "И никаких сохранений."
    cs_th "Нельзя вернуться на пять минут назад и выбрать другую реплику."
    cs_th "Нельзя перемотать разговор, если сказала что-то не то."
    cs_th "И совершенно непонятно, что случится, если допустить серьёзную ошибку."
    cs_narrator "Я медленно вдохнула."
    cs_narrator "Дарья заметила моё выражение лица."
    label cs_check_day01_part09_returns:
    # cs_darya_variety: reaction
    # cs_focus_suppressed: show cs_darya thinking pioneer normal at cs_darya_normal_center
    # cs_focus: camera
    show cs_darya thinking pioneer normal at cs_darya_normal_center with Dissolve(0.25)
    cs_da "Ты опять задумалась?"
    cs_ls "Немного."
    cs_da "О чём?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "О том, что здесь нельзя сохраняться."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    cs_narrator "Она улыбнулась."
    cs_da "Как в игре?"
    cs_ls "Угу."
    cs_da "Но в обычной жизни тоже нельзя."
    cs_narrator "Я ненадолго замолчала."
    cs_narrator "Потом кивнула."
    cs_ls "Верно."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_da "Лен, ты ведь не обязана всё время знать, как правильно поступить."
    cs_narrator "Я повернулась к ней."
    cs_narrator "Пауза."
    cs_ls "Это прозвучало подозрительно разумно."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    cs_narrator "Дарья рассмеялась."
    cs_da "Я старалась."
    cs_narrator "Я тоже улыбнулась."
    cs_ls "Спасибо."
    # cs_focus: camera
    hide cs_darya with Dissolve(0.25)
    cs_narrator "Она кивнула."
    cs_narrator "Мы снова пошли."
    cs_narrator "А я вдруг подумала, что, возможно, именно в этом и заключается самая большая разница между игрой и происходящим."
    cs_narrator "В игре я выбирала ответы, заранее надеясь получить определённый результат."
    cs_narrator "Здесь же предстояло разговаривать с людьми, не зная, что будет дальше."
    cs_narrator "И принимать последствия собственных решений."
    cs_narrator "Даже самых незначительных."
    return
