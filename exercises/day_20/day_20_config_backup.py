from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
source = BASE_DIR / "servers.yaml"

backup_dir = BASE_DIR / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)

backup_file = backup_dir / "servers.backup.yaml"

if source.is_file():
    shutil.copy2(source, backup_file)

    print(
        "=== CONFIG BACKUP MANAGER ===\n"
        "Source: servers.yaml\n"
        "Backup: backups/servers.yaml.bak\n"
        "Backup created successfully"
    )

else:
    print("ERROR: servers.yaml not found")