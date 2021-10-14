import time

from selenium import webdriver

# topic time format: 3h, 5d, Apr 3, Dec'18
# reply time format: just now, 1 minute, 14 minutes, 3 hours, 1 day, 5 days, May 15, Dec 19, '18


# 配置option使浏览器后台打开
driver = webdriver.PhantomJS()


driver.set_window_size(1920,1080)

try:
    # driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    reply_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/replies"

    # 处理滚动条，往下拉一些否则一个页面显示不了所有的reply
    # js = "var q=document.body.scrollTop=5000"
    # driver.execute_script(js)

    driver.get(reply_url)

    content = driver.page_source
    with open('page1.html', 'w', encoding='utf-8') as f:
        f.write(content)

    driver.save_screenshot('1.png')

    js = 'document.body.scrollTop=2000'
    driver.execute_script(js)

    time.sleep(4)
    driver.save_screenshot('2.png')

    user = driver.find_element_by_class_name("user-right")

    div = user.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")
    # print(len(div))

    time_list = user.find_elements_by_tag_name("div")[0].find_elements_by_class_name("time")

    for tl in time_list:
        print("time:", tl.text)

    print("time list length:",len(time_list))

    content = driver.page_source
    with open('page2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    # js = "var q=document.body.scrollTop=10000"
    # js = 'document.body.scrollTop=2000'
    # driver.execute_script(js)

    # print("滚动页面之后：")
    # div = user.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")
    # print(len(div))
    #
    # time_list = user.find_elements_by_tag_name("div")[0].find_elements_by_class_name("time")
    #
    # print("time list length:", len(time_list))
    #
    # for tl in time_list:
    #     print("time:", tl.text)


    # time = div[0].find_element_by_tag_name("div").find_element_by_class_name("time")
    # print(time.text)

except:
    driver.save_screenshot('screenshot.png')


driver.close()
