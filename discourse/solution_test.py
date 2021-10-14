from bs4 import BeautifulSoup
from selenium import webdriver

#
# driver = webdriver.Remote(
#   desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
#
# b = connect('htmlunit')

# 配置option使浏览器后台打开
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置option
browser = webdriver.Chrome(options=option)

# browser.implicitly_wait(10)
# # 正常打开浏览器
# browser = webdriver.Chrome()

# url = "https://discourse.lmera.ericsson.se/u/eenheni/activity/solved"
topic_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/topics"
browser.get(topic_url)

browser.switch_to.default_content()

# data = browser.page_source
# soup = BeautifulSoup(data, 'xml')
# print(soup.text)

# print(browser.page_source)
# user = driver.find_element_by_class_name("user-right")
# tt = user.find_elements_by_css_selector("[class='topic-list ember-view']")

# print(len(tt))

# table = user.find_elements_by_tag_name("div")

# print(len(table))


# topic = user.find_elements_by_tag_name("tbody")

# print(len(topic))
# .find_element_by_tag_name("div")
# trs = topic.find_elements(By.TAG_NAME("tbody")).find_elements(By.TAG_NAME("tr"))

# print(trs)
# lis.find_elements_by_class_name(By.CLASS_NAME("topic-list ember-view"))
# print(len(lis))
# for value in lis:
#     print(value.text)

# print(str(len(lis)))
# time_list = lis[0].find_elements_by_class_name("time")

# print("timelist:" + time_list)
# print(browser.page_source)


browser.close()
