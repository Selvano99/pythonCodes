#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Desktop Cleaner (versione semplice)
# - Prende il Desktop dell'utente
# - Per ogni file: guarda l'estensione e lo sposta in una cartella dedicata
# - Se il nome esiste già, aggiunge " (1)", " (2)", ...
# - Niente parametri, niente log: pensato per essere letto e capito subito

from pathlib import Path
import shutil

# 1) Dove si trova il Desktop (gestiamo "Desktop" e "Scrivania")
def get_desktop() -> Path:
    home = Path.home()
    for name in ("Desktop", "Scrivania"):
        p = home / name
        if p.exists():
            return p
    # Se non esiste, usiamo comunque ~/Desktop come fallback
    return home / "Desktop"

# 2) Tabella molto piccola: estensione -> cartella
EXT_TO_FOLDER = {
    # immagini
    ".jpg": "Immagini", ".jpeg": "Immagini", ".png": "Immagini", ".gif": "Immagini",
    # documenti
    ".pdf": "Documenti", ".txt": "Documenti", ".doc": "Documenti", ".docx": "Documenti",
    # fogli/presentazioni
    ".xls": "Fogli", ".xlsx": "Fogli", ".csv": "Fogli",
    ".ppt": "Presentazioni", ".pptx": "Presentazioni",
    # archivi
    ".zip": "Archivi", ".rar": "Archivi", ".7z": "Archivi",
    # media
    ".mp3": "Audio", ".wav": "Audio", ".mp4": "Video", ".mov": "Video", ".mkv": "Video",
    # codice
    ".py": "Codice", ".js": "Codice", ".html": "Codice", ".css": "Codice", ".json": "Codice",
}

# 3) Se un file con lo stesso nome esiste già, aggiungiamo " (1)", " (2)", ...
def unique_path(dest_dir: Path, filename: str) -> Path:
    candidate = dest_dir / filename
    if not candidate.exists():
        return candidate

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    i = 1
    while True:
        candidate = dest_dir / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def main():
    desktop = get_desktop()
    print(f"Pulisco: {desktop}")

    if not desktop.exists():
        print("Il percorso del Desktop non esiste. Esco.")
        return

    for item in desktop.iterdir():
        # Saltiamo cartelle e file "nascosti" (tipo .DS_Store su macOS)
        if item.is_dir() or item.name.startswith("."):
            continue

        ext = item.suffix.lower()
        folder_name = EXT_TO_FOLDER.get(ext, "Altri")
        dest_dir = desktop / folder_name
        dest_dir.mkdir(exist_ok=True)

        dest_path = unique_path(dest_dir, item.name)
        shutil.move(str(item), str(dest_path))
        print(f"-> {item.name}  →  {folder_name}/{dest_path.name}")

    print("Fatto!")

if __name__ == "__main__":
    main()
