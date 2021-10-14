
from selenium import webdriver
import datetime

"""
Scores are calculated based on the following parameters:
Topics: each topic is 2 points
Replies: each reply is 1 point
Solutions: each solution is 3 points
"""

# PDLENCRDVT Group members and EIDS:

# "Maxwell MA:maxwell", 替换 "Maxwell MA:exiimaa"
# PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
#                                      "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
#                                      "Maxwell MA:maxwell","Ning ZHANG N:enigzhg", "Peng ZHOU:ezhopen",
#                                      "Tao Sha:eshatao","Yehui WANG:eyehwan","YiMing Gong:EYIMGON1", "Ying FENG:efeying"]

# test example
PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["YiMing Gong:EYIMGON1", "Yehui WANG:eyehwan"]

# 对solution的时间进行处理, 主要有以下几种格式：
# 3 days  表示在一个月内-->2019-03-19
# Mar 13  表示今年的月份和日期-->2019-03-13
# Oct 17, '18 表示18年的月份和日期 -->2018-10-17

def transfer_time(time_list):
    # print(time_list)
    # 获取当前的年/月/日
    solution_time = datetime.datetime.now()
    # year = solution_time.year
    # month = solution_time.month
    # day = solution_time.day

    year = 18
    month = 1
    day = 3


    # 初始化solution的年/月/日
    solution_year = year
    solution_month = month
    solution_day = day

    # 要test 年末12月和年初1月，目前没法测试
    # solution_year = 2019
    # solution_month = 1
    # solution_day = 19

    solution_number = 0
    days = "days"
    split_char = ","

    # 转换时间成xxxx-xx-xx的格式
    for tm in time_list:

        # 1. 3 days
        if days in tm.text:
            print("first case, original time:" + tm.text)
            # 如果是在统计当月之内
            solution_number += 1
        #  2. Mar 13
        elif not(split_char in tm.text) and not(days in tm.text) :
        # elif (str(tm.text).find(split_char) < 0) and (str(tm.text).find(days) < 0):
            print("second case, original time:" + tm.text)
            solution_day = int(str(tm.text).split(" ")[1])
            solution_year = year
            solution_month = str(tm.text).split(" ")[0]
            if solution_month == "Jan":
                solution_month = 1
            elif solution_month == "Feb":
                solution_month = 2
            elif solution_month == "Mar":
                solution_month = 3
            elif solution_month == "Apr":
                solution_month = 4
            elif solution_month == "May":
                solution_month = 5
            elif solution_month == "Jun":
                solution_month = 6
            elif solution_month == "Jul":
                solution_month = 7
            elif solution_month == "Aug":
                solution_month = 8
            elif solution_month == "Ste":
                solution_month = 9
            elif solution_month == "Oct":
                solution_month = 10
            elif solution_month == "Nov":
                solution_month = 11
            else:
                solution_month = 12
            #  solution_time: Feb 21 or Mar 12  Toady: Mar 19 , 那么此时Feb 21和 Mar 12 都是在统计月份内的
            if ((month - solution_month) == 1 and day <= solution_day) or ((month - solution_month) == 0 and day >= solution_day):
                solution_number += 1
        # 3. Dec 4, '17
        else:
            print("third case, original time:" + tm.text)
            # 如果是上一年的12月份且日期大于今日，那么算在统计月份内
            if (year - int(str(tm.text).split("'")[1]) == 1) \
              and (str(tm.text).split(",")[0].split(" ")[0] == "Dec") \
              and int((str(tm.text).split(",")[0].split(" ")[1])) >= day:
                solution_number += 1

    print("Solutions:" + str(solution_number))
    print("#######")


# Monthly statistics about topics and replies

def get_solution_by_month(solution_url):
    print("solution url :" + solution_url)

    # 配置option使Chrome浏览器后台打开
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    browser = webdriver.Chrome(options=option)

    browser.get(solution_url)

    # 查找solution所在的class:uesr-right, solution数量就是uesr-right下的元素个数
    solution_class = browser.find_elements_by_class_name("user-right")

    # 如果获取solution失败,重新获取
    if len(solution_class) <= 0:
        print("获取solution失败，正在重新获取！")
        browser.get(solution_url)
        solution_class = browser.find_elements_by_class_name("user-right")
    # print(browser.page_source)

    # m每个solution包括四个属性值：time/catagory/title/excerpt
    time_list = solution_class[0].find_elements_by_class_name("time")
    # test_list = ["Dec 20", "Dec 2"]
    transfer_time(time_list)
    # transfer_time(test_list)

    browser.close()

# 主函数
if __name__ == '__main__':
    # Each member of the statistical group PDLENCRDVT

    # for member in PDLENCRDVT_MEMBERS_NAMES_AND_EIDS:
    for i in range(len(PDLENCRDVT_MEMBERS_NAMES_AND_EIDS)):

        EID = (PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1])
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"

        solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        get_solution_by_month(solution_url)
