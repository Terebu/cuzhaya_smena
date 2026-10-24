# -*- coding: utf-8 -*-
# Full PNGs use the same proportional canvas and foot baseline as the uniform.
# The shared cs_darya tag replaces the costume instead of stacking portraits.
init -3 python:
    cs_darya_underwear_entries = [
        {"pose": "hair_touch", "path": "sp/Dasha sprites/bra/darya_underwear_hair_touch.png", "bbox": [50, 11, 927, 1672]},
        {"pose": "neutral", "path": "sp/Dasha sprites/bra/darya_underwear_neutral.png", "bbox": [62, 0, 921, 1672]},
    ]
    for cs_entry in cs_darya_underwear_entries:
        for cs_distance in ("far", "normal", "close"):
            renpy.image("cs_darya " + cs_entry["pose"] + " underwear " + cs_distance,
                        cs_dasha_image(cs_entry, cs_distance))
