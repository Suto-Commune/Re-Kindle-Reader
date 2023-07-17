import tomllib


def get_config():
    config_file = open("./config.toml", "r", encoding="UTF-8")
    config1=tomllib.loads(config_file.read())
    return config1


config = get_config()