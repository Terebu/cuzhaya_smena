# -*- coding: utf-8 -*-
# 8 November: the original Everlasting Summer cast joins the emotion director.
# The new edition shows them once as "<tag> normal pioneer" and never changes
# the expression. The same director that drives Darya, Semyon, Zhenya and
# Viola now picks an expression from the line (speech) or from an explicit
# stage direction in narration ("Славя улыбнулась"). Only images that exist
# for the current costume are used: renpy.has_image filters every pool.
init -4 python:
    cs_emo_es_pools = {
        "calm": (["normal", "serious", "tender", "normal_smile"], []),
        "explain": (["normal", "serious", "smile", "normal_smile"], []),
        "curious": (["surprise", "surp1", "normal", "serious"], []),
        "smile": (["smile", "smile2", "happy", "tender", "normal_smile", "grin"], ["happy", "laugh"]),
        "laugh": (["laugh", "grin", "happy", "laugh2", "smile2"], ["laugh", "laugh2"]),
        "shy": (["shy", "smile3", "tender"], ["shy"]),
        "surprise": (["surprise", "surp1", "surp2", "shocked"], ["surp3", "shocked", "scared"]),
        "sad": (["sad", "upset", "serious", "guilty"], ["sad", "scared"]),
        "cry": (["sad", "cry_smile", "upset"], ["cry"]),
        "mad": (["angry", "dontlike", "upset", "serious"], ["angry", "angry2", "rage"]),
    }
    # Olga Dmitrievna and the engineers are calmer on screen.
    cs_emo_es_adult = dict(cs_emo_es_pools, cry=(["sad", "serious"], []), shy=(["smile", "normal"], []))

    # Preserve all genuine Slavya expressions. Image existence is checked
    # exactly by the shared director, rather than by an approximate match.
    cs_emo_sl_pools = cs_emo_es_pools

    cs_emo_actors.update({
        "sl": (cs_emo_sl_pools, 0, u"слав[яиеюй]"),
        "un": (cs_emo_es_pools, 0, u"тихонов|тёзк|тезк"),
        "mt": (cs_emo_es_adult, 0, u"ольг[аеиу] дмитриевн|вожат[аыоуе]"),
        "mi": (cs_emo_es_pools, 0, u"мику"),
        "dv": (cs_emo_es_pools, 0, u"алис[аеыуой]"),
        "us": (cs_emo_es_pools, 0, u"ульян"),
        "sh": (cs_emo_es_adult, 0, u"шурик"),
        "el": (cs_emo_es_adult, 0, u"электроник"),
    })
    cs_emo_speakers.update({
        "cs_sl": ("sl",), "cs_un": ("un",), "cs_mt": ("mt",), "cs_mi": ("mi",),
        "cs_dv": ("dv",), "cs_us": ("us",), "cs_sh": ("sh",), "cs_el": ("el",),
    })

# Repair this mod's obsolete, unsupported auto-selected attributes. Images remain
# untouched for the base game and other mods, including their authored scenes.
init 46 python:
    def cs_sl_conversation_image(name):
        name = tuple(name)
        if name and name[0] == 'sl':
            if not renpy.has_image(name, exact=True):
                # Old auto pools could save unsupported attributes such as
                # upset/guilty. Restore a registered expression, same costume.
                pose = 'sad' if name[1:2] in (('upset',), ('guilty',)) else 'normal'
                fixed = ('sl', pose) + name[2:]
                if renpy.has_image(fixed, exact=True):return fixed
        return name

    def cs_sl_repair_conversation_pose():
        if not getattr(store, 'cs_active', False):return
        cached = cs_director_people.get('sl')
        if cached:
            name, positions = cached
            fixed = cs_sl_conversation_image(name)
            if fixed != tuple(name):
                store.cs_director_people['sl'] = (fixed, positions)
        if not renpy.showing('sl'):return
        name = ('sl',) + tuple(renpy.get_attributes('sl') or ())
        fixed = cs_sl_conversation_image(name)
        if fixed != name:
            if not renpy.has_image(fixed, exact=True):
                raise Exception('Missing Slavya conversation pose: %r' % (fixed,))
            renpy.show(fixed)
            store.cs_emo_state.pop('sl', None)
            cs_presence_stage()

    def cs_sl_repair_at_line(event, **kwargs):
        if event == 'begin':cs_sl_repair_conversation_pose()
    config.all_character_callbacks.append(cs_sl_repair_at_line)
    config.after_load_callbacks.append(cs_sl_repair_conversation_pose)
    config.interact_callbacks.append(cs_sl_repair_conversation_pose)
