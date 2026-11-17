from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent
config_path = BASE_DIR / "servers.yaml"

try:
    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

except FileNotFoundError:
    print('Nie znaleziono pliku')

except yaml.YAMLError as error:
    print(f"Niepoprawny YAML: {error}")

else:   
    servers = config["servers"]

    print("=== PORTABLE YAML LOADER ===")

    for server in servers:
        print(f"{server['name']}")

    print(f"Total servers: {len(servers)}")
