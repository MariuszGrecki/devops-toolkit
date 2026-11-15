import yaml

try:
    with open("servers_maintenance.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

except FileNotFoundError:
    print('Nie znaleziono pliku')

except yaml.YAMLError as error:
    print(f"Niepoprawny YAML: {error}")

else:   
    servers = config["servers"]
    worker_01_present = False

    for server in servers:
        if server["name"] == 'worker-01':
            server["active"] = False
            server["cpu"] = 85.0
            worker_01_present = True

    if worker_01_present:  
        print("Server worker-01 updated successfully")
        print("Active: False")
        print("CPU: 85.0")
          
        with open("servers_maintenance.yaml", "w", encoding="utf-8") as file:
            yaml.safe_dump(config, file, sort_keys=False)

    else:
        print("Server worker-01 not found")




