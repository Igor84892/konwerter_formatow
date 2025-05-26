import sys
import os

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

    print(f"📥 Plik wejściowy: {input_path} ({input_ext})")
    print(f"📤 Plik wyjściowy: {output_path} ({output_ext})")

if __name__ == "__main__":
    main()
