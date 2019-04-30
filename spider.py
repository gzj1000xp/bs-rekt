# -*- coding: utf-8 -*
import urllib
import re
from bs4 import BeautifulSoup
import os
import requests
import time
import datetime


def getpage(wrongtry=0, leastlink=""):
    homepage = "https://www.rektmag.net"
    article_page = []
    session = requests.session()
    html = session.get(homepage, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")
    for asrc in soup.find_all('div', class_='Blog-header-content'):
        a_src = asrc.find('a').get('href')
        pageurl = homepage + a_src
        article_page.append(pageurl)
        downpic(pageurl)
    return article_page


def downpic(article):
    global picnum
    CurrentPath = os.getcwd()

    print(article)
    dirname_list = re.split("/", article)
    # dirname = dirname_list[-4] + '-' + dirname_list[-3] + '-' + dirname_list[-2]
    dirname = dirname_list[-1]
    print(dirname)

    session_d = requests.session()
    html_d = session_d.get(article, headers=headers)
    soup = BeautifulSoup(html_d.content, "html.parser")
    for imgsrc in soup.find_all('div', class_='image-wrapper'):
        img_src = imgsrc.find('img').get('src')
        print(img_src)
        picname_list = re.split("/", img_src)
        picname = picname_list[-1]
        print(picname)
        filename = CurrentPath + '/rekt_img/' + dirname + '/' + picname
        picnum = picnum + 1
        if os.path.exists(CurrentPath + '/rekt_img/' + dirname):
            pass
        else:
            os.mkdir(CurrentPath + '/rekt_img/' + dirname)

        if os.path.exists(filename):
            print(u'该文件已经存在')
        else:
            try:
                urllib.request.urlretrieve(img_src, filename)
                time.sleep(0.5)
                print(u'下完了%s张' % picnum)
            except Exception:
                print(u'这张图片下载出问题了： %s' % filename)


# 程序入口
if __name__ == '__main__':
    if not os.path.exists("rekt_img"):
        os.makedirs("rekt_img")
        print("创建目录")
        # 创建目录
print ("存储在 PY文件目录/rekt_img 中")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': user_agent, 'Referer': 'https://www.rektmag.net'}
# 准备headers
pagenum = 0
picnum = 0
# 准备计次变量
article_list = getpage()
