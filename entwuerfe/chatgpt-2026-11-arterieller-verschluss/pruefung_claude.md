# Prüfung durch Claude – „Akuter arterieller Verschluss“ (ChatGPT-Entwurf)

Stand: 07.11.2026 · geprüft: `quelle/folie_01.svg` bis `folie_03.svg`, Caption-Entwurf in `STATUS.md` und `quellenpruefung.md`.
**Keine Freigabe.** Dies ist eine Empfehlung. Freigeben kann nur Mariam.

## Gesamturteil

- **Fachlich:** Alle Aussagen sind richtig, und die Lösung C stimmt. Es fehlen aber zwei Dinge, die in der Heilpraktikerprüfung regelmäßig gefragt werden: die **Lagerung** (Bein tief, polstern, weder wärmen noch kühlen) und die **Abgrenzung zur Venenthrombose**. Beides habe ich in `_v2` ergänzt.
- **Gestaltung:** Der Entwurf ist sauber und gut lesbar und hat eine eigene, ruhige Handschrift. Er wirkt aber eher **weiß als pastellblau**, und einige kleine Schriften sind auf dem Handy zu klein.
- **Empfehlung:** Mit den `_v2`-Folien halte ich den Beitrag fachlich und gestalterisch für **veröffentlichungsreif, vorbehaltlich Mariams Freigabe**. Die Originalfolien würde ich so nicht veröffentlichen, weil Lagerung und Abgrenzung fehlen.

## 1. Technik (Bildmacher)

Alle drei SVG-Dateien rendern fehlerfrei auf 1080 × 1350. Die Schriften Inter und Liberation Serif werden korrekt geladen, nichts ist abgeschnitten.

Hinweis zum Ablauf: ChatGPT hat die Dateien einzeln hochgeladen. Dadurch startet der Bildmacher mehrmals hintereinander, und die Bilder von Folie 2 und 3 erscheinen erst nach dem letzten Durchlauf. Besser ist es, alle Dateien eines Beitrags in **einem** Commit hochzuladen.

## 2. Fachliche Prüfung

| Aussage | Bewertung | Belege |
|---|---|---|
| Plötzlich blass, kalt, sehr schmerzhaft → akuter arterieller Verschluss (Lösung C) | ✅ richtig | ESVS 2020 (Björck et al., DOI 10.1016/j.ejvs.2019.09.006); Callum & Bradbury, BMJ 2000; MSD Manual „Periphere arterielle Verschlusskrankheit“; Fragenbuch 1.14.15 |
| Ablenker A (Erysipel) und B (TVT) | ✅ sinnvoll gewählt | Fragenbuch 1.14.15 (TVT: Bein schwillt an, kann bläulich werden), 4.8 (Wundrose: scharf begrenzte Rötung, oft Fieber) |
| „Zeitkritischer Notfall – bei Verdacht Notruf 112“ | ✅ richtig | ESC 2024 PAAD-Leitlinie (Abschnitt akute Extremitätenischämie); Fragenbuch 1.14.15 und 1.14.14 (BMJ 2000, MSD) |
| Warnzeichen: Schmerz, blass/kalt, fehlender oder schwacher Puls, Gefühlsstörung oder Lähmung | ✅ richtig (Auswahl aus den „6 P“) | ESVS 2020; BMJ 2000 |
| „Weniger Durchblutung bedeutet weniger Sauerstoff und Wärme“ | ✅ richtig, stark vereinfacht | – |
| `quellenpruefung.md`, Punkt 4 (Notruf 112 nur „redaktionell“) | ✅ jetzt belegt | Fragenbuch 1.14.15 / 1.14.14, gestützt auf BMJ 2000, MSD Manual (Patienten- und Profiausgabe), ESVS 2020 |
| **Fehlt:** Lagerung und Erstmaßnahmen | ⚠️ prüfungsrelevant | Fragenbuch 1.14.14: Bein tief lagern, mit Watte polstern bzw. locker einhüllen, nicht laufen lassen, weder kühlen noch erwärmen, keine Kompression, keine Spritze in den Muskel (ESVS 2020, MSD, Uniklinik Linz, S2k-Leitlinie Kompressionstherapie) |
| **Fehlt:** Farbe allein entscheidet nicht | ⚠️ typische Prüfungsfalle | Fragenbuch 1.14.15: Hält der Verschluss an, wird die Haut fleckig-bläulich (marmoriert) |
| Merkkasten Folie 3 („Plötzlich blass + kalt + Schmerz“) | ⚠️ unvollständig | Die Konsequenz fehlt. Ergänzt um „→ Notruf 112“. |
| Schema Folie 3 | ⚠️ missverständlich | Das Gefäß ist vor und hinter dem Verschluss gleich gefärbt. Der gestrichelte blaue Strich unter dem Gerinnsel sieht aus wie ein Tropfen und zeigt nicht „weniger Blutfluss“. |

