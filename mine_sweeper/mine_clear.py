from selenium import webdriver


url = "https://blizzard-cloud.rnd.ki.sw.ericsson.se/mine/mine.html?uniqueid=EENHENI-8Eh5ZCL2IpZFvre6lORfjnZD"

driver = webdriver.PhantomJS()

driver.get(url)

print(driver.page_source)