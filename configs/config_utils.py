# config_utils.py

import tomllib

from configs import dirs

def env(section, key, default):
    with open(dirs.ROOT_DIR+"/env.toml", "rb") as f:
        data = tomllib.load(f)
        if data[section][key] == "":
            return default
        else:
            return data[section][key]
