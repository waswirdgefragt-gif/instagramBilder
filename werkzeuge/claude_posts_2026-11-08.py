"""Erzeugt vier neue Karussells (Claude, 08.11.2026) als HTML-Quellen + lokal gerenderte PNG (final/).
Fakten aus Kompaktbuch/Skript 2 „Das wird gefragt“ (Zahlen = Häufigkeit in Prüfungsfragen)."""
import os, shutil, html
from playwright.sync_api import sync_playwright
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(R, 'entwuerfe')

KOPF_SVG = ('<svg width="44" height="44" viewBox="0 0 40 40"><rect x="2" y="2" width="36" height="36" rx="7" fill="#fff"/>'
            '<rect x="8" y="9" width="8" height="8" rx="1.6" fill="none" stroke="#3B4B66" stroke-width="1.6"/>'
            '<path d="M7 8l10.5 10.5M17.5 7.5L7.5 17.5" stroke="#A9466A" stroke-width="2.4" stroke-linecap="round"/>'
            '<rect x="20" y="12" width="13" height="2.2" rx="1.1" fill="#C6CDD8"/><rect x="8" y="23" width="8" height="8" rx="1.6" fill="none" stroke="#3B4B66" stroke-width="1.6"/>'
            '<rect x="20" y="26" width="13" height="2.2" rx="1.1" fill="#C6CDD8"/></svg>')
CSS = '''
:root { --blau1:#C5D9F2; --blau2:#E3EDF9; --navy:#2F3E58; --rose:#A9466A; --grau:#5D6473; --rot:#C62828; }
html,body { margin:0; width:1080px; height:1350px; overflow:hidden; }
body { background:linear-gradient(180deg,var(--blau1),var(--blau2)); font-family:"Inter",sans-serif; color:var(--navy); position:relative; }
.kopf { position:absolute; top:58px; left:90px; right:90px; display:flex; justify-content:space-between; align-items:center; }
.marke { display:flex; gap:14px; align-items:center; font:700 31px "Liberation Serif",serif; }
.seite { font:600 24px "Inter"; background:#fff; border-radius:99px; padding:6px 18px; }
.inhalt { position:absolute; top:170px; left:90px; right:90px; }
.pill { display:inline-block; background:var(--rose); color:#fff; font:800 24px "Inter"; letter-spacing:.14em; padding:9px 20px; border-radius:99px; margin-bottom:28px; }
.pill.rot { background:var(--rot); }
h1 { font:900 100px/1.03 "Inter Display","Inter",sans-serif; margin:0; letter-spacing:-2px; }
h2 { font:800 58px/1.1 "Inter Display","Inter",sans-serif; margin:0 0 26px; letter-spacing:-1px; }
h1 .r, h2 .r { color:var(--rose); }
.lead { font:400 40px/1.34 "Inter"; margin:44px 0 0; }
.lead b { font-weight:700; }
.karte { background:#fff; border-radius:22px; padding:24px 30px; margin-bottom:18px; box-shadow:0 6px 18px rgba(47,62,88,.08); }
.karte h3 { font:800 33px/1.2 "Inter"; margin:0 0 6px; }
.karte p { font:400 28px/1.36 "Inter"; margin:0; color:#3C475A; }
.karte .rotz { color:var(--rot); font-weight:700; }
.karte.not { border-left:12px solid var(--rot); }
.karte.not h3 { color:var(--rot); }
.tag { display:inline-block; font:800 18px "Inter"; letter-spacing:.08em; color:#fff; background:var(--rot); border-radius:6px; padding:4px 9px; margin-right:10px; vertical-align:5px; }
.zahl { float:right; font:800 30px "Inter Display"; color:var(--rose); margin-left:16px; }
.merke { background:#F7E4EA; border-radius:22px; padding:24px 30px; font:400 30px/1.38 "Inter"; }
.merke b { color:var(--rose); }
.wisch { position:absolute; left:90px; top:1110px; background:#fff; border-radius:16px; padding:18px 30px; font:700 32px "Inter"; box-shadow:0 6px 18px rgba(47,62,88,.12); }
.fuss { position:absolute; bottom:56px; left:90px; right:90px; font:500 24px "Inter"; color:var(--grau); display:flex; justify-content:space-between; }
.rf { display:flex; gap:22px; align-items:flex-start; }
.rf .nr { flex:none; width:58px; height:58px; border-radius:50%; background:var(--navy); color:#fff; font:800 30px/58px "Inter"; text-align:center; }
.antw { font:800 30px "Inter"; }
.antw.f { color:var(--rot); } .antw.r { color:#2E7D4F; }
'''
def folie(seite, n, inhalt, fuss_rechts=''):
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="kopf"><div class="marke">{KOPF_SVG}Das wird gefragt.</div><span class="seite">{seite}/{n}</span></div>'
            f'{inhalt}<div class="fuss"><span>Schriftliche Heilpraktikerprüfung</span><span>{fuss_rechts}</span></div></body></html>')

