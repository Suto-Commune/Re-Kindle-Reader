import logging

import httpx

url = "http://127.0.0.1:12306/reader3"


# 书架信息
def get_book_shelf():
    logging.info(f"\b[{__name__}] Get the book shelf data.")
    response = httpx.get(f"{url}/getBookshelf")
    json = response.json()["data"]
    data = []
    for i in json:
        data.append(
            {
                # 书籍URL
                "book_url": i["bookUrl"],
                # 源
                "origin": i["origin"],
                # 书名
                "name": i["name"],
                # 作者
                "author": i["author"],
                # 分类
                "kind": i["kind"],
                # 封面
                "cover": i["coverUrl"],
                # 介绍
                "intro": i["intro"],
                # 组
                "group": i["group"],
                # 最新章节标题
                "latest_title": i["latestChapterTitle"],
                # 总章节数(从0开始)
                "total_index": int(i["totalChapterNum"]),
                # 最后阅读标题
                "last_title": i["durChapterTitle"],
                # 最后阅读的章节(从0开始)
                "last_index": int(i["durChapterIndex"])
            }
        )
    return data


# 章节信息
def get_chapter_list(book_url: str, refresh: int):
    logging.info(f"\b[{__name__}] Get the chapter list for {book_url}.refresh is {refresh}.")
    data = {
        "url": book_url,
        "refresh": refresh
    }
    response = httpx.post(f"{url}/getChapterList", json=data)
    json = response.json()["data"]
    data = []
    for i in json:
        data.append(
            {
                # 章节URL
                "chapter_url": i["url"],
                # 章节名称
                "chapter_title": i["title"],
                # 章节序号
                "chapter_index": int(i["index"]),
                # 书籍URL
                "book_url": book_url
            }
        )
    return data


def get_book_content(book_url: str, index: int):
    data = {
        "url": book_url,
        "index": index
    }
    response = httpx.post(f"{url}/getBookContent", json=data)
    json = response.json()
    data = {
        # 章节内容
        "text": json["data"],
        # 书籍URL
        "book_url": book_url,
        # 书籍INDEX
        "index": index
    }
    return data

