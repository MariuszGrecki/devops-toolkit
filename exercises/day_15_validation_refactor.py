import json

def validate_server(server): 
    if 'cpu' not in server or 'name' not in server  or 'active' not in server:
        return False

    if not isinstance(server["active"], (bool)):
        return False

    if not validate_name(server["name"]) or not validate_cpu(server["cpu"]):
        return False

    return True


def validate_name(name):
    if not isinstance(name, str):
        return False

    if not name.strip():
        return False

    return True


def validate_cpu(cpu):
    if type(cpu) not in (int, float):
        return False

    if not 0 <= cpu <= 100:
        return False

    return True

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
        if validate_server(server):
            valid_servers.append(server)
            print(f"{server['name']} : VALID")
        else:
            invalid_servers.append(server)
            print(f"{server.get('name', 'UNKNOWN')} : INVALID")

print(f"Valid servers: {len(valid_servers)}")
print(f"Invalid servers: {len(invalid_servers)}")
