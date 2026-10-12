# -*- coding: utf-8 -*-
# Full source PNGs, proportional virtual distances, one common visible baseline.
init -4 python:
    import json
    with renpy.file("mods/chuzaya_smena/sp/dasha_metadata.json") as cs_meta_file:
        cs_dasha_metadata = json.load(cs_meta_file)

    def cs_dasha_image(entry, distance, visible_height=1560.0):
        ratio = {"far":0.82, "normal":1.0, "close":1.22}[distance]
        left, top, right, bottom = entry["bbox"]
        factor = visible_height * ratio / (bottom - top)
        canvas_w, canvas_h = int(1000 * ratio), int(1600 * ratio)
        x = int(canvas_w / 2.0 - (left + right) / 2.0 * factor)
        y = int(canvas_h - bottom * factor)
        canvas = im.Composite((canvas_w, canvas_h), (x, y), im.FactorScale(entry["path"], factor))
        # Apply the scene's sunset lighting to custom actors too, retaining full PNGs.
        return ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(canvas, im.matrix.tint(1.0, 0.87, 0.78)), "True", canvas)

    for cs_costume, cs_entries in cs_dasha_metadata.items():
        for cs_entry in cs_entries:
            cs_number = cs_entry["number"]
            for cs_distance in ("far", "normal", "close"):
                cs_image = cs_dasha_image(cs_entry, cs_distance)
                cs_base = "cs_dasha_%s %d" % (cs_costume, cs_number)
                renpy.image(cs_base + " " + cs_distance, cs_image)
                if cs_costume == "pioneer":
                    # The author chose the surprised PNG for Darya's smiling reaction.
                    cs_reaction_image = cs_image
                    if cs_entry["pose"] == "smile":
                        cs_smile_entry = next(e for e in cs_entries if e["pose"] == "surprised")
                        cs_reaction_image = cs_dasha_image(cs_smile_entry, cs_distance)
                    renpy.image("cs_darya " + cs_entry["pose"] + " pioneer " + cs_distance, cs_reaction_image)
                    # Preserve older semantic names when a new set has no exact equivalent.
                    for cs_old_pose, cs_new_pose in {"sad":"worried", "shy":"surprised"}.items():
                        if cs_entry["pose"] == cs_new_pose:
                            renpy.image("cs_darya " + cs_old_pose + " pioneer " + cs_distance, cs_image)
                if cs_distance == "normal":
                    renpy.image(cs_base, cs_image)
                    if cs_costume == "pioneer":
                        renpy.image("cs_dasha_full %d" % cs_number, cs_image)
                        renpy.image("cs_darya " + cs_entry["pose"] + " pioneer", cs_reaction_image)
                        for cs_old_pose, cs_new_pose in {"sad":"worried", "shy":"surprised"}.items():
                            if cs_entry["pose"] == cs_new_pose:
                                renpy.image("cs_darya " + cs_old_pose + " pioneer", cs_image)
                if cs_costume == "winter":
                    cs_emotion = {1:"neutral",2:"smile",3:"interested",4:"sleep"}.get(cs_number, cs_entry.get("pose", "neutral"))
                    renpy.image("cs_dasha_winter " + cs_emotion + " " + cs_distance, cs_image)
                    if cs_distance == "normal": renpy.image("cs_dasha_winter " + cs_emotion, cs_image)
                    renpy.image("cs_dasha " + cs_emotion + " " + cs_distance, cs_image)
                    if cs_distance == "normal": renpy.image("cs_dasha " + cs_emotion, cs_image)

transform cs_dasha_far_right:
    xalign 0.97
    yanchor 1.0
    ypos 1.35

transform cs_dasha_close_right:
    xalign 0.97
    yanchor 1.0
    ypos 1.84

transform cs_day_sl_left:
    xalign 0.03
    yalign 1.0

transform cs_day_mt_center:
    xalign 0.5
    yalign 1.0
