def get_cpu_status(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 70:
        return "WARNING"
    else:
        return "OK"

if __name__ == "__main__":
    print(get_cpu_status(95))