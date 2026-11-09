# -*- coding: utf-8 -*-
# Older saves can resume the published scene after its newly corrected cues.
init 100 python:
    def cs_legacy_day04_arrival_repair():
        if not getattr(store,'cs_active',False):return
        node=renpy.game.script.lookup(renpy.game.context().current)
        path=str(getattr(node,'filename','')).replace('\\','/').rstrip('c')
        if type(node).__name__!='Say' or not path.endswith('/days/day04/04_scene.rpy'):return
        boundary=None
        for candidate in renpy.game.script.namemap.values():
            if (type(candidate).__name__=='Say' and candidate.filename==node.filename
                    and getattr(candidate,'what','')==u'И побежала к скамейке.'):
                boundary=candidate.linenumber
                break
        if boundary is None:return
        if node.linenumber<=boundary:
            store.cs_d4_scene_cast=[t for t in cs_d4_scene_cast if t!='cs_semen']
            cs_actor_exit(['cs_semen'])
        elif getattr(node,'what','')==u'Сёмочка!' and 'cs_semen' not in cs_d4_scene_cast:
            store.cs_d4_scene_cast=list(cs_d4_scene_cast)+['cs_semen']
            cs_frame_focus(cs_d4_scene_cast)
    def cs_legacy_day04_arrival_at_line(event,**kwargs):
        if event=='begin':cs_legacy_day04_arrival_repair()
    config.after_load_callbacks.append(cs_legacy_day04_arrival_repair)
    config.all_character_callbacks.append(cs_legacy_day04_arrival_at_line)
