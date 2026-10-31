server_name = "api-production"
server_ip = "10.0.0.15"
port = 443
is_active = True
memory_usage = 65.5
cpu_usage = 42.8

print(f" === SERVER INFORMATION ===")
print(f"Server: {server_name}")
print(f"IP: {server_ip}")
print(f"PORT: {port}")
print(f"ACTIVE: {is_active}")
print(f"MEMORY USAGE: {memory_usage} %")
print(f"MEMORY FREE: {100 - memory_usage:.1f} %")
print(f"CPU USAGE: {cpu_usage} %")
print(f"CPU FREE: {100 - cpu_usage:.1f} %")
