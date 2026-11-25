# -*- coding: utf-8 -*-
# Expand story Say nodes at init so compiled statement IDs and old saves
# continue to enter on the first sentence. Each page is a real ADV Say.
init 190 python:
    import re as cs_sent_re
    from __builtin__ import set as cs_sent_set

    cs_sent_tokens = cs_sent_re.compile(ur"\{\{|\[\[|\{[^{}]+\}|\[[^\[\]]+\]")
    cs_sent_end = cs_sent_re.compile(
        ur"[.!?…。！？]+(?:[»”’\"')\]]+[.!?…。！？]*)*")
    cs_sent_start = cs_sent_re.compile(ur"[«„“\"'(\[\u2014\u2013]*[ \t]*[A-ZА-ЯЁ0-9\u3040-\u30ff\u3400-\u9fff]")
    cs_sent_japanese = cs_sent_re.compile(ur"[\u3040-\u30ff\u3400-\u9fff]")
    cs_sent_guillemets = cs_sent_re.compile(ur"[«»]")
    cs_sent_short = cs_sent_re.compile(
        ur"(?:\d+\s+(?:г|д)|\b(?:тов|им|ул|стр|рис|гл|см|ср|руб|коп|мин|сек|проф|акад))\.$",
        cs_sent_re.I)
    cs_sent_initial = cs_sent_re.compile(
        ur"(?:^|\s)(?:[А-ЯЁA-Z]\.\s*)+[А-ЯЁA-Z]\.$|(?:^|\s)[А-ЯЁA-Z]\.$")
    cs_sent_compound = cs_sent_re.compile(ur"(?:^|\s)[тТ]\.\s*$")
    cs_sent_compound_tail = cs_sent_re.compile(ur"[едпш]\.", cs_sent_re.I)
    cs_sent_format = cs_sent_set(("a", "alpha", "b", "color", "cps", "font",
        "i", "k", "outlinecolor", "plain", "s", "size", "u"))

    def cs_sent_projection(text):
        visible, offsets, marks = [], [], []
        start = 0
        for match in cs_sent_tokens.finditer(text):
            visible.append(text[start:match.start()])
            offsets.extend(range(start, match.start()))
            token = match.group()
            if token.startswith(u"{") and token != u"{{":
                marks.append((match.start(), match.end(), token))
            else:
                # Interpolations are never inspected as punctuation.
                visible.append(token[0] if token in (u"{{", u"[[") else u"Я")
                offsets.append(match.start())
            start = match.end()
        visible.append(text[start:])
        offsets.extend(range(start, len(text)))
        return u"".join(visible), offsets, marks

    def cs_sent_abbreviation(visible, match, following):
        if match.group() != u".":
            return False
        prefix = visible[:match.end()]
        if cs_sent_compound.search(prefix) and cs_sent_compound_tail.match(following):
            return True
        if cs_sent_short.search(prefix):
            return True
        # A lone "Я." is a sentence. Recognize initials before a name.
        if cs_sent_initial.search(prefix) and prefix[-2] != u"Я":
            return bool(cs_sent_re.match(ur"[А-ЯЁA-Z](?:\.|[а-яёa-z])", following))
        return False

    def cs_sentence_layout(text):
        visible, offsets, marks = cs_sent_projection(text)
        cuts, page_ids = [], [[0]]
        quote_depth = quote_cursor = old_page = 0
        for match in cs_sent_end.finditer(visible):
            stop = match.end()
            for quote in cs_sent_guillemets.finditer(visible, quote_cursor, stop):
                if quote.group() == u"«":
                    quote_depth += 1
                else:
                    quote_depth = max(0, quote_depth - 1)
            quote_cursor = stop
            if stop == len(visible):
                continue
            rest = visible[stop:]
            following = rest.lstrip()
            if not following:
                continue
            japanese = (match.group()[0] in u"。！？" and
                        cs_sent_japanese.match(following))
            if not japanese and (rest == following or not cs_sent_start.match(following)):
                continue
            if cs_sent_abbreviation(visible, match, following):
                continue
            old_page += 1
            if quote_depth:
                # Resume saves made on a former continuation at the full quote.
                page_ids[-1].append(old_page)
                continue
            page_ids.append([old_page])
            cut = offsets[len(visible) - len(following)]
            for tag_start, tag_end, token in reversed(marks):
                if tag_end > cut:
                    continue
                if text[tag_end:cut].strip() or token.startswith(u"{/"):
                    break
                cut = tag_start
            cuts.append(cut)
        if not cuts:
            return [text], page_ids

        # Restore active formatting on the next page. Closing tags before the
        # boundary stay attached to the sentence they originally formatted.
        pages, active = [], []
        start = mark_index = 0
        prefix = u""
        for end in cuts + [len(text)]:
            while mark_index < len(marks) and marks[mark_index][1] <= end:
                tag_start, tag_end, token = marks[mark_index]
                tag = token[1:-1].split(u"=", 1)[0]
                if tag in cs_sent_format:
                    active.append((tag, token))
                elif tag.startswith(u"/") and active and active[-1][0] == tag[1:]:
                    active.pop()
                mark_index += 1
            part = text[start:end].strip()
            if end != len(text):
                suffix = u"".join(u"{/%s}" % tag for tag, token in reversed(active))
            else:
                suffix = u""
            pages.append(prefix + part + suffix)
            prefix = u"".join(token for tag, token in active)
            start = end
        return pages, page_ids

    def cs_sentence_pages(text):
        return cs_sentence_layout(text)[0]

    def cs_install_sentence_pages():
        script = renpy.game.script
        entry = script.lookup("chuzhaya_smena_start")
        root = entry.filename.replace("\\", "/").rsplit("/", 1)[0] + "/days/"
        nodes = cs_sent_set(script.namemap.values())
        counts = [0, 0]
        for node in nodes:
            if not isinstance(node, renpy.ast.Say) or not node.interact:
                continue
            if not node.filename.replace("\\", "/").startswith(root):
                continue
            pages, page_ids = cs_sentence_layout(node.what)
            continuation = node.next
            for index in range(len(pages) - 1, 0, -1):
                names = [("cs_adv_sentence", node.name, old_id) for old_id in page_ids[index]]
                page = renpy.ast.Say((node.filename, node.linenumber), node.who,
                                     pages[index], None)
                page.name = names[0]
                page.chain(continuation)
                for name in names:
                    script.namemap[name] = page
                continuation = page
            for old_id in page_ids[0][1:]:
                script.namemap[("cs_adv_sentence", node.name, old_id)] = node
            if len(pages) > 1:
                node.what = pages[0]
                node.chain(continuation)
                counts[0] += 1
                counts[1] += len(pages) - 1
        return tuple(counts)

    cs_sentence_page_counts = cs_install_sentence_pages()
