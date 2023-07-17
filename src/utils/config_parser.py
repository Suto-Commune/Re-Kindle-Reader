import copy
import json
import re
from collections import UserDict
from io import BytesIO, TextIOWrapper, BufferedRandom
from os import PathLike
from typing import Union, IO
from zipfile import ZipFile


class ConfigParser(UserDict):

    def __init__(self,
                 config: Union[
                     'ConfigParser', dict, PathLike, str, IO, TextIOWrapper, BytesIO, BufferedRandom] = 'config.json'):
        if isinstance(config, dict):
            data: dict = config
        elif isinstance(config, (str, PathLike)):
            with open(config, 'r') as f:
                data: dict = json.loads(self._del_comments(f.read()))
        elif isinstance(config, (IO, TextIOWrapper, BytesIO, BufferedRandom, ZipFile)):
            data: dict = json.load(config)
        elif isinstance(config, ConfigParser):
            data = config.data
        else:
            raise TypeError('config type error')
        super().__init__(data)

    @staticmethod
    def _del_comments(json_raw: str):
        json_str = re.sub(re.compile(r'//.*\n'), '', json_raw)
        json_str = re.sub(re.compile(r'/\*[^.]*\*/'), '', json_str)
        return json_str

    def __repr__(self):
        return f'ConfigParser({self.data})'

    def __contains__(self, item):
        return self.get_from_pointer(item) is not None

    def get_from_pointer(self, pointer: Union[str, int], default=None):
        json_path = str(pointer).split('/')
        json_path = list(filter(lambda x: bool(x), json_path))
        config = copy.deepcopy(self.data)

        for i in json_path:

            if config is None:
                return default
            if isinstance(config, list):
                i = int(i)
                if i >= len(config):
                    return default
                config = config[i]
            elif isinstance(config, dict):
                config = config.get(i, default)
            else:
                return default

        return config

    def __getitem__(self, item):
        return self.get_from_pointer(item)

    def __getattr__(self, item):
        i = self.data[item]
        return ConfigParser(i) if isinstance(i, dict) else i
