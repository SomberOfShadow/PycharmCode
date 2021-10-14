import time

from selenium import webdriver

# change 1: get topic list
# change 2: get topic time
# change 3: use chrome to replace phantomJs

def pull_buttom(driver):
    js1 = 'return document.body.scrollHeight'
    js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    old_scroll_height = 0
    while (driver.execute_script(js1) > old_scroll_height):
        old_scroll_height = driver.execute_script(js1)
        driver.execute_script(js2)
        time.sleep(3)

topic_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/topics"
reply_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/replies";

# topic_url = "https://discourse.lmera.ericsson.se/u/eenheni/activity/topics"

# PhantomJs browser
# driver = webdriver.PhantomJS()

# Chrome browser
option = webdriver.ChromeOptions()
option.add_argument('headless')  # setting option
driver = webdriver.Chrome(options=option)



driver.get(topic_url)

pull_buttom(driver)

# print(driver.page_source)

topic_class = driver.find_elements_by_class_name("user-right")

div = topic_class[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name(
    "div")
# user = driver.find_element_by_class_name("user-table")
trs = div[0].find_elements_by_tag_name("table")[0].find_elements_by_tag_name("tbody")[0].find_elements_by_tag_name("tr")

print("trs:", len(trs))

topic_time_list = []
for tr in trs:
    tds = tr.find_elements_by_tag_name("td")
    time_stamp_mill_seconds = tds[3].find_element_by_tag_name("span").get_attribute("data-time")
    seconds = int(time_stamp_mill_seconds) / 1000
    topic_time_list.append(seconds)

print("time list size :", len(topic_time_list))

# driver.get(reply_url)
# pull_buttom(driver)
# reply_class = driver.find_elements_by_class_name("user-right")
# reply_time_list = reply_class[0].find_elements_by_tag_name("div")[0].find_elements_by_class_name("time")
#
# print("reply time list size :", len(reply_time_list))

driver.close()




