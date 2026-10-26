"""Keep already-issued explicit return labels during authoring regeneration."""
import re
from collections import defaultdict
def preserve_calls(old,new):
    pattern=re.compile(r'^(\s*call (cs_\w+))(?: from (cs_return_\w+))?$',re.M)
    labels=defaultdict(list)
    for m in pattern.finditer(old):labels[m[2]].append(m[3])
    indices=defaultdict(int)
    def replace(m):
        i=indices[m[2]];indices[m[2]]+=1
        prior=labels[m[2]][i] if i<len(labels[m[2]]) else None
        return m[1]+(' from '+prior if prior else '')
    return pattern.sub(replace,new)
