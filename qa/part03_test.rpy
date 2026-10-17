# -*- coding: utf-8 -*-
default cs_qa_part03_audit = False
init 40 python:
    class CSQAwaitMenu(Action):
        def get_sensitive(self):
            return renpy.get_screen("choice") is not None or renpy.get_screen("cs_mod_choice") is not None
        def __call__(self):
            pass
    class CSQASelectChoice(Action):
        def __init__(self, caption):
            self.caption = caption
        def _item(self):
            screen = renpy.get_screen("cs_mod_choice") or renpy.get_screen("choice")
            if screen is None:
                return None
            for item in screen.scope.get("items", []):
                if item.caption == self.caption and item.action is not None:
                    return item
            return None
        def get_sensitive(self):
            return self._item() is not None
        def __call__(self):
            item = self._item()
            if item is None:
                raise Exception("Expected menu choice: %r" % self.caption)
            result = renpy.display.behavior.run(item.action)
            if result is not None:
                renpy.end_interaction(result)
            return result
    def cs_qa_part03_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part03_audit or not cs_part03_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [tag for tag in tags if renpy.showing(tag)]
        if len(actual) > 2 or set(actual) != set(cs_part03_cast):
            raise Exception("Incorrect part-3 cast: %r instead of %r" % (actual, cs_part03_cast))
        if cs_part03_cg and actual:
            raise Exception("Portrait on full-screen illustration")
    config.all_character_callbacks.append(cs_qa_part03_cast)

label cs_qa_part03_path:
    $ cs_qa_part02_audit = True
    $ cs_qa_part03_audit = True
    $ cs_darya_known = True
    $ cs_day02_miku_listened = None
    $ cs_sl_day2_awarded = False
    $ cs_friend_mi = 0
    $ cs_friend_sl = 0
    $ day_time()
    $ persistent.sprite_time = "day"
    window show
    call cs_day02_14
    jump cs_day02_part02_pending

label cs_qa_sl_replay:
    hide screen cs_day02_continue_screen
    window show
    call cs_day02_24
    jump cs_day02_part04_pending
