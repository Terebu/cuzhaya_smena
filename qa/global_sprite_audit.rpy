# -*- coding: utf-8 -*-
default cs_qa_global_audit = False
default cs_qa_global_dialogue_checks = 0
default cs_qa_global_cg_checks = 0
default cs_qa_global_reflective_checks = 0
default cs_qa_global_speaker_checks = 0
init 45 python:
    import json
    with renpy.file("mods/chuzaya_smena/qa/dialogue_statement_lookup.json") as cs_qa_lookup_file:
        cs_qa_speech_lookup = json.load(cs_qa_lookup_file)
    with renpy.file("mods/chuzaya_smena/source/offscreen_dialogue.json") as cs_qa_voice_file:
        cs_qa_offscreen_voices = json.load(cs_qa_voice_file)
    cs_qa_voice_tags = dict(cs_da=("cs_darya", "cs_dasha_winter"), cs_sy=("cs_semen",), cs_sl=("sl",), cs_mt=("mt",), cs_dv=("dv",), cs_us=("us",), cs_sh=("sh",), cs_el=("el",), cs_un=("un",), cs_mz=("cs_zhenya",), cs_vi=("cs",), cs_mi=("mi",))
    def cs_qa_global_images(event, **kwargs):
        if event != "show_done" or not cs_qa_global_audit:
            return
        store.cs_qa_global_dialogue_checks += 1
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_dasha_full", "cs_dasha", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "us", "sl", "mt", "el", "sh", "cs")
        if cs_reflective_shot:
            store.cs_qa_global_reflective_checks += 1
            if any(renpy.showing(t) for t in tags):
                raise Exception("Actor leaked into authored REFLECTIVE_SHOT at %r" % (renpy.get_filename_line(),))
        for tag in tags:
            if renpy.showing(tag):
                attributes = renpy.get_attributes(tag)
                if not renpy.has_image((tag,) + tuple(attributes or ())):
                    raise Exception("Missing actor image: %r" % ((tag,) + tuple(attributes or ()),))
        if renpy.showing("mz") and renpy.showing("cs_zhenya"):
            raise Exception("Two representations of Zhenya")
        if renpy.showing("cs_dasha_winter") and renpy.showing("cs_darya"):
            raise Exception("Winter and pioneer Darya simultaneously")
        full_cgs = [t for t in renpy.get_showing_tags() if t.startswith("cs_cg_") or t in ("cs_sleep_winter", "cs_sleep_summer", "cs_lena_pioneer_mirror")]
        if full_cgs:
            store.cs_qa_global_cg_checks += 1
        if full_cgs and [t for t in tags if renpy.showing(t)]:
            raise Exception("Portraits over full-screen CG: %r" % full_cgs)
        filename, line = renpy.get_filename_line()
        relative = filename.replace("\\", "/").split("chuzaya_smena/", 1)[-1]
        statement = cs_qa_speech_lookup.get(relative, {}).get(str(line))
        if statement and statement["speaker"] in cs_qa_voice_tags and not full_cgs:
            voice = dict(file=relative, speaker=statement["speaker"], text=statement["text"])
            offscreen = any(__import__("__builtin__").all(e.get(k) == v for k, v in voice.items()) for e in cs_qa_offscreen_voices)
            if not offscreen:
                store.cs_qa_global_speaker_checks += 1
                if not any(renpy.showing(t) for t in cs_qa_voice_tags[statement["speaker"]]):
                    raise Exception("Invisible interlocutor at %s:%s: %s" % (relative, line, statement["speaker"]))
        if len([t for t in tags if renpy.showing(t)]) > 3:
            raise Exception("More than three portraits in one authored frame at %s:%s" % (relative, line))
    config.all_character_callbacks.append(cs_qa_global_images)
