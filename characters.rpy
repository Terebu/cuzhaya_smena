# -*- coding: utf-8 -*-
# Namespaced IDs deliberately separate Lena Sokolova from the game's un.
init 20 python:
    cs_ls = Character(u"Лена", color="#c9a8ee", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_da = DynamicCharacter("u'Дарья' if cs_darya_known else u'Незнакомка'", color="#f0a59c", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_narrator = Character(None, what_style="narrator_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_th = Character(None, what_style="thoughts_prolog", what_italic=True, what_prefix=u"~ ", what_suffix=u" ~", ctc="ctc_animation", ctc_position="fixed")
    cs_sy = Character(u"Семён", color="#e7d596", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
