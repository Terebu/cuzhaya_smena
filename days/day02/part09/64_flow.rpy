# -*- coding: utf-8 -*-
label cs_day02_dinner_branches:
    if cs_friend_mz >= 2:
        call cs_day02_64a from cs_return_a62d75454298c100f349
    elif cs_friend_mz == 1:
        call cs_day02_64b from cs_return_e5086dc02802f25a9bd7
    else:
        call cs_day02_64c from cs_return_789ffc2f9db834902041
    label cs_check_part09_dinner:
    if cs_friend_mz >= 1:
        call cs_day02_64d from cs_return_86432cbaaf80281c6838
        if cs_friend_mz >= 2 and cs_mz_map_lead:
            call cs_day02_64d1 from cs_return_d2ce00d5a94fb8c4b689
        elif cs_friend_mz == 1:
            call cs_day02_64d2 from cs_return_a8601540a1343314556d
    call cs_day02_64e from cs_return_0fbc106550fabbfca128
    return
