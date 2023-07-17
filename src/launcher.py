import logging
import subprocess
import threading
from pathlib import Path

import psutil

from src.utils.config_parser import ConfigParser


# Reader Start

class Launcher:

    @staticmethod
    def reader_thread():

        if not Path("pid").exists():
            logging.info("Reader")
            Launcher.open()
        else:
            with open("pid", "r") as f:
                pids = psutil.pids()
                p = f.readline()
                if p == "" or p not in str(pids):
                    Launcher.open()

    @staticmethod
    def open():
        try:
            p = subprocess.Popen([f"{ConfigParser().java}", "-jar", "reader.jar", "--reader.server.port=12306"],
                                 cwd="./reader", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            with open("./pid", "w") as f:
                f.write(str(p.pid))
            while p.poll() is None:
                line = p.stdout.readline(-1)
                s = str(line).replace("b'", "").replace("\\r\\n'", "")
                if "ReaderApplication Started" in s:
                    logging.info("\b[reader.jar] " + s)
        except FileNotFoundError as err:
            logging.getLogger(__name__).exception(err)
            logging.getLogger(__name__).critical(
                'Unable to load thread:"reader",please check file or java integrity.')

    def start(self):
        self.t_reader.start()

    t_reader = threading.Thread(name='reader', target=reader_thread, daemon=True)