POSTS = {}
# ---------- A: Grundlogik der Lunge ----------
A = []
A.append(('<div class="inhalt" style="top:250px"><div class="pill">LUNGE VERSTEHEN</div>'
          '<h1>Wo sitzt das Problem?<br><span class="r">Dann verstehst du die Beschwerden.</span></h1>'
          '<p class="lead">Jeder Abschnitt der Lunge hat <b>eine Aufgabe</b>. Fällt sie aus, entstehen typische Beschwerden – das erklärt fast jede Prüfungsfrage zur Atmung.</p></div>'
          '<div class="wisch">Wischen →</div>'))
mk = [('1', .3764, .3600), ('2', .3016, .5080), ('3', .786, .553), ('4', .809, .711), ('5', .891, .700), ('6', .1200, .6774)]
W, Hh = 820, 820 * 1772 / 2200
marker = ''.join(f'<div style="position:absolute;left:{x * W - 24}px;top:{y * Hh - 24}px;width:48px;height:48px;border-radius:50%;background:#2F3E58;border:3px solid #fff;color:#fff;font:800 26px/48px Inter;text-align:center">{n}</div>' for n, x, y in mk)
liste = [('1', 'Luftröhre', 'Luft durchlassen'), ('2', 'Bronchien', 'Luft verteilen und reinigen'), ('3', 'Bronchiolen', 'Luftstrom fein regeln – ohne Knorpel'),
         ('4', 'Lungenbläschen', 'Gase austauschen'), ('5', 'Lungengerüst', 'Weg für den Sauerstoff kurz halten'), ('6', 'Pleura', 'Lunge gleiten lassen, an die Brustwand koppeln')]
A.append(('<div class="inhalt" style="top:150px"><h2>Wer macht was?</h2><div style="display:flex;justify-content:center">'
          f'<div style="position:relative;width:{W}px;height:{Hh:.0f}px;border-radius:22px;overflow:hidden"><img src="grafik/lunge.png" style="width:{W}px;height:{Hh:.0f}px">{marker}</div></div>'
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 26px;margin-top:22px">'
          + ''.join(f'<div class="rf" style="gap:14px"><span class="nr" style="width:44px;height:44px;font-size:24px;line-height:44px">{n}</span><div style="font:400 26px/1.3 Inter"><b>{a}</b><br>{b}</div></div>' for n, a, b in liste)
          + '</div></div>'))
A.append(('<div class="inhalt"><div class="pill">1–3 · ATEMWEGE</div><h2>Die Luft kommt<br><span class="r">schlecht durch.</span></h2>'
          '<div class="karte"><h3>Luftröhre und Kehlkopf eng</h3><p>z. B. Fremdkörper, Pseudokrupp: <b>Stridor</b> – pfeifendes Geräusch beim <b>Einatmen</b></p></div>'
          '<div class="karte"><h3>Bronchien und Bronchiolen eng</h3><p>z. B. Asthma, COPD: <b>Giemen</b> und verlängerte <b>Ausatmung</b>. Bronchiolen haben keinen Knorpel – sie verengen sich besonders leicht.</p></div>'
          '<div class="karte"><h3>Wohin rutscht ein Fremdkörper?</h3><p>Meist in den <b>rechten</b> Hauptbronchus – er verläuft steiler und ist weiter. <span class="zahl">2×</span></p></div>'
          '<div class="merke"><b>Merke:</b> Einatmen pfeift → oben eng. Ausatmen pfeift → unten eng.</div></div>'))
