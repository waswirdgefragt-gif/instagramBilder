# Grafik-Aufträge an ChatGPT

Hier legt Claude die Prompts für anatomische Illustrationen ab. ChatGPT holt sie sich hier selbstständig, erzeugt die Bilder in seinem Chat und liefert sie zurück.
**Festlegung Mariam (07.11.2026):** ChatGPT zeichnet die Anatomie. Claude prüft unabhängig und baut die Grafik in den Post ein. Freigabe nur durch Mariam.

## Ordner

```
grafik-auftraege/
  offen/      Aufträge, die ChatGPT bearbeiten soll (je Grafik eine Datei)
  erledigt/   abgeschlossene Aufträge (Claude verschiebt sie nach der Prüfung hierher)
```

**Dateiname:** `JJJJ-MM-TT_<thema>.md`, z. B. `2026-11-07_bronchien-fremdkoerper.md`

## Aufbau eines Auftrags

1. **Kopf:** Status (`offen`, `in Arbeit`, `geliefert`, `Korrektur nötig`, `angenommen`), zugehöriger Beitragsordner, Lieferdateiname.
2. **Bild-Prompt:** zum direkten Kopieren in den Bildgenerator.
3. **Anatomische Prüfpunkte:** daran prüft Claude.
4. **Quellen:** für die interne Prüfung, nicht für den Post.

## Regeln für die Grafik

- **Keine Schrift im Bild.** Beschriftungen, Überschriften und Pfeile mit Text setzt Claude im Layout, denn KI-Bilder schreiben oft falsch.
- **Hintergrund** hell und ruhig, am besten einfarbig pastellblau oder weiß, damit die Grafik sauber freigestellt und eingebettet werden kann.
- **Hochformat** oder quadratisch, mindestens 1024 Pixel auf der kurzen Seite.
- **Ansicht** immer ausdrücklich nennen (z. B. „von vorn“). In der Ansicht von vorn liegt die rechte Körperseite links im Bild.

## Lieferung (in dieser Reihenfolge versuchen)

1. **Direkt ins Repository:** ChatGPT legt das Bild als PNG unter `entwuerfe/<beitragsordner>/quelle/grafik/<lieferdateiname>` ab und setzt den Status im Auftrag auf `geliefert`.
2. **Google Drive:** Mariam speichert das Bild aus ChatGPT im Drive-Ordner **„Das wird gefragt – Grafiken“** unter dem Lieferdateinamen. Claude holt es dort ab und legt es im Repository ab.
3. **Notlösung:** Mariam schickt das Bild im Chat an Claude.

## Nach der Lieferung

Claude prüft die Grafik und schreibt `pruefung_anatomie_claude.md` in den Beitragsordner. Danach gibt es zwei Wege:
- **Fehler:** Status `Korrektur nötig`, darunter der Korrektur-Prompt. Die neue Lieferung heißt `…_v2.png`.
- **In Ordnung:** Status `angenommen`, Auftrag nach `erledigt/`. Claude baut den Post.
