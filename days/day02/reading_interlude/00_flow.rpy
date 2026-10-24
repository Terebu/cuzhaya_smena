# -*- coding: utf-8 -*-
label cs_day02_reading_interlude:
    call cs_day02_reading_01 from cs_return_76a7762f8da99a69c15b
    call cs_day02_reading_02 from cs_return_777e3495d296730b3c2d
    call cs_day02_reading_03 from cs_return_65673aaffe76884ed9e2
    if cs_friend_mz >= 2:
        call cs_day02_reading_04c from cs_return_d4a181871ff1f1bb3f28
    elif cs_friend_mz == 1:
        call cs_day02_reading_04b from cs_return_8f502f693aadc5270606
    else:
        call cs_day02_reading_04a from cs_return_0f281c307d32dbe675b9
    call cs_day02_reading_05 from cs_return_08f03e3b17bce02dfdcc
    call cs_day02_reading_06 from cs_return_4fdc41289c32dc91521b
    if cs_friend_mz >= 2:
        call cs_day02_reading_07c from cs_return_3d6c4d0ce376060090f9
    elif cs_friend_mz == 1:
        call cs_day02_reading_07b from cs_return_1f9bf03f629484b2199a
    else:
        call cs_day02_reading_07a from cs_return_910ef6a948b8fb5aa2cd
    call cs_day02_reading_08 from cs_return_c09a40408445d3593bc8
    call cs_day02_reading_09 from cs_return_2d17585def89c6e55080
    call cs_day02_reading_book_drop from cs_return_e2fc3dfa4abf2705c7e7
    $ cs_reading_live = False
    return
