"""Record hashes only AFTER the listed contact pages were visually inspected."""
from pathlib import Path
import sys,json,hashlib
stage=Path(sys.argv[1]);folder=Path(sys.argv[2]);out=stage/'reviewed_contact_pages.json'
data=json.loads(out.read_text()) if out.exists() else {}
for number in sys.argv[3:]:
    page=folder/('%02d.png'%int(number));assert page.is_file()
    data[str(page)]=hashlib.sha256(page.read_bytes()).hexdigest()
out.write_text(json.dumps(data,indent=2),encoding='utf8')
print('Recorded inspected pages:',len(sys.argv)-3)
