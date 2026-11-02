# -*- coding: utf-8 -*-
label cs_day03_96:
    $ save_name = "Чужая смена — День 3: Приём по предварительной наглости"
    $ cs_director_scene("bg ext_dining_hall_away_day")
    scene bg ext_dining_hall_away_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    show cs_semen smile pioneer normal at cs_semen_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_96:
    label cs_check_day03_96_semen:
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    cs_narrator "Я проводила Женю взглядом. Она неторопливо шла в сторону библиотеки, придерживая книгу под мышкой. Когда её фигура скрылась за поворотом, я наконец позволила себе расслабиться."
    cs_th "Ну вот. Второй вполне культурный разговор за утро. Кажется, моё исправление происходит с пугающей скоростью. Нужно срочно предпринять меры, пока меня не назначили образцовой пионеркой."
    cs_narrator "Дарья заметила мою улыбку."
    cs_da "Даже спрашивать боюсь, о чём ты сейчас думаешь."
    cs_narrator "Я повернулась к ней."
    cs_ls "А зря. Мысли исключительно светлые."
    cs_da "Именно это и настораживает."
    cs_narrator "Семён, который стоял неподалёку, заинтересованно посмотрел на нас."
    cs_sy "Что опять?"
    cs_narrator "Я поправила галстук. Выпрямилась. И посмотрела куда-то в сторону медпункта."
    cs_ls "Сегодня мне предстоит встреча с одной из самых обаятельных женщин этого лагеря."
    if renpy.showing("cs_darya"):
        show cs_darya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья закрыла глаза."
    cs_da "Лена…"
    cs_narrator "Семён посмотрел на меня. Потом в сторону медпункта."
    cs_sy "К Виоле, что ли?"
    cs_narrator "Я медленно кивнула."
    cs_ls "Прекрасная дедукция, товарищ Семён. Следствие установило личность за считаные секунды."
    if renpy.showing("cs_semen"):
        show cs_semen awkward pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он вздохнул."
    cs_sy "Ты же идёшь туда из-за руки?"
    cs_narrator "Я посмотрела на повязку."
    cs_ls "Не разрушай атмосферу. Я пыталась придать обычной перевязке немного светского лоска."
    cs_narrator "Дарья усмехнулась."
    cs_da "Особенно после вчерашнего падения."
    cs_ls "Вот. Даже ближайшее окружение выступает против художественной подачи материала."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён рассмеялся. Я повернулась к нему."
    cs_ls "Кстати, Семён. Если тоже соберёшься к Виоле, предупреждаю: сегодня я первая."
    cs_narrator "Он остановился."
    cs_sy "С чего ты вообще взяла, что я собираюсь?"
    cs_narrator "Я невинно улыбнулась."
    cs_ls "Предусмотрительность. Вдруг у нас внезапно возникнет очередь."
    cs_sy "У меня с утра вообще-то другие дела."
    cs_ls "Какие?"
    cs_narrator "Он посмотрел на меня с подозрением."
    cs_sy "А тебе зачем?"
    cs_ls "Собираю статистику занятости населения."
    cs_sy "Соколова, иди уже к своему врачу."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_ls "Вот это отношение. Человек интересуется общественной жизнью, а его отправляют лечиться."
    cs_sy "У тебя, между прочим, для этого есть уважительная причина."
    cs_narrator "Я посмотрела на локоть."
    cs_th "Возразить нечего. Опять."
    cs_ls "Ладно. Признаю, замечание обоснованное."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён усмехнулся."
    cs_sy "Ничего себе. Ты сегодня согласилась со мной."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Видишь? Стоит один раз проявить здравый смысл, как окружающие уже готовы созвать комиссию."
    cs_narrator "Она покачала головой. Но улыбалась. Семён поправил галстук."
    cs_sy "Ладно, я к клубам. Увидимся позже."
    cs_ls "Договорились."
    cs_narrator "Я выдержала паузу. Потом добавила:"
    cs_ls "И если передумаешь насчёт Виолы…"
    cs_sy "Лена!"
    cs_ls "Всё. Молчу."
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_check_day03_96_semen_left:
    cs_narrator "Он покачал головой и направился по дорожке. Дарья посмотрела ему вслед, затем на меня."
    cs_da "Ты понимаешь, что специально его провоцируешь?"
    cs_ls "Разумеется."
    cs_narrator "Она приподняла бровь."
    cs_da "И зачем?"
    cs_ls "Он забавно отвечает. К тому же за эти два дня вполне научился давать сдачи."
    cs_narrator "Дарья усмехнулась."
    cs_da "А когда-нибудь ему надоест."
    cs_narrator "Я помолчала. Потом кивнула."
    cs_ls "Тогда перестану."
    cs_narrator "Она посмотрела на меня с удивлением."
    cs_da "Правда?"
    cs_ls "Ну да. Я же не ставлю целью довести человека до белого каления."
    cs_narrator "Пауза."
    cs_ls "Обычно это просто побочный эффект."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась. И мы направились к медпункту."
    return
