def get():
    import requests
    import wget
    import os
    import sys
    import logging
    import subprocess

    logging.info("Checking the ENV.")
    if not os.path.exists("reader"):
        os.mkdir("reader")
    else:
        ...

    if not "jar" in str(os.listdir("./reader")):
        logging.warning("Reader not found.Try to download it from github.")
        latest = requests.get("https://api.github.com/repos/hectorqin/reader/releases/latest").json()
        url = str()
        for i in latest["assets"]:
            if ".jar" in i["name"]:
                url = i["browser_download_url"]
                break
        try:
            wget.download(url, "./reader/reader.jar")
            print("")
        except:
            logging.warning("Cannot download the reader file.Try to download it from ghproxy.")
            try:
                wget.download(f"https://ghproxy.com/{url}", "./reader/reader.jar")
                print("")
            except:
                logging.error(f"Cannot download the reader file.Try to download it from {url}"
                              f" by yourself,then rename it as \"reader.jar\",put it into the reader folder.")
                sys.exit(0)

    if "java" not in str(subprocess.run(["where", "java"], stdout=subprocess.PIPE).stdout):
        logging.error("Java Not Found.Please Install Java 17+.You Can Download It From adoptium.net")
        sys.exit(0)

    logging.info("Done.")
