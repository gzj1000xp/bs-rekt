# -*- coding: utf-8 -*
import urllib
import re
from bs4 import BeautifulSoup
import os
import requests
import time


def getpic(homepage="", wrongtry=0, leastlink=""):

    piclist = []
    session = requests.session()
    html = session.get(homepage, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")
    # print(soup.find_all('div', class_='AdaptiveMedia-photoContainer js-adaptive-photo'))
    for asrc in soup.find_all('div', class_='AdaptiveMedia-photoContainer js-adaptive-photo'):
        a_src = asrc.find('img').get('src')
        picurl = a_src
        # print(picurl)
        piclist.append(picurl)
        # downpic(pageurl)
    return piclist


def downpic(pic_list):
    global picnum
    CurrentPath = os.getcwd()
    # print(CurrentPath)
    for img_src in pic_list:
        print(img_src)
        picname_list = re.split("/", img_src)
        picname = picname_list[-1]
        print(picname)
        filename = CurrentPath + '/twitter/' + picname
        picnum = picnum + 1
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
    #page = 0
    #member_id = "1036063"
    if not os.path.exists("twitter"):
        os.makedirs("twitter")
        print("创建目录")
        # 创建目录
print ("存储在 PY文件目录/twitter 中")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': user_agent, 'Referer': 'https://www.rektmag.net'}
# 准备headers
pagenum = 0
picnum = 0
# 准备计次变量

sites = ["https://twitter.com/PDChina", "https://twitter.com/NatGeo", "https://twitter.com/XinhuaChinese"]
# homepage = "https://twitter.com/PDChina"

for homepage in sites:
    pic_list = getpic(homepage)
    downpic(pic_list)
