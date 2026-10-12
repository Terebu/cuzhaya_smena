# -*- coding: utf-8 -*-
default cs_friend_un = 0
default cs_met_un = False
default cs_un_name_known = False
default cs_part09_choice = None

init 20 python:
    cs_un = DynamicCharacter("u'Лена Тихонова' if cs_un_name_known else u'Неизвестная девушка'", color="#b956ff", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
