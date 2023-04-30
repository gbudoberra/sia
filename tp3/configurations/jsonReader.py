import json


class JsonReader:
    def __init__(self, json_file="conf_and.json"):
        with open(json_file, "r") as f:
            config = json.load(f)
            self.points = config.get("points", None)
            self.expected = config.get("expected", None)
            self.update_method = config.get("update_method", None)
            self.activation_method = config.get("activation_method", None)
            self.learning_rate = config.get("learning_rate", None)
            self.epsilon = config.get("epsilon", None)
            self.perceptron_by_layer = config.get("perceptron_by_layer", None)
