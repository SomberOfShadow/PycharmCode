import time

from selenium import webdriver

# topic time format: 3h, 5d, Apr 3, Dec'18
# reply time format: just now, 1 minute, 14 minutes, 3 hours, 1 day, 5 days, May 15, Dec 19, '18


# 配置option使浏览器后台打开
driver = webdriver.PhantomJS()

# driver.maximize_window()
# driver.set_window_size(1920,1080)
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
reply_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/replies"

driver.get(reply_url)

# 参考地址：https://www.cnblogs.com/yestreenstars/p/5548101.html
# 通过js1可以获取body对象的高度，通过js2可以下拉滚动条。
# 先将上一次获取的body对象的高度（old_scroll_height）设为0，然后获取最新的body对象的高度，
# 跟上一次获取的进行比较，如果比上一次的值大，就把最新的值赋值给old_scroll_height，
# 然后下拉滚动条，休眠3秒钟，再循环比较，直到最新的值不比上一次的值大为止。
js1 = 'return document.body.scrollHeight'
js2 = 'window.scrollTo(0, document.body.scrollHeight)'
old_scroll_height = 0
while (driver.execute_script(js1) > old_scroll_height):
    old_scroll_height = driver.execute_script(js1)
    driver.execute_script(js2)
    time.sleep(3)

user = driver.find_element_by_class_name("user-right")
div = user.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")
# print(len(div))

time_list = user.find_elements_by_tag_name("div")[0].find_elements_by_class_name("time")

# for tl in time_list:
#     print("time:", tl.text)

print("time list length:", len(time_list))

driver.close()
