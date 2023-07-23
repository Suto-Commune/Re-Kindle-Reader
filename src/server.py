import importlib
import logging
import os
import platform
from pathlib import Path
from typing import Generator

from flask import Flask
from gevent import pywsgi


class Server:
    def __init__(self):
        self.app = Flask(__name__, static_folder='./RKR', static_url_path='/')
        self.app.template_folder = Path('src/templates').resolve()
        ...

    def start(self, debug: bool, port: int):
        if debug:
            logging.info("DEBUG IS TRUE.Using Flask.app.run.")
            self.app.run(host='0.0.0.0', debug=True, port=port)
        else:
            logging.info("Using WSGI.")
            server = pywsgi.WSGIServer(('0.0.0.0', port), self.app)
            server.serve_forever()

    def load_blueprint(self):
        def get_blueprints() -> Generator[str, None, None]:
            for root, dirs, files in os.walk(Path("src/pages")):
                for file in filter(lambda x: x.endswith(".py"), files):
                    file_path = os.path.join(root, file)
                    file_path = file_path.replace(".\\", "").replace(".py", "")
                    yield file_path

        for i in get_blueprints():
            m = '.'.join(i.split("/" if "Linux" in platform.system() else "\\"))
            logging.info(f"Load {m}.")
            module = importlib.import_module(m)
            self.app.register_blueprint(module.page)

    def run_server(self, debug: bool, port: int):
        self.load_blueprint()
        self.start(debug, port)

