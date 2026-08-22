import json

config = {"learning_rate": 0.01, "epochs":10}

with open("config.json", "w") as f:
    json.dump(config, f)

with open("config.json", "r") as f:
    config = json.load(f)

print(config)