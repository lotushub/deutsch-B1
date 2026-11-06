"""Build a standalone offline HTML file from the authored sources (Python 3)."""
from pathlib import Path
root = Path(__file__).resolve().parent
html = (root / 'src/template.html').read_text(encoding='utf-8')
script = (root / 'src/app.js').read_text(encoding='utf-8')
if '</script' in script.lower():
    raise SystemExit('Inline script contains an HTML closing script tag; escape it first.')
(root / 'index.html').write_text(html.replace('__APP_SCRIPT__', script), encoding='utf-8')
print('Built index.html — ready to open offline.')
