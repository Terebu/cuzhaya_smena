# -*- coding: utf-8 -*-
# Native-sized source PNGs share the established Darya canvas and baseline.
init -2 python:
    cs_pajama_sources = {
        "neutral": {"path": "sp/darya_pajamas/darya_pajamas_neutral.png", "bbox": [0,14,919,1656]},
        "smile": {"path": "sp/darya_pajamas/darya_pajamas_smile.png", "bbox": [58,14,913,1657]},
        "sleepy": {"path": "sp/darya_pajamas/darya_pajamas_sleepy.png", "bbox": [0,14,927,1657]},
    }
    for cs_pajama_pose, cs_pajama_entry in cs_pajama_sources.items():
        for cs_pajama_distance in ("far", "normal", "close"):
            renpy.image("cs_darya " + cs_pajama_pose + " pajamas " + cs_pajama_distance,
                        cs_dasha_image(cs_pajama_entry,cs_pajama_distance))
    # Semantic aliases let the existing emotion director retain the costume.
    for cs_pajama_alias,cs_pajama_pose in {"shrug":"neutral","thinking":"neutral","worried":"neutral","serious":"neutral","amused":"smile","shy_smile":"smile","shy":"smile","sad":"neutral"}.items():
        for cs_pajama_distance in ("far", "normal", "close"):
            renpy.image("cs_darya " + cs_pajama_alias + " pajamas " + cs_pajama_distance,
                        cs_dasha_image(cs_pajama_sources[cs_pajama_pose],cs_pajama_distance))

image cs_bus410_closed_day = im.Scale(cs_root + "bg/bus_stop/camp_bus410_closed_day.png",1920,1080)
image cs_bus410_open_day = im.Scale(cs_root + "bg/bus_stop/camp_bus410_open_day.png",1920,1080)

# The native game includes a lit night library. Keep the published mod alias.
# Image statements run at 500, so replace the historical daytime composite afterwards.
init 510 python:
    renpy.image("cs_library_interior_night", "images/bg/int_library_night2.jpg")
