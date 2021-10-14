import datetime

from selenium import webdriver

# time = datetime.datetime.now()
# year = time.year
# month = time.month
# day = time.day

year = 2019
month = 6
day = 12


def get_solution_by_month(solution_url):

    # driver = webdriver.PhantomJS()

    # use firefox headless mode
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)

    driver.get(solution_url)

    print("date to query solved:", year, month, day)
    print("solution url :" + solution_url)
    # find class:uesr-right, the number of solution is equal to the length of uesr-right
    solution_class = driver.find_elements_by_class_name("user-right")
    print("type:", type(solution_class))

    # if fail to get solution, try to get it again
    # if len(solution_class) <= 0:
    #     flag = 3
    #     while flag > 0:
    #         print("fail to get solution, trying again ... please wait " + str(3-flag+1) + " times !")
    #         driver.close()
    #         driver = webdriver.PhantomJS()
    #         driver.get(solution_url)
    #         solution_class = driver.find_elements_by_class_name("user-right")
    #         flag -= 1
    #         if len(solution_class) <= 0:
    #             flag = -1
    #             break

    # each solution has four properties：time/catagory/title/excerpt
    time_list = solution_class[0].find_elements_by_class_name("time")
    print("time_list:", time_list)
    solved_stamp_list = []

    for sl in time_list:
        solved_time_stamp_mill_seconds = sl.find_element_by_tag_name("span").get_attribute("data-time")
        seconds = int(solved_time_stamp_mill_seconds) / 1000
        solved_stamp_list.append(seconds)
        print(seconds)



if __name__ == '__main__':
    # solved_url = "https://discourse.lmera.ericsson.se/u/efeying/activity/solved"
    solved_url = "https://discourse.lmera.ericsson.se/u/eenheni/activity/solved"
    get_solution_by_month(solved_url)