A.append(('<div class="inhalt"><div class="pill">4–5 · BLÄSCHEN UND GERÜST</div><h2>Der Gasaustausch<br><span class="r">ist gestört.</span></h2>'
          '<div class="karte"><h3>Bläschen voller Flüssigkeit</h3><p>Pneumonie, Lungenödem: <b>feuchte Rasselgeräusche</b>; beim Lungenödem Atemnot im Liegen, schaumiger Auswurf. <span class="zahl">6×</span></p></div>'
          '<div class="karte"><h3>Bläschenwände zerstört</h3><p>Lungenemphysem: weniger Austauschfläche, die Lunge ist überbläht, Luft bleibt beim Ausatmen gefangen.</p></div>'
          '<div class="karte"><h3>Gerüst vernarbt</h3><p>Lungenfibrose, Silikose: Die Wand zwischen Luft und Blut wird dicker – der Sauerstoff kommt schlechter ins Blut, die Lunge wird steif.</p></div>'
          '<div class="merke"><b>Merke:</b> Rasseln = Flüssigkeit in den Bläschen. Steife Lunge = Narben im Gerüst.</div></div>'))
A.append(('<div class="inhalt"><div class="pill">6 · PLEURA</div><h2>Die Lunge kann sich<br><span class="r">nicht entfalten.</span></h2>'
          '<div class="karte"><h3>Pleuraerguss</h3><p>Flüssigkeit im Pleuraspalt: Klopfschall <b>gedämpft</b>, Atemgeräusch abgeschwächt. <span class="zahl">7×</span></p></div>'
          '<div class="karte"><h3>Pneumothorax</h3><p>Luft im Pleuraspalt: Klopfschall <b>hypersonor</b>, Atemgeräusch einseitig abgeschwächt. <span class="zahl">8×</span></p></div>'
          '<div class="karte not"><h3><span class="tag">NOTFALL</span>Spannungspneumothorax</h3><p>Ventil: Luft strömt hinein, nicht hinaus – Herz und Gefäße werden verdrängt. <span class="rotz">Verdacht → 112</span></p></div>'
          '<div class="merke"><b>Merke:</b> Ort → was dort schiefgeht → welche Beschwerde. So musst du weniger auswendig lernen.</div></div>'))
POSTS['claude-2026-11-lunge-grundlogik'] = (A, 'Zahl = so oft in 52 Prüfungen gefragt')

# ---------- B: Notfälle der Atemwege ----------
B = []
B.append(('<div class="inhalt" style="top:250px"><div class="pill rot">NOTFALL</div>'
          '<h1>Atemnot:<br><span class="r">Wann sofort 112?</span></h1>'
          '<p class="lead">Sieben Notfälle der Atemwege, die in der Heilpraktikerprüfung immer wieder gefragt werden – und woran du sie erkennst.</p></div>'
          '<div class="wisch">Wischen →</div>'))
B.append(('<div class="inhalt"><div class="pill">OBERE ATEMWEGE</div><h2>Kehlkopf, Luftröhre</h2>'
          '<div class="karte not"><h3><span class="tag">NOTFALL</span>Epiglottitis</h3><p>Kind mit hohem Fieber, Speichelfluss, kloßiger Sprache, sitzt vorgebeugt. <span class="rotz">Verdacht → 112. Nicht in den Rachen schauen!</span></p></div>'
          '<div class="karte"><h3>Pseudokrupp</h3><p>Bellender Husten, Stridor, meist nachts nach Erkältung. <span class="rotz">Atemnot, Einziehungen, Blaufärbung → 112</span></p></div>'
          '<div class="karte"><h3>Eingeatmeter Fremdkörper</h3><p>Plötzlich beim Essen oder Spielen, ohne Fieber. Hustet er wirksam: weiterhusten lassen. <span class="rotz">Husten unwirksam → 112, bis zu 5 Rückenschläge, dann bis zu 5 Oberbauchkompressionen (Säugling: Brustkorb)</span></p></div></div>'))
