import yaml

class ConfigLoader:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        with open("D:/github_repository/MedLLM/config.yml", 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config

    def get_config(self):
        return self.config
