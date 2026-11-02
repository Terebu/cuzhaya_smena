# -*- coding: utf-8 -*-
label cs_day01_55_a:
    $ save_name = "Чужая смена — День 1: Помощь библиотекарю"
    show cs_zhenya normal pioneer normal at cs_darya_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на книги возле стола."
    cs_ls "Слушай, тебе помочь?"
    cs_narrator "Женя подняла глаза."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "С чем?"
    cs_narrator "Я указала на стопку."
    cs_ls "С книгами. Судя по всему, их нужно разобрать."
    cs_narrator "Женя немного помолчала."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А ты умеешь?"
    cs_ls "Сортировать книги? Думаю, освою."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Здесь не просто по алфавиту всё раскладывается."
    cs_narrator "Она показала на инвентарные номера."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Есть разделы, каталожные карточки, номера хранения."
    cs_ls "Тогда сначала объясни, что куда."
    cs_narrator "Женя пыталась понять, серьёзно ли я. Потом пододвинула стопку."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Хорошо. Вот эти пока разложи по авторам. Только ничего на полки самостоятельно не ставь."
    cs_ls "Принято."
    cs_narrator "Дарья подошла ближе."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Можно я тоже помогу?"
    cs_narrator "Женя посмотрела на неё."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Если аккуратно."
    cs_da "Постараемся."
    cs_narrator "Мы принялись разбирать книги."
    cs_narrator "Сложного ничего: сверять фамилии, названия, номера. Главное — не торопиться."
    cs_narrator "Я взяла очередную книгу и посмотрела на титульный лист."
    cs_ls "Интересная система."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "В каком смысле?"
    cs_ls "Всё можно найти без компьютера. Только нужно правильно организовать."
    cs_narrator "Женя нахмурилась."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А компьютер здесь при чём?"
    cs_th "А вот это сейчас лучше не развивать."
    cs_ls "Ни при чём. Просто сравниваю с тем, к чему привыкла."
    cs_narrator "Она кивнула."
    # cs_speaker: present
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Если систему не соблюдать, потом ничего не найдёшь."
    cs_ls "Вполне понимаю."
    cs_narrator "Я положила очередную книгу в нужную стопку."
    cs_ls "Хаос хорош, пока не приходится искать в нём конкретную вещь."
    cs_narrator "Взгляд Жени стал одобрительным."
    # cs_speaker: present
    show cs_zhenya shy pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вот именно."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья едва заметно улыбнулась."
    cs_th "Моё чувство порядка кому-то пригодилось."
    cs_narrator "Женя проверила разобранную стопку и кивнула."
    # cs_speaker: present
    show cs_zhenya shy pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Нормально. Спасибо."
    cs_ls "Всегда пожалуйста."
    cs_narrator "Она немного помолчала."
    # cs_speaker: present
    show cs_zhenya shy pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Обычно новенькие сюда приходят за книгами. А не помогать."
    cs_narrator "Я пожала плечами."
    cs_ls "Сегодня у меня вообще не самый обычный день."
    cs_narrator "Женя чуть заметно улыбнулась."
    # cs_speaker: present
    show cs_zhenya shrug pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Это я уже поняла."
    cs_narrator "Дарья тихо произнесла:"
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Видишь? Спокойное знакомство."
    cs_ls "Запишем в достижения."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только без шума."
    cs_narrator "Я немедленно понизила голос."
    cs_ls "Так точно."
    cs_narrator "Женя покачала головой, уже без раздражения."
    return
