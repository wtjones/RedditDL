from yaml_config import YamlConfig

class ConfigProvider(object):
    
    def __init__(self, path):
        if("config.yaml" in path):
            self._config = YamlConfig(path)
        else:
            NotImplemented("Config file is unknown.")
    def resolve(self):
        return self._config