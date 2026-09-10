from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
tex = (ROOT / 'paper' / 'main.tex').read_text()
claims = (ROOT / 'claims' / 'claims.yaml').read_text()
zenodo = json.loads((ROOT / 'zenodo.json').read_text())
required = ['\\begin{abstract}', '\\section{Introduction', '\\section{Limitations', '\\section{Conclusion', '\\bibliography{references}']
missing = [x for x in required if x not in tex]
if missing:
    raise SystemExit(f'missing manuscript markers: {missing}')
if 'publication_authorized: false' not in claims:
    raise SystemExit('publication guard missing')
if zenodo.get('publication_status') != 'not_published' or zenodo.get('external_identifier') is not None:
    raise SystemExit('zenodo template is not fail-closed')
if '\\citep{' not in tex:
    raise SystemExit('no citations found')
print('validation: PASS')
print(f'manuscript_bytes: {len(tex.encode())}')
print(f'claim_lines: {len(claims.splitlines())}')
print('publication_status: not_published')