B.append(('<div class="inhalt"><div class="pill">UNTERE ATEMWEGE UND LUNGE</div><h2>Bronchien, Lunge, Pleura</h2>'
          '<div class="karte"><h3>Schwerer Asthmaanfall</h3><p>Kann kaum sprechen, Blaufärbung, Erschöpfung; im schwersten Fall fehlt das Giemen („stille Lunge“). <span class="rotz">→ 112</span></p></div>'
          '<div class="karte not"><h3><span class="tag">NOTFALL</span>Spannungspneumothorax</h3><p>Zunehmende Atemnot, gestaute Halsvenen, Herzrasen. <span class="rotz">Verdacht → 112</span></p></div>'
          '<div class="karte not"><h3><span class="tag">NOTFALL</span>Lungenembolie</h3><p>Plötzliche Atemnot, Brustschmerz beim Atmen, Herzrasen, oft nach OP oder Bettlägerigkeit. <span class="rotz">Verdacht → 112</span> <span class="zahl">9×</span></p></div>'
          '<div class="karte not"><h3><span class="tag">NOTFALL</span>Lungenödem</h3><p>Atemnot im Liegen, Rasseln, schaumiger Auswurf. <span class="rotz">Verdacht → 112</span> <span class="zahl">6×</span></p></div></div>'))
B.append(('<div class="inhalt"><div class="pill">SO HANDELST DU</div><h2>Bis der Rettungs­dienst kommt</h2>'
          '<div class="karte"><h3>Oberkörper hoch</h3><p>Asthma: aufrecht sitzen, Arme abstützen (Kutschersitz). Lungenödem: Beine herabhängen lassen (Herzbettlage).</p></div>'
          '<div class="karte"><h3>Beruhigen, nicht allein lassen</h3><p>Enge Kleidung lockern, eigenes Notfallspray anwenden lassen, Atmung und Kreislauf beobachten.</p></div>'
          '<div class="karte"><h3>Bei Epiglottitis: nichts in den Mund</h3><p>Kein Spatel, nicht flach hinlegen – das Kind sitzen lassen, wie es am besten Luft bekommt.</p></div>'
          '<div class="merke"><b>Merke:</b> Bei Atemnot entscheidet die Lagerung – fast immer gilt: Oberkörper hoch.</div></div>'))
POSTS['claude-2026-11-notfaelle-atemwege'] = (B, 'Zahl = so oft in 52 Prüfungen gefragt')

# ---------- C: Quiz ----------
Q = [('Der Pleuraspalt ist beim Gesunden mit Luft gefüllt.', False, 'Er enthält nur wenige Milliliter Gleitflüssigkeit – und keine Luft.', None),
     ('Über einem Pleuraerguss ist der Klopfschall hypersonor.', False, 'Gedämpft! Hypersonor klingt es über Luft: Pneumothorax, Emphysem.', '7×'),
     ('Die rechte Lunge hat drei Lappen, die linke zwei.', True, 'Links ist weniger Platz – dort liegt das Herz.', '3×'),
     ('Eine Lungenembolie entsteht meist aus Gerinnseln der tiefen Bein- oder Beckenvenen.', True, 'Das Gerinnsel wandert über die untere Hohlvene und das rechte Herz in die Lungenarterie.', '12×'),
     ('Fieber ist ein typisches Akutzeichen der Lungenembolie.', False, 'Typisch sind plötzliche Atemnot, schnelle Atmung, Herzrasen, atemabhängiger Brustschmerz.', '9×')]
C = []
C.append(('<div class="inhalt" style="top:250px"><div class="pill">PRÜFUNGSWISSEN</div>'
          '<h1>Richtig<br><span class="r">oder falsch?</span></h1>'
          '<p class="lead">Fünf Aussagen zur Lunge – alle so oder ähnlich in der schriftlichen Heilpraktikerprüfung gefragt. Merk dir deine Antworten, die Auflösung kommt am Ende.</p></div>'
          '<div class="wisch">Wischen →</div>'))
C.append(('<div class="inhalt"><h2>Was meinst du?</h2>'
          + ''.join(f'<div class="karte rf"><span class="nr">{i + 1}</span><p style="font:500 32px/1.35 Inter;color:#2F3E58">{html.escape(t)}</p></div>' for i, (t, *_ ) in enumerate(Q))
          + '<div class="merke" style="margin-top:6px">Richtig oder falsch? <b>Auflösung → nächste Folie</b></div></div>'))
