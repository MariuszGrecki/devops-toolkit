configs = [
    {"servers": [{"name": "api-01"}]},
    None,
    {"servers": "api-01"},
    {"name": "worker-01"},
    {"servers": []}
]

for i, config in enumerate(configs, start=1):

    if isinstance(config, dict) and isinstance(config.get("servers"), list):
        print(f"Configuration {i}: VALID")
    else:
        print(f"Configuration {i}: INVALID")
