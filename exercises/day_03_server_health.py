server_name = "api-production"
cpu_usage = 92.5
memory_usage = 76.0

cpu_usage_status = ''
memory_usage_status = ''

print(f" === SERVER INFORMATION ===")
print(f"Server: {server_name}")
print(f"CPU USAGE: {cpu_usage} %")

if cpu_usage >= 90:
    cpu_usage_status = "CRITICAL"
elif cpu_usage >= 70:
    cpu_usage_status = "WARNING"
else:
    cpu_usage_status = "OK"

print(f"CPU STATUS: {cpu_usage_status} ")


print(f"MEMORY USAGE: {memory_usage} %")

if memory_usage >= 90:
    memory_usage_status = "CRITICAL"
elif memory_usage >= 70:
    memory_usage_status = "WARNING"
else:
    memory_usage_status = "OK"

print(f"MEMORY STATUS: {memory_usage_status} ")
