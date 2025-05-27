import sys
import os
from formats.json_handler import read_json, write_json

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
    output_ext = os.path.splitext(output_path)[1].lower()

    try:
        if input_ext == ".json":
            data = read_json(input_path)
            print("✅ Wczytano JSON.")

            if output_ext == ".json":
                write_json(data, output_path)
                print("✅ Dane zapisano do pliku JSON.")
            else:
                print("⚠️ Na razie obsługiwany tylko zapis do JSON.")
        else:
            print("⚠️ Nieobsługiwany format wejściowy:", input_ext)

    except Exception as e:
        print(f"❌ Błąd: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

