import requests
import re
from multiprocessing import Pool


# 爬取校花网上所有校花照片

def getpage(url):
    response = requests.get(url)
    html = response.text
    return html


def prase(html):
    imgurls_names = re.findall(r'alt="(.+?)".+?(/d/file/.+?\.jpg)', html)
    # return imgurls_names
    for imgurls_name in imgurls_names:
        print(imgurls_name)
       # exit
        # yield imgurls_name


def writef(item):
    name, img_url = item[0], item[1]

    img_response = requests.get('http://www.xiaohuar.com' + img_url)

    img_data = img_response.content
    print('下载图片 ' + name + ' ing')
    with open(r'C:\MySoftWare\Pycharm\PycharmTest\InternetWormTest\pics\xiaohua\%s.jpg' % name, 'wb') as f:
        f.write(img_data)
    print('下载图片 ' + name + ' done')


# 替换路径里的非法字符
def strip(path):
    path = re.sub(r'[? \\*|"<>:/]', '', str(path))
    return path


def main(page):
    url = 'http://www.xiaohuar.com/list-1-' + str(page) + '.html'
    html = getpage(url)
    # print(html)
    for item in prase(html):
        print("item", item)
        # writef(item)


if __name__ == '__main__':
    # main()
    # for i in range(3):
    #     main(i)
    pool = Pool()
    pool.map(main, [i for i in range(20)])
    pool.close()
    pool.join()
