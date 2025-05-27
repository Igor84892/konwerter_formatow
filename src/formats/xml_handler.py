import xmltodict

def read_xml(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return xmltodict.parse(f.read())
    except Exception as e:
        raise ValueError(f"Błąd odczytu pliku XML: {e}")

def write_xml(data, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(xmltodict.unparse(data, pretty=True))
    except Exception as e:
        raise ValueError(f"Błąd zapisu pliku XML: {e}")
