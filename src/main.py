import sys
import os
import json

def main():
    if len(sys.argv) != 3:
        print("❌ Użycie: python main.py input_file output_file")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"❌ Plik wejściowy nie istnieje: {input_path}")
        sys.exit(1)

    input_ext = os.path.splitext(input_path)[1].lower()

    try:
        if input_ext == ".json":
            with open(input_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            print("✅ JSON poprawnie wczytany:")
            print(data)
        else:
            print(f"⚠️ Nieobsługiwany format wejściowy: {input_ext}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Błąd podczas wczytywania pliku: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

