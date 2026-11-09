import json

try:
    with open("servers.json", "r", encoding="utf-8") as file:
        servers = json.load(file)

except FileNotFoundError:
    print("servers.sjon not found")

except json.JSONDecodeError as e:
    print(f"Invalid JSON")

else:
    active_servers = []
    print("=== JSON SERVER INVENTORY ===")
    for server in servers:
        if server["active"]:
            status = "ACTIVE"
            active_servers.append(server)
        else: 
            status = "INVACTIVE"

        print(f"{server['name']}: {status}")

    print(f"Total servers: {len(servers)}")
    print(f"Active servers: {len(active_servers)}")

    data = {
        "total_servers": len(servers),
        "active_servers": len(active_servers)
    }

    with open("server.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)