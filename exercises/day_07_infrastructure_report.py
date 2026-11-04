servers = [
    {"name": "api-production", "cpu": 95.0, "active": True},
    {"name": "worker-01", "cpu": 42.5, "active": True},
    {"name": "database-01", "cpu": 75.0, "active": True},
    {"name": "backup-01", "cpu": 20.0, "active": False},
]

total_servers = 0
critical_servers = 0

def get_cpu_status(cpu, active):
    if active != True:
        return "SKIPPED"

    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 70:
        return "WARNING"
    else:
        return "OK"

print("=== INFRASTRUCTURE HEALTH REPORT ===")

for server in servers:
    total_servers += 1
    
    cpu_status = get_cpu_status(server['cpu'], server['active'])

    if cpu_status == 'CRITICAL':
        critical_servers += 1

    print(f"{server['name']} : {cpu_status}")

print(f"Total servers : {total_servers}")
print(f"Critical servers : {critical_servers}")