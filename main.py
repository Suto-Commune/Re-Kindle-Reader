import logging
import src
from src.server import Server

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s][%(filename)s] %(message)s',
                    datefmt='%b/%d/%Y-%H:%M:%S')
logger = logging.getLogger(__name__)


def info():
    logger.info("RE:Kindle-Reader Start!")
    logger.info("Github Link: https://github.com/NatsumiXD/Re-Kindle-Reader")
    logger.info("Author: NatsumiXD")
    logger.info("SUTO")


if __name__ == "__main__":
    # 版权信息
    info()
    # 检查环境
    check_env = src.getready.get()
    # 启动线程
    Launcher = src.launcher.Launcher()
    Launcher.start()
    server = Server()
    server.run_server(True, 5000)
