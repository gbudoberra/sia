import json


class Config:
    def __init__(self, json_file="conf.json"):
        with open(json_file, "r") as f:
            config = json.load(f)
            self.characters = sorted(config.get("characters", None))
            self.noises = config.get("noises", None)
