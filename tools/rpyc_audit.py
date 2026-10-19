"""Read Ren'Py 7 AST data without importing or executing its Python code."""
from pathlib import Path
import io, pickle, struct, zlib, collections, hashlib

class Record:
    def __new__(cls, *args, **kwargs): return object.__new__(cls)
    def __setstate__(self, state):
        self.state = state
        if isinstance(state, dict): self.__dict__.update(state)
        elif isinstance(state, tuple):
            for part in state:
                if isinstance(part, dict): self.__dict__.update(part)

CLASSES = {}
class DataUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module in ('builtins', '__builtin__') and name in ('set','frozenset','object'):
            return {'set':set,'frozenset':frozenset,'object':object}[name]
        if module == 'collections' and name == 'defaultdict': return collections.defaultdict
        key = module, name
        if key not in CLASSES:
            base = str if name in ('PyExpr','PyExprLiteral') else {'RevertableDict':dict,'RevertableList':list,'RevertableSet':set}.get(name,Record)
            attrs = {'audit_module':module}
            if base is str: attrs['__new__'] = lambda cls,*a: str.__new__(cls,a[0] if a else '')
            elif base in (dict,list,set): attrs['__setstate__'] = Record.__setstate__
            CLASSES[key] = type(name,(base,),attrs)
        return CLASSES[key]

def payload(path, slot=1):
    data = Path(path).read_bytes()
    if data.startswith(b'RENPY RPC2'):
        pos = 10
        while True:
            number,start,length = struct.unpack('<III',data[pos:pos+12]); pos += 12
            if number == slot: return zlib.decompress(data[start:start+length])
            if not number: raise ValueError('Missing RPYC slot')
    return zlib.decompress(data)

def inspect(path, slot=1):
    root = DataUnpickler(io.BytesIO(payload(path, slot)),encoding='utf8',errors='replace').load()
    seen=set(); nodes=[]; stack=[root]
    while stack:
        obj=stack.pop()
        if id(obj) in seen: continue
        seen.add(id(obj))
        if isinstance(obj,dict): stack.extend(obj.values())
        elif isinstance(obj,(tuple,list,set,frozenset)): stack.extend(obj)
        elif hasattr(obj,'__dict__'):
            attrs=vars(obj); stack.extend(attrs.values())
            if getattr(obj,'audit_module','') == 'renpy.ast' and 'name' in attrs:
                nodes.append({'id':attrs['name'],'kind':type(obj).__name__,
                              'filename':attrs.get('filename'),'line':attrs.get('linenumber'),
                              'image':attrs.get('imgname'),
                              'screen':getattr(attrs.get('screen'),'name',None)})
    return {'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'nodes':nodes}

def identifiers(info):
    return {repr(n['id']) for n in info['nodes']}
