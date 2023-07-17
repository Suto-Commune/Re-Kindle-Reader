from flask import Flask
from gevent import pywsgi
import logging
import os
import importlib


class Server:
    def __init__(self):
        self.app = Flask(__name__, static_folder='./RKR', static_url_path='/')
        ...

    def start(self, debug: bool, port: int):
        if debug:
            logging.info("DEBUG IS TRUE.Using Flask.App.Run .")
            self.app.run(host='0.0.0.0', debug=True, port=port)
        else:
            logging.info("Using WSGI .")
            server = pywsgi.WSGIServer(('0.0.0.0', port), self.app)
            server.serve_forever()

    def load_blueprint(self):
        liss = list()
        modules = {}
        directory = ".\\src\\pages"
        lis = list()
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)

                    file_path = file_path.replace(".\\", "").replace(".py", "").split("\\")
                    lis.append(file_path)
        for i in lis:
            m = ""
            for j in range(0, len(i)):
                if j == 0:
                    m = i[0]
                else:
                    m = m + "." + str(i[j])
            liss.append(m)
        for i in liss:
            logging.info(f"Load {i} .")
            module = importlib.import_module(i)
            modules[i] = module
        for i in liss:
            self.app.register_blueprint(modules[i].page)

    def run_server(self, debug: bool, port: int):
        self.load_blueprint()
        self.start(debug, port)

# Server1 = Server()
# Server1.run_server(True, 5000)
