import logging
import src
from src.server import Server
from src.toml_config_reader import config

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s][%(filename)s] %(message)s',
                    datefmt='%b/%d/%Y-%H:%M:%S')
logger = logging.getLogger(__name__)


def info():
    def multi_line_log(logger_: logging.Logger = logging.getLogger(), level: int = logging.INFO, msg: str = ""):
        for line in msg.splitlines():
            logger_.log(level, line)

    contributors = ["@NatsumiXD", "@hsn8086"]
    contributors_msg = "Contributors: "
    for i in contributors:
        contributors_msg += i + ","
    contributors_msg = contributors_msg[0:-1]

    logger.info("====================================================")
    multi_line_log(logger_=logger, msg="""
    |        # #     #   #    #   # #     #     |
    |    # #     # ########## # #     #         |
    |           #    #    #          #          |
    |          #          #         #           |
    |        ##          #        ##            |
    |      ##           #       ##              |
    |    ##           #       ##                |
    """)
    logger.info("------------------------------------------------------")
    logger.info("Re:Kindle-Reader Loading!")
    logger.info("Github Link: https://github.com/NatsumiXD/Re-Kindle-Reader")
    logger.info(contributors_msg)
    logger.info("Organizations: @SUTO-Commune")
    logger.info("====================================================")


if __name__ == "__main__":
    # 版权信息
    info()
    # 检查环境
    check_env = src.getready.get()
    # 启动线程
    Launcher = src.launcher.Launcher()
    Launcher.start()
    server = Server()
    server.run_server(config["server"]["DEBUG"], 5000)