**Caption:** Fachlich richtig. Ein Vorschlag: ergänzen „Bein tief lagern und polstern, nicht wärmen oder kühlen.“ Und „Notfallmedizin“ als Hashtag eher durch #Heilpraktikerausbildung ersetzen, das passt besser zur Zielgruppe.

## 3. Gestaltung im Vergleich zu `post01_v3` und `post02_v2`

| Punkt | Befund | Vorschlag |
|---|---|---|
| Hintergrund | Sehr helles Blau (#E5F1F9) mit fast weißer Karte; wirkt weiß, nicht pastellblau | Pastellblauer Verlauf (#C5D9F2 → #E3EDF9) als Rahmen um die weiße Karte. So bleibt ChatGPTs Karten-Handschrift erhalten und die Reihe ist erkennbar (in `_v2` umgesetzt). |
| Farben | Navy #263E58 und Altrosa #AF5979 passen gut | beibehalten |
| Typografie | Überschriften Inter 600, ruhig und sachlich; in unseren Beiträgen sind sie kräftiger (Inter Display Black) | Kann als eigene Handschrift bleiben. Für mehr Wirkung im Feed wäre Folie 1 mit Gewicht 800 stärker. |
| Kleine Schriften | Unterzeile „Heilpraktikerwissen mit Durchblick“ 18 px, Fußzeile 19 px: auf dem Handy etwa 6 pt, kaum lesbar | mindestens 22 px (in `_v2` umgesetzt) |
| Kopf „Das wird gefragt.“ | 54 px plus Unterzeile, belegt viel Platz auf jeder Folie | Möglich, aber unsere Beiträge nutzen einen kleinen Kopf mit Logo. Für ein einheitlicheres Bild 31–36 px mit Logo-Symbol. Nicht geändert, weil es ChatGPTs Handschrift ist. |
| Karussell-Aufbau | Frage → Auflösung → Warum: klar und gut, mit Wisch-Hinweisen | sehr gut; mit Lagerung und TVT-Abgrenzung inhaltlich vollständiger |
| Lesbarkeit | Kontraste gut, Zeilenlängen gut, nichts abgeschnitten | – |

## 4. Neue Versionen (Originale unverändert)

- `quelle/folie_01_v2.svg`: pastellblauer Rahmen, kleine Schriften auf 22 px.
- `quelle/folie_02_v2.svg`: dazu der Notfallkasten mit Erstmaßnahmen: „Notruf 112 · Bein tief lagern und weich polstern, nicht laufen lassen, weder wärmen noch kühlen“.
- `quelle/folie_03_v2.svg`:
  - neues Schema mit Blutflusspfeil, vor dem Verschluss kräftig rot, dahinter blass („dahinter: kaum Blut → blass, kalt, Schmerz“),
  - Satz zur fleckig-bläulichen Haut bei anhaltendem Verschluss,
  - kurzer Vergleich mit der Venenthrombose,
  - Merksatz mit „→ Notruf 112“.

Alle neuen Aussagen stammen aus geprüften Antworten des Fragenbuchs (1.14.14, 1.14.15) und den dort genannten Quellen.

## Quellen

- European Society for Vascular Surgery (ESVS): 2020 Clinical Practice Guidelines on the Management of Acute Limb Ischaemia. Eur J Vasc Endovasc Surg 2020;59:173–218. https://doi.org/10.1016/j.ejvs.2019.09.006
- ESC 2024 Guidelines for the management of peripheral arterial and aortic diseases. Eur Heart J 2024;45(36):3538–3700. https://pubmed.ncbi.nlm.nih.gov/39210722/
- Callum K, Bradbury A. ABC of arterial and venous disease: Acute limb ischaemia. BMJ 2000;320:764–767. https://www.bmj.com/content/320/7237/764
- MSD Manual, Ausgabe für Patienten: Periphere arterielle Verschlusskrankheit (plötzlicher Verschluss).
- MSD Manual, Ausgabe für medizinische Fachkreise: Periphere arterielle Verschlusskrankheit (Jones WS, 2025/2026).
- Fragenbuch „Das wird gefragt – Fragen & Antworten“, Kapitel 1.14 (Stand 07.11.2026, unabhängig geprüft).
