import os
import yaml

def load_policies(folder):
    policies = []
    for filename in os.listdir(folder):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            with open(os.path.join(folder, filename), "r") as f:
                policies.append(yaml.safe_load(f))
    return policies

