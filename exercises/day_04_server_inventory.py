servers = [
    {
        "name" : "api-production",
        "CPU" : 92.5,
        "active" : True,
    },
    {
        "name" : "worker-01",
        "CPU" : 45.0,
        "active" : True,
    },
    {
        "name" : "database-01",
        "CPU" : 76.0,
        "active" : False,
    }
]

print(" === SERVER INFORMATION ===")
print(f"Total servers: {len(servers)}")
print(f"First server: {servers[0]['name']}")
print(f"Second server CPU: {servers[1]['CPU']:.1f} %")
print(f"Last server: {servers[2]['name']}")

servers[0]["CPU"] = 65.0

print(f"Updated CPU: {servers[0]['CPU']:.1f}%")

servers.append({
    "name" : "backup-01",
    "CPU" : 25.0,
    "active" : True,
})

print(f"Last server: {servers[-1]['name']}")
