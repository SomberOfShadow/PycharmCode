import argparse
import datetime
import os
import time
import matplotlib.pyplot as plt
import win32com.client as win32
from selenium import webdriver

# import Selenium2Library
# s = Selenium2Library.Selenium2Library()
# s.open_browser("localhost:7080", "firefox")
# source = s.get_source()


# main function
from selenium.webdriver import Proxy, DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType

if __name__ == '__main__':
    # "https://discourse.lmera.ericsson.se/u?name=eenheni&period=monthly"
    topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=eenheni&period=monthly"
    solved_url = "https://discourse.lmera.ericsson.se/u/ennheni/activity/solved"

    # use PhantomJS
    # driver = webdriver.PhantomJS()

    # use firefox headless mode
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument('--headless')
    # webdriver.FirefoxOptions()
    # driver = webdriver.Firefox(options=firefox_options)

    # Chrome browser

    # polipo_proxy = "127.0.0.1:8124"
    # proxy = Proxy({
    #     'proxyType': ProxyType.MANUAL,
    #     'httpProxy': polipo_proxy,
    #     'ftpProxy': polipo_proxy,
    #     'sslProxy': polipo_proxy,
    #     'noProxy': ''
    # })
    # capabilities = dict(DesiredCapabilities.CHROME)
    # proxy.add_to_capabilities(capabilities)
    # capabilities['acceptSslCerts'] = True
    # capabilities['acceptInsecureCerts'] = True

    option = webdriver.ChromeOptions()

    option.add_argument(
        'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

    option.add_argument('headless')  # setting option
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--disable-gpu')
    # option.add_argument('--window-size=1280,1000')
    option.add_argument('--allow-insecure-localhost')
    option.add_argument('--allow-running-insecure-content')

    option.add_argument("--ignore-ssl-errors=true");
    option.add_argument("--ssl-protocol=any");
    # option.add_argument(
    #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    #

    driver = webdriver.Chrome(options=option)




    # use PhantomJS
    # driver = webdriver.PhantomJS()



    print("topic and reply url:" + topic_reply_monthly_url)

    # driver.implicitly_wait(5)

    driver.get(topic_reply_monthly_url)
    # driver.implicitly_wait(5)
    # js = "var q=document.documentElement.scrollTop=100000"
    # for i in range(3):
    #     driver.execute_script(js)
    #     time.sleep(2)
    print(driver.page_source)
    topic_reply_list = driver.find_element_by_class_name("users-page")
    # print(topic_reply_list.text)
    # topic_reply_list = driver.find_elements_by_class_name("number")
    # topic_number = topic_reply_list[2].text
    # topic_number = topic_reply_list[3].text
    # print("topic number:" + topic_number)


    driver.close()

