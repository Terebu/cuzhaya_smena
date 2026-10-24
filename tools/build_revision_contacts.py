from pathlib import Path
import subprocess,sys,json
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024')
engine=stage/'validation/steamapps/common/Everlasting Summer'
for prefix in ('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_revision_','p6_p7_','p6_costume_','revision_cross_'):
 subprocess.run([sys.executable,str(R/'tools/build_qa_contact_sheets.py'),str(engine),prefix,'64'],check=True)
