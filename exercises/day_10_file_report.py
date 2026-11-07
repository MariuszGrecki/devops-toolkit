with open("servers.txt", "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()
content_length = len(lines)

for line in lines:
    print(line)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("=== SERVER FILE REPORT ===\n")
    file.write(f"{content}\n")
    file.write(f"Total servers: {content_length}\n")