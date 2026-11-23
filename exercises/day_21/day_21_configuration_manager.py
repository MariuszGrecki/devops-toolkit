
from pathlib import Path
import shutil
import yaml

BASE_DIR = Path(__file__).resolve().parent

source_file = BASE_DIR / "servers.yaml"
backup_dir = BASE_DIR / "backups"
backup_file = backup_dir / "servers.yaml.bak"

print("=== CONFIGURATION MANAGER ===")

try:
    with source_file.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        print("ERROR: Invalid configuration")

    elif not isinstance(config.get("servers"), list):
        print("ERROR: Invalid configuration")

    else:
        servers = config["servers"]
        server_updated = False

        for server in servers:
            if not isinstance(server, dict):
                continue

            if server.get("name") == "worker-01":
                server["active"] = False
                server_updated = True
                break

        if server_updated:
            backup_dir.mkdir(parents=True, exist_ok=True)

            shutil.copy2(source_file, backup_file)

            with source_file.open("w", encoding="utf-8") as file:
                yaml.safe_dump(
                    config,
                    file,
                    allow_unicode=True,
                    sort_keys=False
                )

            print("Backup created: backups/servers.yaml.bak")
            print("Server worker-01 updated successfully")

        else:
            print("Server worker-01 not found")

except FileNotFoundError:
    print("ERROR: servers.yaml not found")

except yaml.YAMLError as error:
    print(f"ERROR: Invalid YAML: {error}")

except OSError as error:
    print(f"ERROR: File operation failed: {error}")

