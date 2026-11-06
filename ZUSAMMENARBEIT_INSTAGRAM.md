# Zusammenarbeit an Instagram-Beiträgen: Mariam, Claude und ChatGPT

**Oberste Regel:** Claude und ChatGPT dürfen Entwürfe erstellen, gegenseitig prüfen und Empfehlungen geben. **Freigeben darf nur Mariam.** Ohne ihre ausdrückliche Zustimmung zu genau diesem Beitrag wird nichts bei Instagram oder Metricool veröffentlicht oder eingeplant. Auch eine Empfehlung von Claude oder ChatGPT ersetzt diese Zustimmung nicht.

## Technische Lage (geprüft am 7.11.2026)

| | Claude | ChatGPT |
|---|---|---|
| Text-Dateien (Markdown, HTML, SVG, JSON) schreiben | ja | ja (die README in `chatgpt_entwuerfe` stammt von ChatGPT) |
| Bilder und GIFs (Binärdateien) hochladen | ja | derzeit nein |
| Workflow-Dateien (GitHub Actions) anlegen | ja | unbekannt |
| Dateien oder Zweige löschen | nein (Zugriff gesperrt) | – |

## Vorgeschlagener Ablauf: Entwürfe als Quelltext

Bilder von ChatGPT kommen nicht direkt ins Repository. Deshalb **speichert ChatGPT jede Grafik als Quelltext**, also als HTML/CSS oder SVG. Das ist reiner Text, und den kann ChatGPT schreiben. Ein **automatischer Bildmacher** (GitHub Action) erzeugt daraus bei jedem Hochladen die fertigen Bilder.

```
entwuerfe/
  2026-11-arterieller-verschluss/
    quelle/           <- ChatGPT oder Claude legt HTML/SVG ab (je Folie eine Datei)
    bilder/           <- wird automatisch erzeugt: folie_01.png … (1080 × 1350)
    pruefung.md       <- Prüfung und Empfehlungen der jeweils anderen KI
    STATUS.md         <- Entwurf / geprüft / FREIGEGEBEN (nur Mariam setzt FREIGEGEBEN)
```

- **Animationen:** HTML/CSS-Animationen werden auf dieselbe Weise automatisch zu MP4 bzw. GIF.
- **KI-Bilder** (gemalte Illustrationen aus einem Bildgenerator) lassen sich so nicht abbilden. Dafür gibt es eine Ausnahme: Mariam lädt die Datei **einmal** direkt auf GitHub hoch, über *Add file → Upload files* im richtigen Ordner, auch vom Handy-Browser aus. Ein Umweg über den anderen Chat ist nicht nötig.
- **Prüfung:** Die andere KI liest den Ordner und schreibt ihre Rückmeldung in `pruefung.md`. Überarbeitungen kommen als **neue** Dateien dazu (`folie_02_v2.html`). Originale werden nie überschrieben.
- **Freigabe:** Mariam schaut sich die Bilder in `bilder/` an und sagt im Chat ausdrücklich „Beitrag X freigegeben“. Erst dann darf veröffentlicht oder eingeplant werden.

## Markenstil (Leitplanken, keine Gleichmacherei)

- Pastellblauer Hintergrund, dunkelblaue Typografie (Navy), Rosé bzw. Altrosa als Akzent.
- Hochwertiger Fachbuchstil der Reihe „Das wird gefragt – Heilpraktikerwissen mit Durchblick“.
- Wenig Deko, kein Pergament- oder Vintage-Look.
- Fußzeile „Schriftliche Heilpraktikerprüfung“, kein Name auf den Folien.
- Claude und ChatGPT dürfen eigene Handschriften behalten. Geprüft wird auf fachliche Richtigkeit und darauf, dass der Beitrag erkennbar zur Reihe gehört, nicht auf identische Gestaltung.

## Hinweis

Dieses Repository ist **öffentlich**, weil Instagram die Bilder über öffentliche Links abruft. Entwürfe sind damit für jeden mit dem Link sichtbar. Sollen Entwürfe vertraulich bleiben, können sie in einem privaten Repository liegen. Dann werden nur freigegebene Bilder hierher kopiert.
