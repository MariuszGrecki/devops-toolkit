import json

try: 
    with open("day_14/servers_validation.json", "r", encoding="utf-8") as file:
        servers = json.load(file)

except FileNotFoundError:
    print("Nie znaleziono pliku")

except json.JSONDecodeError as e:
    print("Invalid JSon")

else:

    print("=== CONFIG VALIDATION REPORT ===")

    valid_servers = []
    invalid_servers = []
    status = ''

    for server in servers:
        if 'cpu' not in server or 'name' not in server  or 'active' not in server:
            invalid_servers.append(server)
            print(f"{server['name']} : INVALID")
            continue

        if server["name"] == '':
            invalid_servers.append(server)
            print(f"{server['name']} : INVALID")
            continue

        if not isinstance(server["active"], (bool)):
            invalid_servers.append(server)
            print(f"{server['name']} : INVALID")
            continue

        if type(server["cpu"]) not in(int, float) or not 0 <= server["cpu"] <= 100:
            invalid_servers.append(server)
            print(f"{server['name']} : INVALID")
            continue

        valid_servers.append(server)
        print(f"{server['name']} : VALID")

print(f"Valid servers: {len(valid_servers)}")
print(f"Invalid servers: {len(invalid_servers)}")
