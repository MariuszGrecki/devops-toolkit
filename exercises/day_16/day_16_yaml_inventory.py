import yaml

try:
    with open("servers.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

except FileNotFoundError:
    print('Nie znaleziono pliku')

except yaml.YAMLError as error:
    print(f"Niepoprawny YAML: {error}")

else:   
    servers = config["servers"]

    print("=== YAML SERVER INVENTORY ===")

    active_servers = []

    for server in servers:
        server_status = ''

        if server["active"]:
            active_servers.append(server)
            server_status = 'ACTIVE'
        else:
            server_status = 'INACTIVE'

        print(f"{server['name']}:  {server_status}")

    print(f"Total servers: {len(servers)}")
    print(f"Active servers: {len(active_servers)}")
