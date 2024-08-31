import yaml

class Config:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def load(config_path):
        with open(config_path, "r") as file:
            config_data = yaml.safe_load(file)
        return Config(config_data)
    
    def get(self, key, default=None):
        return self.data.get(key, default)
