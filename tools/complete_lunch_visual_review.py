from pathlib import Path
import json,hashlib
stage=Path('D:/stean/release_chuzaya_smena/day03_part07_revision_20261024')
engine=stage/'validation/steamapps/common/Everlasting Summer'
ledger=json.loads((stage/'reviewed_contact_pages.json').read_text())
folders=['p6_render_reviewed_high_contacts','p6_render_reviewed_low_contacts','p6_lunch_revision_contacts',
         'p6_revision_camera_contacts','p6_p7_attention_contacts','p6_p7_camera_contacts','p6_costume_contacts','p6_lunch_cross_save_contacts']
pages=[];frames=[]
for name in folders:
    folder=engine/name
    for item in json.loads((folder/'index.json').read_text()):
        p=folder/item['sheet']
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        assert ledger.get(str(p))==actual,'Contact page not yet inspected: '+str(p)
        pages.append(str(p));frames+=item['frames']
result=dict(all_contact_pages_reviewed=True,pages=len(pages),frames=len(frames),contact_pages=pages,
            scope='Both full routes, complete lunch matrix, all-actor camera, attention/save, wardrobe and cross-version save screenshots; manually inspected contact pages and selected full-size frames.')
(stage/'visual_review.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print('VISUAL_REVIEW_PASS',len(pages),'contact pages;',len(frames),'frames')
