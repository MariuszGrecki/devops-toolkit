import server_utils

servers = [
    {"name": "api-production", "cpu": "95.5", "active": True},
    {"name": "worker-01", "cpu": "unknown", "active": True},
    {"name": "database-01", "cpu": "76.0", "active": True},
    {"name": "backup-01", "cpu": "20.0", "active": False},
]

print("=== MODULAR SERVER MONITOR===")

for server in servers:
    if not server['active']:
        print(f"{server['name']}: SKIPPED")
        continue

    try:
        cpu_usage = float(server['cpu'])
    except ValueError:
        print(f"{server['name']}: INVALID CPU")
        continue

    cpu_status = server_utils.get_cpu_status(cpu_usage)

    print(f"{server['name']}: {cpu_status}")