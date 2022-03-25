#! encoding: utf-8
"""
电影天堂，电影磁力链
"""
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',

}


def get_html(url):
    r = requests.get(url, headers=headers, timeout=60)  # 最基本的不带参数的get请求
    html = r.text
    return html


def parse_page(text):
    """解析页面的信息"""
    global max_page
    words = []
    html = etree.HTML(text)
    lesson = html.xpath("/html/body/div[5]/div[2]/div[2]/text()")[0]
    soup = BeautifulSoup(text, 'lxml')
    max_page = int(soup.select('option')[6].string.split('/')[-1])
    trs = soup.find_all('tr')
    for index, tr in enumerate(trs, 0):
        # print(tr)
        if index == 0 or index == 1:
            continue
        word = [lesson, ]
        for i, td in enumerate(tr, 0):
            if i == 1:  # 编号
                word.append(td.string)
            if i == 5:  # 日本语
                word.append(td.string)
            if i == 7:  # 假名
                word.append(td.string)
            if i == 9:  # 音频
                word.append(td.find("a").attrs.get("name"))
            if i == 11:  # 中文
                word.append(td.string)
            if i == 13:  # 词性
                word.append(td.string)
            if i == 15:  # 例句
                word.append(td.a.attrs.get("title"))
        words.append(word)
    return words


def spider():
    data = []
    for lesson_id in range(288, 336):
        page_id = 1
        while page_id <= max_page:
            url = f"http://jp.qsbdc.com/jpword/word_list.php?lesson_id={lesson_id}&&tag=all&&page_id={page_id}"
            print(url)
            html = get_html(url)
            result = parse_page(html)
            data.extend(result)
            page_id += 1
            # time.sleep(random.randint(1,1))
    print(data)
    with open('data.txt','w') as f:
        f.write(str(data))


if __name__ == '__main__':
    max_page = 1
    last_lesson_id = 0
    spider()