C.append(('<div class="inhalt" style="top:150px"><h2>Auflösung</h2>'
          + ''.join(f'<div class="karte rf" style="padding:18px 26px"><span class="nr">{i + 1}</span><div><span class="antw {"r" if ok else "f"}">{"Richtig" if ok else "Falsch"}</span>{(" <span class=zahl style=float:none;margin-left:14px>" + z + "</span>") if z else ""}<p style="margin-top:4px">{html.escape(erk)}</p></div></div>' for i, (t, ok, erk, z) in enumerate(Q))
          + '</div>'))
POSTS['claude-2026-11-quiz-lunge'] = (C, 'Zahl = so oft in 52 Prüfungen gefragt')

# ---------- D: Prüfungsfalle Niederdrucksystem ----------
D = []
D.append(('<div class="inhalt" style="top:250px"><div class="pill">PRÜFUNGSFALLE</div>'
          '<h1>Arterie =<br><span class="r">Hochdruck?</span></h1>'
          '<p class="lead">Klingt logisch – ist aber eine der beliebtesten Fallen der Prüfung. <b>Gehört die Lungenarterie zum Hoch- oder zum Niederdrucksystem?</b></p></div>'
          '<div class="wisch">Wischen →</div>'))
D.append(('<div class="inhalt"><div class="pill">DIE AUFLÖSUNG</div><h2>Die Lungenarterie gehört<br><span class="r">zum Niederdrucksystem.</span></h2>'
          '<div class="karte"><h3>Niederdrucksystem</h3><p>Alle Venen (auch die Pfortader), das rechte Herz, der ganze Lungenkreislauf – also auch die Lungenarterie – und der linke Vorhof. Hier liegen rund 85 % des Blutes. <span class="zahl">3×</span></p></div>'
          '<div class="karte"><h3>Hochdrucksystem</h3><p>Die linke Kammer (während sie auswirft), die Aorta und die Arterien des Körperkreislaufs.</p></div>'
          '<div class="merke"><b>Merke:</b> Nicht der Name „Arterie“ entscheidet, sondern der Druck darin.</div></div>'))
D.append(('<div class="inhalt"><div class="pill">WARUM IST DAS SO?</div><h2>Hoher Druck<br><span class="r">nur, wo er nötig ist.</span></h2>'
          '<div class="karte"><h3>Körperkreislauf</h3><p>Das Blut muss bis in die Zehenspitzen – dafür braucht es hohen Druck und eine kräftige linke Kammer mit dicker Wand.</p></div>'
          '<div class="karte"><h3>Lunge</h3><p>Der Weg ist kurz, und in den Bläschen braucht der Gasaustausch einen ruhigen Blutfluss. Hoher Druck würde Flüssigkeit in die Bläschen pressen – wie beim Lungenödem.</p></div>'
          '<div class="karte"><h3>Deshalb</h3><p>ist die Wand der rechten Kammer dünner als die der linken, und die Vorhöfe sind noch dünner.</p></div></div>'))
POSTS['claude-2026-11-niederdrucksystem'] = (D, 'Zahl = so oft in 52 Prüfungen gefragt')

if __name__ == '__main__':
    lunge = '/tmp/claude-0/-home-claude/b2aa2457-44e0-5bd9-8541-10933726e0e5/scratchpad/uebers/s2p5-000.png'
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for ordner, (folien, fr) in POSTS.items():
            q = os.path.join(E, ordner, 'quelle'); f = os.path.join(E, ordner, 'final'); os.makedirs(q, exist_ok=True); os.makedirs(f, exist_ok=True)
            if 'grundlogik' in ordner:
                os.makedirs(os.path.join(q, 'grafik'), exist_ok=True)
                from PIL import Image
                Image.open(lunge).convert('RGB').resize((1100, 886)).save(os.path.join(q, 'grafik', 'lunge.png'))
            for i, inh in enumerate(folien, 1):
                p = os.path.join(q, f'folie_{i:02d}.html')
                open(p, 'w', encoding='utf-8').write(folie(i, len(folien), inh, fr if i > 1 else ''))
                pg.goto('file://' + p); pg.wait_for_timeout(250)
                ueber = pg.evaluate('() => [...document.querySelectorAll(".inhalt")].map(e => e.getBoundingClientRect().bottom)')
                pg.screenshot(path=os.path.join(f, f'folie_{i:02d}.png'))
                print(ordner, i, 'Inhalt bis', [round(u) for u in ueber], '(Grenze ~1270)')
        br.close()
