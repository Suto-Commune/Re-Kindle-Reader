import yaml


def get_config():
    config_file = open("./config.yaml", "r", encoding="UTF-8")
    config_dict = yaml.load(config_file, Loader=yaml.FullLoader)
    config_file.close()
    return config_dict


config = get_config()
