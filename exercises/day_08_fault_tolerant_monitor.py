servers = [
    {"name": "api-production", "cpu": "95.5", "active": True},
    {"name": "worker-01", "cpu": "unknown", "active": True},
    {"name": "database-01", "cpu": "76.0", "active": True},
    {"name": "backup-01", "cpu": "20.0", "active": False},
]

def get_cpu_status(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 70:
        return "WARNING"
    else:
        return "OK"

print("=== FAULT-TOLERANT SERVER MONITOR===")

for server in servers:
    if server['active'] == False:
        print(f"{server['name']} : SKIPPED")
        continue
    
    try:
        cpu = float(server['cpu'])
    except ValueError:
        print(f"{server['name']} : INVALID CPU value")
        continue

    cpu = get_cpu_status(cpu)

    print(f"{server['name']} : {cpu}")

