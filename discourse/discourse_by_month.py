import datetime
from selenium import webdriver

"""
Scores are calculated based on the following parameters:
Topics: each topic is 2 points
Replies: each reply is 1 point
Solutions: each solution is 3 points
"""

# PDLENCRDVT Group members and EIDS:

# "Maxwell MA:maxwell", 替换 "Maxwell MA:exiimaa"
PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
                                     "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
                                     "Maxwell MA:maxwell","Ning ZHANG N:enigzhg", "Peng ZHOU:ezhopen",
                                     "Tao Sha:eshatao","Yehui WANG:eyehwan","YiMing Gong:EYIMGON1", "Ying FENG:efeying"]

# test example
# PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn"]

score_list = []
topic_list = []
reply_list = []
solution_list = []

solution_time = datetime.datetime.now()
year = solution_time.year
month = solution_time.month
day = solution_time.day


# Monthly statistics about topics and replies

def get_topic_reply(topic_reply_monthly_url, EID):

    print("topic and reply url:" + topic_reply_monthly_url)

    # 配置option使Chrome浏览器后台打开
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    browser = webdriver.Chrome(options=option)
    browser.get(topic_reply_monthly_url)
    # browser.implicitly_wait(10)

    topic_reply_list = browser.find_elements_by_class_name("number")
    number = len(topic_reply_list)
    # 统计topic和reply数量
    if number > 0:
        topic_number = topic_reply_list[2].text
        reply_number = topic_reply_list[3].text
    else:
        print("获取topics和replies失败,重新获取！")
        browser.get(topic_reply_monthly_url)
        topic_reply_list = browser.find_elements_by_class_name("number")

    # 保存topic、reply
    topic_list.append(topic_number)
    reply_list.append(reply_number)

    # print("length:" + str(len(topic_reply_list)))
    print("EID:" + EID)
    if len(topic_reply_list) > 0:
        print("Topics:" + topic_reply_list[2].text)
        print("Replies:" + topic_reply_list[3].text)

    browser.close()


# get solution all

def get_solution(solution_url):
    print("solution url :" + solution_url)

    # 配置option使Chrome浏览器后台打开
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    browser = webdriver.Chrome(options=option)

    browser.get(solution_url)

    # 查找solution所在的class:uesr-right, solution数量就是uesr-right下的元素个数, 要做异常检查机制

    solution_class = browser.find_elements_by_class_name("user-right")

    # print(browser.page_source)

    # m每个solution包括四个属性值：time/catagory/title/excerpt
    time_list = solution_class[0].find_elements_by_class_name("time")

    length = len(time_list)

    # 打印每个人solution个数
    print("Solution numbers:" + str(length))
    print("#########")
    # 保存solution
    solution_list.append(length)

    browser.close()


# get solution by month

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

    # 下面对solution按月统计
    length = transfer_time(time_list)

    # 打印每个人solution个数
    print("Solution numbers:" + str(length))
    print("#########")
    # 保存solution
    solution_list.append(length)

    browser.close()


# 对solution的时间进行处理, 主要有以下几种格式：
# 3 days  表示在一个月内-->2019-03-19
# Mar 13  表示今年的月份和日期-->2019-03-13
# Oct 17, '18 表示18年的月份和日期 -->2018-10-17

def transfer_time(time_list):
    # print(time_list)
    # 获取当前的年/月/日
    # solution_time = datetime.datetime.now()
    # year = solution_time.year
    # month = solution_time.month
    # day = solution_time.day

    # 初始化solution的年/月/日
    solution_year = year
    solution_month = month
    solution_day = day

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
        # 2. Mar 13
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
        # 3. Dec 17, '18
        else:
            print("third case, original time:" + tm.text)
            # 如果是上一年的12月份且日期大于今日，那么算在统计月份内
            if (year - int(str(tm.text).split("'")[1]) == 1) \
              and (str(tm.text).split(",")[0].split(" ")[0] == "Dec") \
              and int((str(tm.text).split(",")[0].split(" ")[1])) >= day:
                solution_number += 1
    return solution_number


# 主函数
if __name__ == '__main__':

    # Each member of the statistical group PDLENCRDVT

    # for member in PDLENCRDVT_MEMBERS_NAMES_AND_EIDS:
    for i in range(len(PDLENCRDVT_MEMBERS_NAMES_AND_EIDS)):

        EID = (PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1])
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"

        solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        get_topic_reply(topic_reply_monthly_url, EID)

        # get_solution(solution_url)
        get_solution_by_month(solution_url)

    for i in range(len(solution_list)):
        topics = topic_list[i]
        replies = reply_list[i]
        solutions = solution_list[i]

        score = int(topics) * 2 + int(replies) * 1 + int(solutions) * 3
        EID = PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1]
        score_list.append("EID:" + EID + " Topics:" + str(topics) + " Replies:" + str(replies) + " Solutions:" + str(solutions) + " Score:" + str(score))

print("下面是每个成员的EID/topic/reply/solution/score:")
print(score_list)

#画图 

# 将数据写入文件,文件名按时间命名

path = "C:\\MySoftWare\\Pycharm\\PycharmTest\\discourse\\score_" + year+ "_" + "month" + "_" + day + ".txt"
with open(path, 'w') as fh:
    for i in range(len(score_list)):
        fh.write(score_list[i] + "\n")
    fh.close()
print("信息写入完成!")




