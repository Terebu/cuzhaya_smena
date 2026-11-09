# -*- coding: utf-8 -*-
# 2026-11-08: полная публичная редакция снова основная.
# Сокращённый слой days/revision20261106 оставлен на диске, но больше не
# подменяет опубликованные метки пролога и дней 1–4.

init 130 python:
    for _cs_label in list(cs_rev_label_overrides):
        if config.label_overrides.get(_cs_label) == cs_rev_label_overrides[_cs_label]:
            config.label_overrides.pop(_cs_label, None)

    if cs_rev_migrate_loaded_story in config.after_load_callbacks:
        config.after_load_callbacks.remove(cs_rev_migrate_loaded_story)

    cs_pub_day_labels = {0: "chuzhaya_smena_start", 1: "cs_day01", 2: "cs_day02", 3: "cs_day03", 4: "cs_day04"}

    def cs_pub_migrate_loaded_story():
        # Сохранение внутри сокращённой редакции переносим в начало того же
        # дня полной версии: текст там другой, и продолжить с середины нельзя.
        if not getattr(store, "cs_active", False):
            return
        candidates = list(reversed(renpy.get_return_stack())) + [renpy.game.context().current]
        for address in candidates:
            try:
                node = renpy.game.script.lookup(address)
            except Exception:
                continue
            filename = str(getattr(node, "filename", "")).replace("\\", "/")
            if "/revision20261106/" not in filename:
                continue
            day = int(getattr(store, "cs_rev_day", 0) or 0)
            store.cs_rev_active = False
            renpy.block_rollback()
            renpy.set_return_stack([])
            renpy.jump(cs_pub_day_labels.get(day, "cs_day01"))
    config.after_load_callbacks.append(cs_pub_migrate_loaded_story)
