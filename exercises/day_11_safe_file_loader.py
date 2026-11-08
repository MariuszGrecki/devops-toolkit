try:
    with open("servers.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("servers.txt not found")

else:
    servers = []

    for line in content.splitlines():
        server_name = line.strip()

        if server_name:
            servers.append(server_name)

    if not servers:
        print("WARNING: No servers configured")

    print("=== SAFE CONFIGURATION LOADER ===")
    print("File loaded successfully")
    print(f"Servers found: {len(servers)}")

    for server in servers:
        print(f"- {server}")


        

