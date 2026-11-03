servers = [
    {"name": "api-production", "cpu": 92.5, "active": True},
    {"name": "worker-01", "cpu": 45.0, "active": True},
    {"name": "database-01", "cpu": 76.0, "active": False},
    {"name": "backup-01", "cpu": 83.0, "active": True},
]

def get_cpu_status(cpu_usage):
    if cpu_usage >= 90:
        return "CRITICAL"
    elif cpu_usage >= 70:
        return "WARNING"
    else:
        return "OK"


print(f" === SERVER HEALTH MONITOR ===")
for server in servers:
    cpu_status = ''

    if server["active"]:
        cpu_status = get_cpu_status(server["cpu"])
    else:
        cpu_status = 'SKIPPED'  

    print(f"{server['name']} : {cpu_status}")
