"""
获取以下几个属性值：
Topics
Replies
全部字段值和对应的索引值：
Received -->0
Given  -->1
Topics -->2
Replies -->3
Viewed -->4
Read -->5
Visits -->6
"""

from selenium import webdriver

# 配置option使浏览器后台打开
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置option
browser = webdriver.Chrome(options=option)

# # 正常打开浏览器
# browser = webdriver.Chrome()
# url = "https://discourse.lmera.ericsson.se/u?name=Dianny%20chen"
# url = "https://discourse.lmera.ericsson.se/u?name=EENHENI"

month_url = "https://discourse.lmera.ericsson.se/u?name=efeying&period=monthly"

# month_url = "https://discourse.lmera.ericsson.se/u?name=Bin%20WU&period=monthly"
# browser.get(url)
browser.get(month_url)
lis = browser.find_elements_by_class_name("number")


print("Topics:" + lis[2].text)
print("Replies:" + lis[3].text)
# for value in lis:
#     print(value.text)

# print(str(len(lis)))

# print(browser.page_source)
browser.close()
