servers = [
    {"name": "api-production", "cpu": 92.5, "active": True},
    {"name": "worker-01", "cpu": 45.0, "active": True},
    {"name": "database-01", "cpu": 76.0, "active": False},
    {"name": "backup-01", "cpu": 83.0, "active": True},
]

print(f" === MULTI-SERVER HEALTH CHECK ===")


for server in servers:
    cpu_usage_status = ''

    if server['active'] == False: 
        cpu_usage_status = 'SKIPPED'
    else :
        if server['cpu'] >= 90:
            cpu_usage_status = "CRITICAL"
        elif server['cpu'] >= 70:
            cpu_usage_status = "WARNING"
        else:
            cpu_usage_status = "OK"

    print(f" {server['name']} : CPU {server['cpu']:.1f} - {cpu_usage_status}")
