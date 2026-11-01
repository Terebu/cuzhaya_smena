"""Replay reviewed day-four prose edits after manuscript generation.
The original supplied manuscript stays intact; exact changes are auditable JSON.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parent.parent
changed=0
for group in ("early","middle","late"):
    edits=json.loads((R/("source/day04_prose_"+group+".json")).read_text(encoding="utf8"))
    for e in edits:
        p=R/e["file"];s=p.read_text(encoding="utf8")
        if e.get("kind")=="span":
            assert s.count(e["start"])==s.count(e["end"])==1,e["file"]
            start=s.index(e["start"])+len(e["start"])
            end=s.index(e["end"],start)
            result=s[:start]+e["after"]+s[end:]
        elif e["after"] and e["after"] in s:
            continue
        elif e["before"] in s:
            assert e["before"] and s.count(e["before"])==1,(e["file"],e["before"][:60])
            result=s.replace(e["before"],e["after"],1)
        else:
            assert e["after"] and e["after"] in s,(e["file"],"Editorial anchor missing",e["before"][:60])
            continue
        if result!=s:
            p.write_text(result,encoding="utf8");changed+=1
print("DAY04_PROSE_APPLIED",changed)
