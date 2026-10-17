# -*- coding: utf-8 -*-
testcase cs_mod_image_registry:
    pause 1.0
    $ cs_registry_refs = json.load(renpy.file("mods/chuzaya_smena/qa/mod_literal_stage_references.json"))
    $ cs_registry_missing_images = [x for x in cs_registry_refs["images"] if not renpy.has_image(x)]
    $ cs_registry_missing_audio = [x for x in cs_registry_refs["audio"] if not renpy.loadable(x)]
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/mod_image_registry_result.json", "w").write(json.dumps(dict(images=len(cs_registry_refs["images"]),audio=len(cs_registry_refs["audio"]),missing_images=cs_registry_missing_images,missing_audio=cs_registry_missing_audio)))
    assert not cs_registry_missing_images and not cs_registry_missing_audio
    run Quit(confirm=False)
