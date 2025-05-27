# Konwerter formatów danych: JSON, XML, YAML

## Opis
Projekt pozwala na konwersję danych pomiędzy formatami: JSON, XML i YAML. Dostępna jest wersja konsolowa oraz graficzna (GUI).

## Obsługiwane funkcje
Wczytywanie: JSON, YAML, XML  
Zapis: JSON, YAML, XML  
GUI: tkinter  
Wersja EXE: `pyinstaller --onefile --noconsole`

## Struktura projektu
- `src/main.py` – wersja konsolowa
- `src/gui_app.py` – wersja graficzna
- `formats/` – moduły obsługi formatów
- `.github/workflows/build.yml` – automatyczne budowanie `.exe` przez GitHub Actions
- `installResources.ps1` – skrypt instalacyjny

## Jak uruchomić
```bash
python src/main.py wejście.json wyjście.xml
python src/gui_app.py

