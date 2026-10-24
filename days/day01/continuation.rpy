# -*- coding: utf-8 -*-
default cs_day01_part05_done = False
default cs_day01_part06_done = False
default cs_day01_part07_done = False
default cs_day01_part08_done = False
default cs_day01_part09_done = False

label cs_day01_part05:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_21 from cs_return_c47d52941cb207a78bfd
    call cs_day01_22 from cs_return_f5f9539bb845c12af8c7
    call cs_day01_23 from cs_return_654843b1f6d28eeac03a
    call cs_day01_24 from cs_return_140af7a17ae893242962
    $ cs_day01_part05_done = True
    jump cs_day01_part06

label cs_day01_part06:
    hide screen cs_day01_pending
    # Continue the same table and music into the end of lunch, without a reset.
    call cs_day01_25 from cs_return_992c1cccc08ad8afa3ec
    call cs_day01_26 from cs_return_726967f478537e58a8ec
    call cs_day01_27 from cs_return_ea544910f5748abc8e93
    call cs_day01_28 from cs_return_39d21437b2a7e19816a2
    call cs_day01_29 from cs_return_e473e1321963263aaa44
    call cs_day01_30 from cs_return_f6e648729d50ccabfa65
    $ cs_day01_part06_done = True
    jump cs_day01_part07_pending

label cs_day01_part07_pending:
    jump cs_day01_part07

# Preserve the label stored by saves made at the previous development stop.
label cs_check_day01_part06_pending:
    jump cs_day01_part07

label cs_day01_part07:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_31 from cs_return_0efbcddf18ee22127c68
    call cs_day01_32 from cs_return_84d3ff730842ee7d3176
    call cs_day01_33 from cs_return_a1ef66bce9aec24f9c9b
    call cs_day01_34 from cs_return_1a643fd2c199512bbe5f
    call cs_day01_35 from cs_return_05d71f68c20bf1057b2c
    call cs_day01_36 from cs_return_85d67261eea2430dc298
    call cs_day01_37 from cs_return_39d7d99678f16b4e8646
    call cs_day01_38 from cs_return_e1aa52b56f907ddfd2ac
    call cs_day01_39 from cs_return_11064c6f75699eb8a289
    $ cs_day01_part07_done = True
    jump cs_day01_part08_pending

label cs_day01_part08_pending:
    jump cs_day01_part08

label cs_check_day01_part07_pending:
    jump cs_day01_part08

label cs_day01_part08:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_40 from cs_return_7644dc7d360078662f9f
    call cs_day01_41 from cs_return_0aa4c226394b9e84e02d
    call cs_day01_42 from cs_return_60bfca97ac00d9fe84a0
    call cs_day01_43 from cs_return_d3ea5238429f2ae29dff
    call cs_day01_44 from cs_return_f3ac7a28cfab7304d2ce
    call cs_day01_45 from cs_return_fb508625606ab7d10e88
    $ cs_day01_part08_done = True
    jump cs_day01_part09_pending

label cs_day01_part09_pending:
    jump cs_day01_part09

label cs_check_day01_part08_pending:
    jump cs_day01_part09

label cs_day01_part09:
    if cs_day01_part09_done:
        jump cs_day01_part10_pending
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_46 from cs_return_5a981f2e40168ecef323
    call cs_day01_47 from cs_return_09172f467a7023e72b39
    call cs_day01_49 from cs_return_95c426ea9547ae6145a7
    call cs_day01_50 from cs_return_e4b18e25507c8790e42d
    call cs_day01_51 from cs_return_2a8b12ab805274e534ab
    $ cs_day01_part09_done = True
    jump cs_day01_part10_pending

label cs_day01_part10_pending:
    jump cs_day01_part10

label cs_check_day01_part09_pending:
    jump cs_day01_part10

label cs_day01_part10:
    if cs_day01_part10_done:
        jump cs_day01_part11_pending
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_dinner_bridge from cs_return_293f313792eacc221605
    call cs_day01_52 from cs_return_7c87e187dfd1363fe1c3
    call cs_day01_53 from cs_return_afd6862d2860abf4ac05
    call cs_day01_54 from cs_return_95648f7a37d61c362cb8
    call cs_day01_55 from cs_return_6a36c960251a17c2c4a7
    call cs_day01_56 from cs_return_fe583e76fb77654ab6d2
    call cs_day01_57 from cs_return_9a78c1d52232fa918780
    call cs_day01_58 from cs_return_2926223c95ea032d1328
    $ cs_day01_part10_done = True
    jump cs_day01_part11_pending

label cs_day01_part11_pending:
    jump cs_day01_part11

label cs_check_day01_part10_pending:
    jump cs_day01_part11
