import sys
import os
from formats.json_handler import read_json, write_json
from formats.yaml_handler import read_yaml, write_yaml
from formats.xml_handler import read_xml

def main():
    if len(sys.argv) != 3:
        print("Użycie: python main.py input_file output_file")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"Plik wejściowy nie istnieje: {input_path}")
        sys.exit(1)

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    try:
        # Wczytanie danych
        if input_ext == ".json":
            data = read_json(input_path)
            print("Wczytano JSON.")
        elif input_ext in [".yml", ".yaml"]:
            data = read_yaml(input_path)
            print("Wczytano YAML.")
        elif input_ext == ".xml":
            data = read_xml(input_path)
            print("Wczytano XML.")
        else:
            print(f"Nieobsługiwany format wejściowy: {input_ext}")
            sys.exit(1)

        # Zapis danych (jeszcze tylko JSON/YAML obsługiwany)
        if output_ext == ".json":
            write_json(data, output_path)
            print("Dane zapisano do pliku JSON.")
        elif output_ext in [".yml", ".yaml"]:
            write_yaml(data, output_path)
            print("Dane zapisano do pliku YAML.")
        else:
            print(f"Nieobsługiwany format wyjściowy: {output_ext}")

    except Exception as e:
        print(f"Błąd: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
