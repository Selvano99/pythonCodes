# 🧹 Desktop Cleaner (versione semplice)

**Desktop Cleaner** è un piccolo script Python che organizza automaticamente i file presenti sul tuo Desktop in **cartelle per tipo di file** (immagini, documenti, archivi, ecc.).  
È pensato per essere **facile da capire**, **sicuro da usare** e **subito eseguibile** senza configurazioni.

---

## 📦 Funzionalità principali

- Organizza i file del Desktop in base all’estensione  
- Crea automaticamente le cartelle mancanti (es. “Immagini”, “Documenti”, …)  
- Evita di sovrascrivere file esistenti aggiungendo “(1)”, “(2)”, ecc.  
- Ignora le cartelle e i file nascosti (come `.DS_Store`)  
- Funziona su **Windows**, **macOS** e **Linux**

---

## 🧰 Requisiti

- **Python 3.7** o superiore  
- Nessuna libreria esterna: usa solo moduli standard (`pathlib`, `shutil`)

---

## 🚀 Come usarlo

1. **Scarica o copia** il file `desktop_cleaner_simple.py`
2. Salvalo in una cartella qualsiasi
3. Apri il terminale o il prompt dei comandi
4. Esegui:

   ```bash
   python desktop_cleaner_simple.py
   ```

Lo script rileverà automaticamente il percorso del tuo Desktop (o “Scrivania”, su macOS in italiano) e sposterà i file nelle relative sottocartelle.

---

## 📁 Esempio di risultato

Supponiamo che sul Desktop ci siano:

```
Desktop/
│
├── foto.jpg
├── documento.pdf
├── script.py
├── archivio.zip
└── video.mp4
```

Dopo l’esecuzione:

```
Desktop/
│
├── Immagini/
│   └── foto.jpg
│
├── Documenti/
│   └── documento.pdf
│
├── Codice/
│   └── script.py
│
├── Archivi/
│   └── archivio.zip
│
└── Video/
    └── video.mp4
```

---

## ⚙️ Come funziona in breve

1. Cerca la cartella Desktop (supporta sia “Desktop” che “Scrivania”).  
2. Legge tutti i file (non le sottocartelle).  
3. In base all’estensione, decide dove spostarli (usando un dizionario `EXT_TO_FOLDER`).  
4. Se la cartella non esiste, la crea.  
5. Se un file con lo stesso nome è già presente, aggiunge “(1)”, “(2)”, ecc.  
6. Sposta il file e stampa a schermo l’azione eseguita.

---

## 💡 Personalizzazione

Puoi modificare la tabella `EXT_TO_FOLDER` nel codice per aggiungere o cambiare categorie.  
Esempio:

```python
".psd": "Disegni",
".ai": "Disegni",
".csv": "Fogli",
".zip": "Archivi",
```

---

## 🧪 Suggerimenti d’uso

- Provalo prima su una **cartella di test**: basta cambiare `desktop = get_desktop()` con un percorso manuale, ad esempio:
  ```python
  desktop = Path("/Users/nome/Downloads")
  ```
- Eseguilo ogni tanto per tenere ordinato il Desktop.  
  (Puoi anche schedularlo con **Task Scheduler** su Windows o **cron** su macOS/Linux.)

---

## 📜 Licenza

Questo script è rilasciato sotto licenza **MIT** — puoi modificarlo, copiarlo e usarlo liberamente.
