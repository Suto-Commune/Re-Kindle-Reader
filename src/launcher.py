import os.path
import threading
import subprocess
import logging
import config
import psutil


# Reader Start

class Launcher:

    @staticmethod
    def reader_thread():
        opened = True
        if not os.path.exists("pid"):
            logging.info("Reader")
            opened = False
        elif os.path.exists("pid"):
            with open("pid", "r") as f:
                pids = psutil.pids()
                if not f.readline() in str(pids):
                    opened = False
        if not opened:
            try:
                p = subprocess.Popen([f"{config.java_path}", "-jar", "reader.jar", "--reader.server.port=12306"],
                                     cwd="./reader", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                with open("./pid", "w") as f:
                    f.write(str(p.pid))
                o = 0
                while p.poll() is None:
                    line = p.stdout.readline(-1)
                    if "ReaderApplication Started" in str(line).replace("b'", "").replace("\\r\\n'", ""):
                        o = 1
                    if o == 1:
                        logging.info("\b[reader.jar] " + str(line).replace("b'", "").replace("\\r\\n'", ""))
            except FileNotFoundError as err:
                logging.getLogger(__name__).critical(err)
                logging.getLogger(__name__).critical(
                    'Unable to load thread:"reader",please check file or java integrity.')

    def start(self):
        self.t_reader.start()

    t_reader = threading.Thread(name='reader', target=reader_thread, daemon=True)
