# 爬取网站http://www.xiaohuar.com/hua/的1-20页大学校花的图片
# 流程： url--> 匹配得到校花的图片地址--> 下载图片

# -*- coding: UTF-8 -*-
import re
import requests

# 爬虫类, 定义了几个功能函数
class Spider:
    def __init__(self):
        self.session = requests.Session()

    # 解析一个url
    def parse(self, url):
        response = self.session.get(url)
        html = response.text
        return html

    # 匹配一个页面上所有校花的图片和名字信息
    def get_url_item(self, html):
        img_urls_names = re.findall(r'href="(.*?)".+?alt="(.+?)".+?(/d/file/.+?\.jpg)', html)
        # img_urls_names = re.findall(r'class="img".*?href="(.*?)"', html, re.S)
        # print(img_urls_names)

        # 通过变成set的方式筛选掉重复的
        set_img_urls_names = set(img_urls_names)
        # print(set_img_urls_names)
        return set_img_urls_names

    # 下载图片
    def download(self, url, name):
        r = requests.get(url)
        path = "C:\MySoftWare\Pycharm\PycharmTest\InternetWormTest\pics\selfxiaohua\\" + name + ".jpg"
        print("path:", path)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")

##########################################################################################################################
    #     遍历每一个元素，每个元素的值包含三个字段，如下的形式：
    #     ('http://www.xiaohuar.com/p-1-2010.html', '聊城大学校花飞儿', '/d/file/20181216/9df718a54adae448c65f54246a581a19.jpg')
    #     图片地址：http://www.xiaohuar.com/d/file/20150108011048171.jpg
    #     http://www.xiaohuar.com/list-1-0.html, http://www.xiaohuar.com/list-1-1.html, ..., ...
##########################################################################################################################

if __name__ == '__main__':
    spider = Spider()
    # 下载第一到第二十页所有校花的图片
    for i in range(0, 20):
        website = "http://www.xiaohuar.com/list-1-" + str(i) + ".html"
        html = spider.parse(website)
        url_names = spider.get_url_item(html)
        # print(url_names)

        # 遍历每一个元素，每个元素的值包含三个字段，如下的形式：
        # ('http://www.xiaohuar.com/p-1-2010.html', '聊城大学校花飞儿', '/d/file/20181216/9df718a54adae448c65f54246a581a19.jpg')

        for imgurls_name in url_names:
            # print(imgurls_name[0])
            downlaod_url_posfix = imgurls_name[2]
            downlaod_url = "http://www.xiaohuar.com/" + downlaod_url_posfix
            # print(downlaod_url)
            spider.download(downlaod_url, imgurls_name[1])









