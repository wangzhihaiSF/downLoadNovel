import time
from multiprocessing.pool import Pool

import requests, bs4, datetime
timeSum = 0
pageNumber = 404142

def get_page_source(page):
    url = "https://www.booktxt.net/1_1213/" + str(page) + ".html"
    response = requests.get(url)
    return response

def get_content(response):
    data = bs4.BeautifulSoup(response, "html.parser")
    contentTag = data.select("#content")
    for j in contentTag:
        content = j.getText()
        save_content(content)

def save_content(content):
    novel = open("zhetian.txt", "a+", encoding="utf-8")
    novel.write(content)

def main(page):
    print("开始下载第", page, "章:")
    time1 = time.time()
    response = get_page_source(page)
    data = get_content(response)
    save_content(data)
    time2 = time.time()
    timeChange = time2 -time1
    print("第", page, "章耗时", round(timeChange,1), "秒")

if __name__ == "__main__":
    pool = Pool() # 多线程线程池
    groups = (list(range(404142, 406011)))
    pool.map(main, groups)  # map() 实现多线程下载
    pool.close()
    pool.join()