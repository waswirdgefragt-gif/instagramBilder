"""Bildmacher: wandelt SVG- und HTML-Quelltexte in Instagram-Bilder (PNG, 1080 × 1350) um.

Aufruf:  python3 werkzeuge/bildmacher.py            (alle geänderten Quellen unter entwuerfe/)
         python3 werkzeuge/bildmacher.py --alle     (alles neu erzeugen)

Ablauf je Beitragsordner entwuerfe/<beitrag>/:
  quelle/folie_01.html | .svg  ->  bilder/folie_01.png  (1080 × 1350, gerendert mit 2-facher Auflösung, dann verkleinert)
  zusätzlich bilder/uebersicht.png (alle Folien nebeneinander) und VORSCHAU.md (zum Ansehen direkt auf GitHub).

Sicherheit: Dieses Skript lädt nichts aus dem Internet (alle Netzwerkzugriffe der Seiten werden blockiert)
und hat keinerlei Verbindung zu Instagram, Metricool oder Zapier. Es erzeugt ausschließlich Bilddateien.
"""
import hashlib, json, os, sys, glob, io
from playwright.sync_api import sync_playwright
from PIL import Image

W, H, SCALE = 1080, 1350, 2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASIS = os.path.join(ROOT, 'entwuerfe')
ALLE = '--alle' in sys.argv


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]


def quellen_im(ordner):
    q = os.path.join(ordner, 'quelle')
    return sorted(f for f in glob.glob(os.path.join(q, '*')) if f.lower().endswith(('.html', '.htm', '.svg')))


def rendere(page, quelle, ziel):
    if quelle.lower().endswith('.svg'):
        # SVG in eine HTML-Hülle einbetten (gleiche Schriften wie bei HTML, Größe 1080 × 1350)
        import tempfile, re
        svg = open(quelle, encoding='utf-8').read()
        svg = re.sub(r'<\?xml[^>]*\?>', '', svg)
        basis = 'file://' + os.path.dirname(os.path.abspath(quelle)) + '/'
        huelle = (f'<!doctype html><html><head><meta charset="utf-8"><base href="{basis}">'
                  '<style>html,body{margin:0;padding:0;width:1080px;height:1350px;overflow:hidden;background:#fff}'
                  'body>svg{width:1080px;height:1350px;display:block}</style></head><body>' + svg + '</body></html>')
        tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8'); tmp.write(huelle); tmp.close()
        url = 'file://' + tmp.name
    else:
        url = 'file://' + os.path.abspath(quelle)
    page.goto(url, wait_until='load')
    page.evaluate('document.fonts ? document.fonts.ready : null')
    page.wait_for_timeout(400)
    breite = page.evaluate('Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0)')
    hoehe = page.evaluate('Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0)')
    png = page.screenshot(clip={'x': 0, 'y': 0, 'width': W, 'height': H}, type='png')
    im = Image.open(io.BytesIO(png)).convert('RGB')
    im = im.resize((W, H), Image.LANCZOS)
    im.save(ziel, 'PNG', optimize=True)
    hinweise = []
    if breite > W + 1 or hoehe > H + 1:
        hinweise.append(f'Inhalt ist größer als 1080 × 1350 ({breite} × {hoehe}) und wurde abgeschnitten')
    return hinweise


def uebersicht(bilder, ziel):
    if not bilder: return
    ims = [Image.open(b).convert('RGB').resize((360, 450), Image.LANCZOS) for b in bilder]
    g = 16
    out = Image.new('RGB', (len(ims) * 360 + (len(ims) + 1) * g, 450 + 2 * g), (236, 240, 245))
    for i, im in enumerate(ims):
        out.paste(im, (g + i * (360 + g), g))
    out.save(ziel, 'PNG', optimize=True)


def main():
    ordner = sorted(d for d in glob.glob(os.path.join(BASIS, '*')) if os.path.isdir(os.path.join(d, 'quelle')))
    gesamt = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={'width': W, 'height': H}, device_scale_factor=SCALE)
        # kein Internet: nur lokale Dateien und eingebettete Daten
        ctx.route('**/*', lambda r: r.continue_() if r.request.url.startswith(('file:', 'data:')) else r.abort())
        page = ctx.new_page()
        for d in ordner:
            bild_dir = os.path.join(d, 'bilder'); os.makedirs(bild_dir, exist_ok=True)
            protokoll_pfad = os.path.join(bild_dir, '.quellen.json')
            protokoll = json.load(open(protokoll_pfad)) if os.path.exists(protokoll_pfad) else {}
            bilder, meldungen, neu = [], [], 0
            for q in quellen_im(d):
                name = os.path.splitext(os.path.basename(q))[0]
                ziel = os.path.join(bild_dir, name + '.png')
                h = sha(q)
                if ALLE or protokoll.get(name) != h or not os.path.exists(ziel):
                    for m in rendere(page, q, ziel):
                        meldungen.append(f'{name}: {m}')
                    protokoll[name] = h; neu += 1
                bilder.append(ziel)
            json.dump(protokoll, open(protokoll_pfad, 'w'), indent=1, sort_keys=True)
            uebersicht(bilder, os.path.join(bild_dir, 'uebersicht.png'))
            rel = os.path.relpath(d, ROOT)
            zeilen = [f'# Vorschau: {os.path.basename(d)}', '',
                      '> Automatisch erzeugt vom Bildmacher. **Entwurf – keine Freigabe zur Veröffentlichung.** Freigeben kann nur Mariam.', '',
                      '![Übersicht](bilder/uebersicht.png)', '']
            for b in bilder:
                n = os.path.basename(b)
                zeilen += [f'### {n}', f'![{n}](bilder/{n})', '']
            if meldungen:
                zeilen += ['## Hinweise des Bildmachers', ''] + [f'- {m}' for m in meldungen] + ['']
            open(os.path.join(d, 'VORSCHAU.md'), 'w').write('\n'.join(zeilen))
            print(f'{rel}: {len(bilder)} Folien, {neu} neu erzeugt' + (f' – {len(meldungen)} Hinweise' if meldungen else ''))
            gesamt += neu
        browser.close()
    print(f'Fertig: {gesamt} Bilder erzeugt.')


if __name__ == '__main__':
    main()
