# -*- coding: utf-8 -*-
label cs_day03_139:
    $ save_name = "Чужая смена — День 3: Не только шутки"
    $ renpy.music.set_volume(0.06,delay=1.0,channel="music")
    cs_narrator "Мы немного помолчали."
    cs_narrator "Неподалёку прошли двое пионеров."
    cs_narrator "С площади донёсся чей-то смех."
    cs_narrator "Я смотрела на книгу."
    cs_narrator "Семён разглядывал дорожку."
    cs_narrator "Дарья сидела рядом и, кажется, с удовольствием пользовалась редкой возможностью ничего не говорить."
    cs_narrator "Забавно."
    cs_narrator "Мы ведь все оказались здесь не по собственной воле."
    cs_narrator "Но почему-то только сейчас начинаем общаться так, будто знакомы достаточно давно."
    cs_narrator "Семён посмотрел на меня."
    cs_sy "Слушай, Лена."
    cs_narrator "Я подняла голову."
    cs_ls "Да?"
    cs_sy "А тебе здесь вообще нормально?"
    cs_narrator "Я немного удивилась."
    cs_ls "В каком смысле?"
    cs_narrator "Он пожал плечами."
    cs_sy "Ну… ты уже со всеми познакомилась. То в библиотеке сидишь, то у Мику, то Славе помогаешь."
    cs_narrator "Я кивнула."
    cs_narrator "Он немного помолчал."
    cs_sy "Со стороны кажется, будто ты здесь всю жизнь провела."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Потом на Дарью."
    cs_narrator "А вот это уже неожиданно."
    cs_ls "Не сказала бы."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён усмехнулся."
    cs_sy "А выглядишь именно так."
    cs_narrator "Я задумалась."
    cs_ls "Наверное, просто пытаюсь чем-то заниматься."
    cs_sy "Чтобы не думать о том, почему мы здесь?"
    cs_narrator "Я посмотрела на него внимательнее."
    cs_narrator "На площади неподалёку ещё оставались пионеры."
    cs_narrator "Поэтому ответила осторожно."
    cs_ls "Отчасти."
    cs_narrator "Он кивнул."
    cs_da "Мы всё равно об этом думаем. Просто не постоянно."
    cs_narrator "Семён посмотрел на неё."
    cs_sy "Понимаю."
    cs_narrator "Я немного помолчала."
    cs_ls "А у тебя как?"
    cs_narrator "Он посмотрел в сторону деревьев."
    cs_sy "По-разному."
    cs_narrator "Пауза."
    cs_sy "Иногда кажется, что уже привык. А потом вспоминаю, как вообще сюда попал, и всё снова становится странным."
    cs_narrator "Я кивнула."
    cs_narrator "Да."
    cs_narrator "Очень знакомое ощущение."
    cs_narrator "Он посмотрел на нас."
    cs_sy "Вы хотя бы вдвоём."
    cs_narrator "Дарья чуть повернулась."
    cs_da "Это помогает."
    cs_narrator "Я кивнула."
    cs_ls "Очень."
    cs_narrator "Немного подумала."
    cs_ls "Но ты ведь тоже не совсем один."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён усмехнулся."
    cs_sy "Если ты сейчас предложишь мне официально вступить в вашу компанию, я начну подозревать очередной розыгрыш."
    cs_narrator "Я улыбнулась."
    cs_ls "А вот и нет."
    cs_narrator "Он посмотрел на меня."
    cs_ls "Просто говорю, что мы знакомы. И можем нормально проводить время вместе."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Даже без Лениных представлений."
    cs_narrator "Я повернулась к ней."
    cs_ls "Прошу уточнить: мои представления отличаются высоким художественным уровнем."
    if renpy.showing("cs_semen"):
        show cs_semen relaxed pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    cs_sy "Особенно когда ты начинаешь театрально вздыхать."
    cs_narrator "Я задумалась."
    cs_ls "Между прочим, это сложная актёрская работа."
    if renpy.showing("cs_darya"):
        show cs_darya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья покачала головой."
    cs_narrator "Но улыбалась."
    cs_narrator "Семён снова посмотрел на площадь."
    cs_narrator "Немного помолчал."
    cs_narrator "И вдруг сказал:"
    cs_sy "Всё-таки с вами веселее."
    cs_narrator "Я повернулась к нему."
    cs_narrator "Надо же."
    cs_narrator "Кажется, от товарища Семёна поступило официальное признание."
    cs_narrator "Я улыбнулась."
    cs_narrator "Но на этот раз обошлась без торжественных речей."
    cs_ls "Мне тоже."
    cs_narrator "Он кивнул."
    cs_narrator "И какое-то время мы просто сидели вместе."
    return
