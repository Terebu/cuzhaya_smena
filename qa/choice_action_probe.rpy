# -*- coding: utf-8 -*-
testcase cs_choice_action_probe:
    pause 1.0
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_actual_part08")
    pause 0.6
    run Jump("cs_check_day01_part08_pending")
    click until run CSQASelectChoice("Остановиться и познакомиться")
    click until label cs_check_day01_part09_merge
    assert cs_part09_choice == "meet" and cs_met_un
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/choice_action_probe_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
