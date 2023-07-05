import threading
import subprocess
import logging


# Reader Start

class Launcher:

    @staticmethod
    def reader_thread():
        try:
            p = subprocess.Popen(["java", "-jar", "reader.jar","--reader.server.port=12306"],
                                 cwd="./reader", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            o = 0
            while p.poll() is None:
                line = p.stdout.readline(-1)
                if "ReaderApplication Started" in str(line).replace("b'", "").replace("\\r\\n'", ""):
                    o = 1
                if o == 1:
                    logging.info("\b[reader.jar] "+str(line).replace("b'", "").replace("\\r\\n'", ""))
        except FileNotFoundError as err:
            logging.getLogger(__name__).critical(err)
            logging.getLogger(__name__).critical('Unable to load thread:"reader",please check file or java integrity.')

    def start(self):
        self.t_reader.start()

    t_reader = threading.Thread(name='reader', target=reader_thread, daemon=True)
