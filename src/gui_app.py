import tkinter as tk
from tkinter import filedialog, messagebox
from formats.json_handler import read_json, write_json
from formats.yaml_handler import read_yaml, write_yaml
from formats.xml_handler import read_xml, write_xml
import os
import threading

def konwertuj():
    input_path = entry_input.get()
    output_path = entry_output.get()

    if not os.path.exists(input_path):
        messagebox.showerror("Błąd", f"Plik wejściowy nie istnieje:\n{input_path}")
        return

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    try:
        if input_ext == ".json":
            data = read_json(input_path)
        elif input_ext in [".yml", ".yaml"]:
            data = read_yaml(input_path)
        elif input_ext == ".xml":
            data = read_xml(input_path)
        else:
            messagebox.showerror("Błąd", f"Nieobsługiwany format wejściowy: {input_ext}")
            return

        if output_ext == ".json":
            write_json(data, output_path)
        elif output_ext in [".yml", ".yaml"]:
            write_yaml(data, output_path)
        elif output_ext == ".xml":
            write_xml(data, output_path)
        else:
            messagebox.showerror("Błąd", f"Nieobsługiwany format wyjściowy: {output_ext}")
            return

        messagebox.showinfo("Sukces", f"Konwersja zakończona:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Błąd", str(e))

def uruchom_watkow():
    threading.Thread(target=konwertuj).start()

def wybierz_wejsciowy():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def wybierz_wyjsciowy():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, file_path)

root = tk.Tk()
root.title("Konwerter plików")

tk.Label(root, text="Plik wejściowy:").grid(row=0, column=0, padx=10, pady=5)
entry_input = tk.Entry(root, width=40)
entry_input.grid(row=0, column=1)
tk.Button(root, text="Wybierz...", command=wybierz_wejsciowy).grid(row=0, column=2)

tk.Label(root, text="Plik wyjściowy:").grid(row=1, column=0, padx=10, pady=5)
entry_output = tk.Entry(root, width=40)
entry_output.grid(row=1, column=1)
tk.Button(root, text="Zapisz jako...", command=wybierz_wyjsciowy).grid(row=1, column=2)

tk.Button(root, text="Konwertuj", command=uruchom_watkow, width=20).grid(row=2, column=1, pady=20)

root.mainloop()
