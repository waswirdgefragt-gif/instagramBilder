# Zusammenarbeit an Instagram-Beiträgen: Mariam, Claude und ChatGPT

**Oberste Regel:** Claude und ChatGPT dürfen Entwürfe erstellen, gegenseitig prüfen und Empfehlungen geben. **Freigeben darf nur Mariam.** Ohne ihre ausdrückliche Zustimmung zu genau diesem Beitrag wird nichts bei Instagram oder Metricool veröffentlicht oder eingeplant. Auch eine Empfehlung von Claude oder ChatGPT ersetzt diese Zustimmung nicht.

## Technische Lage (geprüft am 7.11.2026)

| | Claude | ChatGPT |
|---|---|---|
| Text-Dateien (Markdown, HTML, SVG, JSON) schreiben | ja | ja (die README in `chatgpt_entwuerfe` stammt von ChatGPT) |
| Bilder und GIFs (Binärdateien) hochladen | ja | derzeit nein |
| Workflow-Dateien (GitHub Actions) anlegen | ja | unbekannt (nicht nötig) |
| Dateien oder Zweige löschen | nein (Zugriff gesperrt) | – |

## Ablauf (seit 7.11.2026 eingerichtet und getestet)

ChatGPT und Claude speichern jede Folie als **Quelltext** (HTML oder SVG). Der **Bildmacher** (GitHub Action `.github/workflows/bildmacher.yml`) erzeugt daraus nach jedem Hochladen automatisch die fertigen Bilder und eine Vorschauseite. Niemand muss Dateien zwischen den Chats übertragen.

### Ordner und Dateinamen

```
entwuerfe/
  <autor>-<JJJJ-MM>-<thema>/          z. B. chatgpt-2026-11-arterieller-verschluss, claude-2026-11-luft-ohne-blut
    quelle/
      folie_01.html  oder  folie_01.svg  (je Folie eine Datei, zweistellig nummeriert)
      folie_02_v2.html                   (Überarbeitung = neue Datei, Original bleibt)
      bilder_hilfe/…                     (optional: eingebettete Grafiken, nur relative Pfade)
    bilder/                              <- AUTOMATISCH: folie_01.png … (1080 × 1350) und uebersicht.png
    VORSCHAU.md                          <- AUTOMATISCH: alle Bilder zum Ansehen direkt auf GitHub
    STATUS.md                            <- Status, Prüfung, Änderungsprotokoll (von Hand)
    pruefung_claude.md / pruefung_chatgpt.md   <- Rückmeldung der jeweils anderen KI
vorlagen/   beispiel_folie.html, beispiel_folie.svg (Startpunkt, frei veränderbar)
werkzeuge/  bildmacher.py, schriften/ (Inter, Inter Display, Liberation Serif; Emoji wird ergänzt)
```

In `bilder/` und `VORSCHAU.md` bitte nichts von Hand ändern, sie werden bei jeder Änderung der Quelle neu erzeugt.

### Regeln für Quelltexte

- **Format:** Die Fläche ist genau 1080 × 1350 Pixel. In HTML `html,body{width:1080px;height:1350px;margin:0;overflow:hidden}` setzen. In SVG `width="1080" height="1350" viewBox="0 0 1080 1350"`.
- **Schriften:** `Inter`, `Inter Display` und `Liberation Serif`. Emojis sind möglich. Andere Schriften stehen nicht zur Verfügung, und es wird ersatzweise eine Standardschrift genommen.
- **Keine Internet-Inhalte:** Keine Google Fonts, keine Bilder von fremden Seiten, keine Skripte aus dem Netz. Der Bildmacher blockiert alle Netzzugriffe. Bilder entweder als Datei im Ordner `quelle/` mit relativem Pfad oder direkt als `data:`-Adresse einbetten.
- **Inhalt, der über die Fläche hinausragt,** wird abgeschnitten. Der Bildmacher meldet das in `VORSCHAU.md`.
- **Animationen** (HTML/CSS) sind der nächste Schritt und noch nicht eingerichtet.

### Ablauf in drei Schritten

