import requests        #导入requests包
url = 'https://blizzard-cloud.rnd.ki.sw.ericsson.se/mine/hitmine'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)