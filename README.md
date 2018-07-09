# MSPNotenBot

Automatische Abfrage des Laufwerks nach neuen Dokumenten mit den Noten

---

### Usage

Regeln (Klasse / Modul / Telegram username) im `rules.json` definieren.

Cronjob erstellen mit ungefähr folgendem Inhalt:

```bash
python msp-check.py -i E1811_Info_HT\2-MSP Prüfungsergebnisse -s known.txt -r rules.json
```

---

### Todo:

- Durch lesen der PDF's und mit Matrikelnummer Rules eine personenspezifische Auswertung machen -> PM in Telegram



