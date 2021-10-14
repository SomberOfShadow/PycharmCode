import time

from bs4 import BeautifulSoup
from selenium import webdriver

# topic time format: 3h, 5d, Apr 3, Dec'18
# reply time format: just now, 1 minute, 14 minutes,1 hour, 3 hours, 1 day, 5 days, May 15, Dec 19, '18


# 配置option使浏览器后台打开
# topic_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/topics"
topic_url = "https://discourse.lmera.ericsson.se/u/eenheni/activity/topics"

driver = webdriver.PhantomJS()

driver.get(topic_url)

# option = webdriver.ChromeOptions()
# option.add_argument('headless')  # setting option
# driver = webdriver.Chrome(options=option)
# driver.get(topic_url)


# html = driver.page_source
# print(html)
# soup = BeautifulSoup(html,'lxml',from_encoding="utf-8")
# print(soup)

user = driver.find_element_by_class_name("user-right")

# print("user:", user.size)
# print(user.text)

div = user.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[0]\
    .find_elements_by_tag_name("div")

# div = user.find_element_by_tag_name("div").find_elements_by_tag_name("div")[0]\
#     .find_elements_by_tag_name("div")

trs = div[0].find_elements_by_tag_name("table")[0].find_elements_by_tag_name("tr")
# print(len(trs))

# 获取单个time， just for test
tds = trs[0].find_elements_by_tag_name("td")
print(len(tds))
print("time:", tds[4].text)

# 获取时间戳（毫秒）
data_time = tds[4].find_element_by_tag_name("span").get_attribute("data-time")
print("data-time:", data_time)


# get all time, append a list
# topic_time_list = []
#
# for tr in trs:
#     tds = tr.find_elements_by_tag_name("td")
#     topic_time_list.append(tds[4].text)
#
# print("topic nums:", len(topic_time_list))
driver.close()
