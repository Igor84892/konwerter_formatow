import yaml

def read_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise ValueError(f"Błąd odczytu pliku YAML: {e}")