1. **Erstellen:** ChatGPT oder Claude legt einen neuen Beitragsordner mit Quelltexten und `STATUS.md` an. Nach etwa 2–3 Minuten erscheinen `bilder/` und `VORSCHAU.md`.
2. **Gegenseitig prüfen:** Die andere KI liest Quelltext und Vorschau und schreibt `pruefung_<ki>.md` (fachlich, Layout, Markenstil). Verbesserungen kommen als neue Dateien (`_v2`). Jede Änderung wird in `STATUS.md` unter „Änderungen“ vermerkt.
3. **Freigabe:** Mariam schaut sich `VORSCHAU.md` an. Nur sie trägt in `STATUS.md` „FREIGEGEBEN“ ein oder sagt es ausdrücklich im Chat. Erst dann darf veröffentlicht oder eingeplant werden.

**KI-Bilder** (gemalte Illustrationen aus einem Bildgenerator) können nicht als Quelltext gespeichert werden. Mariam gibt sie an Claude weiter, und Claude legt sie in `quelle/grafik/` ab. Alternativ lädt Mariam sie selbst über *Add file → Upload files* hoch. Den Ablauf beschreibt der nächste Abschnitt.

### Anatomie-Grafiken von ChatGPT (fester Ablauf seit 7.11.2026, Festlegung Mariam)

**Rollen:**
- **ChatGPT** liefert die anatomischen Illustrationen und die inhaltlichen Ideen.
- **Claude** prüft unabhängig und baut die Grafik in Post, Karussell oder Reel ein.

**Ablauf:**
1. ChatGPT erstellt die Grafik im Chat. Mariam gibt sie an Claude weiter.
2. Claude legt die Originaldatei **unverändert** in `quelle/grafik/` ab. Bei einer neuen Fassung kommt eine neue Datei mit `_v2` dazu.
3. Claude prüft und schreibt das Ergebnis in `pruefung_anatomie_claude.md`, mit internen Quellen nach `QUELLENREGELN`. Geprüft werden:
   - **anatomische Korrektheit:** Seitenverhältnisse, Lagebeziehungen, rechts und links aus Sicht des Betrachters, Lappen, Fissuren, Herzbucht, Bronchien, Gefäße,
   - **fachliche Aussage:** Stützt die Grafik wirklich die Aussage des Beitrags?
   - **didaktische Verständlichkeit,**
   - **Eignung für Heilpraktiker-Posts.**
4. **Bei Fehlern:**
   - Jeden Fehler konkret benennen.
   - Einen Korrekturvorschlag als Prompt für ChatGPT formulieren.
   - Möglichst auf die korrigierte Grafik warten. Sonst nur mit klar dokumentierten Änderungen weiterbauen.
5. **Einbau:** Claude baut die Grafik in HTML-Folien ein (`<img src="grafik/…">`).
   - Erlaubt sind Zuschneiden, Skalieren, Einbetten und die Kombination mit Text und Layout.
   - Nicht erlaubt ist, die Grafik ohne Grund neu zu interpretieren oder durch eine schwächere SVG-Skizze zu ersetzen.
6. **Freigabe:** wie oben, ausschließlich durch Mariam.

**Technischer Hinweis:** Der Bildmacher erkennt nur Änderungen an den Folien-Quelltexten. Eine überarbeitete Grafik bekommt daher immer einen neuen Dateinamen (`_v2`), und die Folie wird als neue Fassung angelegt.

### Sicherheit

Der Bildmacher erzeugt ausschließlich Bilddateien. Er nutzt keine Zugangsdaten und ist mit Instagram, Metricool oder Zapier nicht verbunden. Er kann also nichts veröffentlichen oder einplanen.

## Markenstil (Leitplanken, keine Gleichmacherei)

- Pastellblauer Hintergrund, dunkelblaue Typografie (Navy), Rosé bzw. Altrosa als Akzent.
- Hochwertiger Fachbuchstil der Reihe „Das wird gefragt – Heilpraktikerwissen mit Durchblick“.
- Wenig Deko, kein Pergament- oder Vintage-Look.
- Fußzeile „Schriftliche Heilpraktikerprüfung“, kein Name auf den Folien.
- Claude und ChatGPT dürfen eigene Handschriften behalten. Geprüft wird auf fachliche Richtigkeit und darauf, dass der Beitrag erkennbar zur Reihe gehört, nicht auf identische Gestaltung.

## Hinweis

Dieses Repository ist **öffentlich**, weil Instagram die Bilder über öffentliche Links abruft. Entwürfe sind damit für jeden mit dem Link sichtbar. Sollen Entwürfe vertraulich bleiben, können sie in einem privaten Repository liegen. Dann werden nur freigegebene Bilder hierher kopiert.
