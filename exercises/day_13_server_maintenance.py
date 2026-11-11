import json

try:
    with open("servers_maintenance.json", "r", encoding="utf-8") as file:
        servers = json.load(file)

except FileNotFoundError:
    print("servers_maintenance.json not found")

except json.JSONDecodeError as e:
    print(f"Invalid JSON")

else:
    new_cpu = 85
    server_updated = False
    server_to_update = "worker-01"

    for server in servers:
        if server["name"] == server_to_update:
            server["cpu"] = new_cpu
            server["active"] = False
            server_updated = True

    if server_updated:
        with open("servers_maintenance.json", "w", encoding="utf-8") as file:
            json.dump(servers, file, indent=4)

        print(f"server {server_to_update} updated successfully")
        print(f"Active: False")
        print(f"CPU: {new_cpu}")
    else:
        print(f"Server {server_to_update} not found")