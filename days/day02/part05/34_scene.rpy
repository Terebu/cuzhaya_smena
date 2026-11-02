# -*- coding: utf-8 -*-
label cs_day02_34:
    $ save_name = "Чужая смена — День 2: Художественная самодеятельность"
    $ cs_part04_live = False
    $ cs_part05_live = True
    if not renpy.showing("cs_cg_poster_planning_day"):
        $ cs_director_scene("cs_cg_poster_planning_day")
        scene cs_cg_poster_planning_day
    $ cs_part05_cg = True
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
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
    $ cs_part05_cast = []
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() is None:
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    label cs_check_part05_s34:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Первую линию я провела вполне уверенно. Вторую — тоже. А вот на третьей внезапно вспомнила, что у бумаги существует одно крайне неприятное свойство. На ней нельзя нажать Ctrl+Z."
    cs_narrator "Я остановилась. Посмотрела на лист, потом на карандаш."
    cs_th "Прекрасно. Художник двадцать первого века столкнулся с технологическими ограничениями двадцатого."
    cs_narrator "Дарья, сидевшая справа, заметила моё выражение лица."
    cs_da "Что случилось?"
    cs_ls "Ничего серьёзного. Просто обнаружила отсутствие функции отмены последнего действия."
    cs_narrator "Она посмотрела на бумагу."
    cs_da "Ластик рядом."
    cs_narrator "Я перевела взгляд на небольшой белый прямоугольник возле карандашей."
    cs_ls "Благодарю, служба технической поддержки."
    cs_da "Обращайся."
    cs_narrator "Семён, до этого занимавшийся подбором карандашей, посмотрел на нас."
    cs_sy "Вы так говорите, будто рисование — какая-то сложная инженерная задача."
    cs_narrator "Я подняла голову."
    cs_ls "Товарищ Семён, любое творческое производство начинается с технического задания."
    cs_sy "У нас просто объявление."
    cs_ls "Вот именно. Поэтому требования особенно строгие."
    cs_narrator "Дарья усмехнулась."
    cs_da "Лена, нам нужно, чтобы люди смогли прочитать, где и когда будет выступление."
    cs_ls "Ты разбиваешь мои амбиции о суровую реальность."
    cs_da "Зато потом не придётся объяснять каждому отдельно."
    cs_narrator "Я задумалась."
    cs_th "Тоже верно."
    cs_narrator "В Москве у меня на компьютере были готовые кисти, шрифты, слои и возможность исправлять практически всё. Здесь — бумага. Несколько карандашей. Ластик."
    cs_narrator "И два человека, которые пока не особенно понимали, почему я уже пять минут размышляю над расположением заголовка."
    cs_th "А ведь в чём-то они правы. Объявление должно быть объявлением. Не обложкой художественного альбома."
    cs_narrator "Я придвинула лист ближе. Сделала лёгкую разметку. Наверху оставила место для крупного заголовка. По краям наметила небольшие изображения музыкальных нот."
    cs_narrator "Внизу — свободное пространство для информации о месте и времени. Семён наклонился."
    cs_sy "А что тут будет?"
    cs_narrator "Он указал на левую часть листа."
    cs_ls "Думаю, гитара."
    cs_sy "Почему?"
    cs_ls "Алиса, кажется, тоже собирается выступать. Логично показать инструмент."
    cs_da "Только не делай его слишком большим. Иначе для текста места не останется."
    cs_ls "Хорошо. У нас, кажется, сформировался полноценный художественный совет."
    cs_narrator "Семён усмехнулся."
    cs_sy "Кто председатель?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Бумага. Она здесь главная пострадавшая сторона."
    cs_narrator "Дарья рассмеялась. Я тоже улыбнулась. И вернулась к рисунку. Постепенно первоначальные линии начали складываться в понятную композицию."
    cs_narrator "Простую. Немного старомодную. Но довольно симпатичную."
    cs_th "Надо же. Оказывается, карандашами тоже можно работать. Кто бы мог подумать."
    return
