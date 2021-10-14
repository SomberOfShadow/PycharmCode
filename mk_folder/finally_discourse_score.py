import argparse
import datetime
import os
import time
import matplotlib.pyplot as plt
import win32com.client as win32
from selenium import webdriver


"""
Scores are calculated based on the following parameters:
Topics: each topic is 2 points
Replies: each reply is 1 point
Solutions: each solution is 3 points
Scores = 2*Topics + Replies + 3*Solutions
"""

# Members name & EID
PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
                                     "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
                                     "Maxwell MA:maxwell", "Peng ZHOU:ezhopen", "YiMing Gong:eyimgon",
                                     "Ying FENG:efeying", "Vince:ezhweix", "Joya:ejiaoya"]


# reply may be too much , so set a threshold, compare with reply numbers
# threshold_reply = 100
# threshold_topic = 30
# threshold_solved = 20

score_list = []
topic_list = []
reply_list = []
solve_list = []

# today date: year/month/day
date_today = datetime.datetime.now()
year = date_today.year
month = date_today.month
day = date_today.day

# usage For example:
#     'python finally_discourse_score.py -u y'
#     'python finally_discourse_score.py -u N -y 2019 -m 5 -d 31'
#     'python finally_discourse_score.py -u Y -y 2019 -m 5 -d 31 -r 120 -t 30 -s 30'
parser = argparse.ArgumentParser(description='The script is to calculate discourse score by monthly.')

# user defined date
# parser.add_argument('--year', '-y', required=True, help='year. e.g. 2019')
# parser.add_argument('--month', '-m', required=True, help='mohth. e.g. 5')
# parser.add_argument('--day', '-d', required=True, help='day. e.g. 2')

# default date
parser.add_argument('--year', '-y', default=int(year), help='default year')
parser.add_argument('--month', '-m', default=int(month), help='default month')
parser.add_argument('--day', '-d', default=int(day), help='default day')

# set threshold_reply/shreshold_topic/threshold_solved default value
parser.add_argument('--threshold_reply', '-r', default=100, type=int, help="default value is 100")
parser.add_argument('--threshold_topic', '-t', default=20, type=int, help="default value is 20")
parser.add_argument('--threshold_solved', '-s', default=20, type=int, help="default value is 20")

# set use which method to calculate score
parser.add_argument('--user_defined', '-u', choices=['Y', 'y', 'N', 'n'], default="N", type=str,
                    help='default value is N, if you want to calculate score on user-defined day'
                         'or choose second way to calculate score, it should be Y or y.')

args = parser.parse_args()

threshold_reply = args.threshold_reply
threshold_topic = args.threshold_topic
threshold_solved = args.threshold_solved

# user_defined = sys.argv[1]
user_defined = args.user_defined

# year = int(sys.argv[2])
year = int(args.year)

# month = int(sys.argv[3])
month = int(args.month)

# day = int(sys.argv[4])
day = int(args.day)

print("topic threshold:", threshold_topic)
print("reply threshold:", threshold_reply)
print("solved threshold:", threshold_solved)
print("user_defined:", user_defined)
print("calculate year:", year)
print("calculate month:", month)
print("calculate day:", day)

# if directly run this script, use following way to input parameters

# print("whether to cutomize date:")
# user_defined = input()
# if user_defined == "Y" or user_defined == "y":
#     print("Please input year:")
#     year = int(input())  # example 2019
#     print("Please input month:")
#     month = int(input())  # example 4/11
#     print("Please input day:")
#     day = int(input())  # example 3/14
# else:
#     solution_time = datetime.datetime.now()
#     year = solution_time.year
#     month = solution_time.month
#     day = solution_time.day

abpath = os.path.abspath('.')
folder = abpath + "\\" + "discourse_result" + "\\" + str(year) + "_" + str(month) + "_" + str(day)


'''
#name: pull_buttom
#parameter: driver 
#function: pull html page to the bottom to get all content
'''


def pull_buttom(driver):
    js1 = 'return document.body.scrollHeight'
    js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    old_scroll_height = 0
    while (driver.execute_script(js1) > old_scroll_height):
        old_scroll_height = driver.execute_script(js1)
        driver.execute_script(js2)
        time.sleep(3)


'''
name: set_threshold()
parameters: stamp_list, threshold
function: set threshold respectively for topic, reply and solved
'''


def set_threshold(stamp_list, threshold):
    # set reply threshold
    origin_length = len(stamp_list)
    if threshold <= origin_length:
        final_length = threshold
    else:
        final_length = origin_length
    tmp_threshold_list = []
    for i in range(0, final_length):
        tmp_threshold_list.append(stamp_list[i])
    return tmp_threshold_list


'''
name: get_topic_by_month
parameters: topic_url, driver
function: count topic numbers by customized method
'''


def get_topic_by_month(topic_url, driver):
    # driver = webdriver.PhantomJS()
    # topic_url = "https://discourse.lmera.ericsson.se/u/ebinwwu/activity/topics"
    driver.get(topic_url)

    # print("date to query topic:", year, month, day)
    print("topic url:", topic_url)

    # 滚动条拉到页面最底部，获取所有的topic
    # scroll the bar to the bottom of the page to get all topics
    pull_buttom(driver)

    topic_class = driver.find_elements_by_class_name("user-right")
    try:
        div = topic_class[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")

    # except StaleElementReferenceException or IndexError:
    except :
        print("Fail to get div element, now to reget it.")
        # driver.implicitly_wait(4)
        # topic_class = driver.find_elements_by_class_name("user-right")
        div = topic_class[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")

    # each topic has one time; get all time, appending to a list
    topic_time_list = []
    # each tr include one topic information
    trs = div[0].find_elements_by_tag_name("table")[0].find_elements_by_tag_name("tbody")[0].find_elements_by_tag_name("tr")

    for tr in trs:
        tds = tr.find_elements_by_tag_name("td")
        time_stamp_mill_seconds = tds[3].find_element_by_tag_name("span").get_attribute("data-time")
        seconds = int(time_stamp_mill_seconds) / 1000
        topic_time_list.append(seconds)

    # # 滚动条拉到页面最底部，获取所有的topic
    # pull_buttom(driver)

    # 检查最新的threshold个topic
    topic_time_list_threshold = set_threshold(topic_time_list, threshold_topic)
    print("topic threshold:", len(topic_time_list_threshold))
    # get topic by month
    # length = transfer_topic_time(topic_time_list_threshold)
    length = transfer_stamp_time(topic_time_list_threshold)

    # append topic to the list
    topic_list.append(length)

    # print topic number
    print("Topics numbers:" + str(length))


'''
name: get_reply_by_month
parameters: reply_url, driver
function: count reply numbers by customized method
'''


def get_reply_by_month(reply_url, driver):
    # driver = webdriver.PhantomJS()
    driver.get(reply_url)
    # print("date to query reply:", year, month, day)
    print("reply url:", reply_url)

    pull_buttom(driver)

    reply_class = driver.find_elements_by_class_name("user-right")
    reply_time_list = reply_class[0].find_elements_by_tag_name("div")[0].find_elements_by_class_name("time")

    # 提取reply的时间戳
    reply_stamp_list = []

    for tl in reply_time_list:
        reply_time_stamp_mill_seconds = tl.find_element_by_tag_name("span").get_attribute("data-time")
        seconds = int(reply_time_stamp_mill_seconds) / 1000
        reply_stamp_list.append(seconds)

    pull_buttom(driver)
    reply_time_list_threshold = set_threshold(reply_stamp_list, threshold_reply)

    print("reply threshold:", len(reply_time_list_threshold))

    # get reply by month, only latest 100 replies included
    length = transfer_stamp_time(reply_time_list_threshold)

    # print reply number
    print("Reply numbers:" + str(length))

    # append reply numbers to the list
    reply_list.append(length)


'''
name: get_topic_reply
parameters: topic_reply_monthly_url, driver
function: get topic and reply numbers from discourse 
'''


def get_topic_reply(topic_reply_monthly_url, driver):
    driver.get(topic_reply_monthly_url)
    print("topic and reply url:" + topic_reply_monthly_url)

    # topic_reply_list = driver.find_elements_by_class_name("number")

    try:
        topic_reply_list = driver.find_elements_by_class_name("number")
        topic_number = topic_reply_list[2].text
    except IndexError:
        topic_reply_list = driver.find_elements_by_class_name("number")
        topic_number = topic_reply_list[2].text

    reply_number = topic_reply_list[3].text

    # append topic and reply to the list
    topic_list.append(topic_number)
    reply_list.append(reply_number)

    if len(topic_reply_list) > 0:
        print("Topics:" + topic_reply_list[2].text)
        print("Replies:" + topic_reply_list[3].text)


'''
name: get_solution_by_month
parameters: get_solution_by_month, driver
function: count solved numbers by customized method
'''


def get_solution_by_month(solution_url, driver):
    # print("date to query solved:", year, month, day)
    print("solved url :" + solution_url)

    driver.get(solution_url)

    # 滚动条拉到页面最底部，获取所有的solved
    pull_buttom(driver)

    # find class:uesr-right, the number of solution is equal to the length of uesr-right
    solution_class = driver.find_elements_by_class_name("user-right")

    # each solution has four properties：time/catagory/title/excerpt
    try:
        time_list = solution_class[0].find_elements_by_class_name("time")
    except IndexError:
        solution_class = driver.find_elements_by_class_name("user-right")
        time_list = solution_class[0].find_elements_by_class_name("time")

    solved_stamp_list = []

    for sl in time_list:
        solved_time_stamp_mill_seconds = sl.find_element_by_tag_name("span").get_attribute("data-time")
        seconds = int(solved_time_stamp_mill_seconds) / 1000
        solved_stamp_list.append(seconds)


    # 设置一个阈值，只验证最新的threshold个solved是否属于该月范围内
    solved_stamp_list_threshold = set_threshold(solved_stamp_list, threshold_solved)
    # get solution by month
    length = transfer_stamp_time(solved_stamp_list_threshold)
    print("solved threshold:", len(solved_stamp_list_threshold))

    # print solution number
    print("Solution numbers:" + str(length))
    print("++--------------------------------------------------------++")
    # append solution to the list
    solve_list.append(length)


'''
name: transfer_stamp_time
parameters: time_list
function: transfer time stamp to date format and judge monthly
'''


def transfer_stamp_time(time_list):
    multi_number = 0
    # Judging whether time belongs to the current month
    for tm in time_list:
        # time stamp format(milliseconds): 1558469965688
        # exampple : 1558469965.688-->2019-05-22
        # xxxxxxxxxxx--> 2018-12-15  2019-01-13
        data_time = time.localtime(tm)
        date_time = time.strftime('%Y-%m-%d', data_time)
        today_year = str(date_time).split("-")[0]
        today_month = str(date_time).split("-")[1]
        today_day = str(date_time).split("-")[2]
        print("origin time:", date_time)
        # 1. target:2019-05-22   origin:2019-05-25
        if int(year) == int(today_year) and int(month) == int(today_month) and int(today_day) <= int(day):
            print("#### first case:", date_time)
            multi_number += 1
        # 2. target:2019-05-22 origin:2019-06-20
        elif int(year) == int(today_year) and (int(month) - int(today_month)) == 1 and int(day) <= int(today_day):
            print("#### second case:", date_time)
            multi_number += 1
        # 3. target:2018-12-22   origin:2019-01-20
        else:
            if (int(year) - int(today_year) == 1 and int(today_month) == 12
                    and int(month) == 1 and int(day) <= int(today_day)):
                print("#### third case:", date_time)
                multi_number += 1
    return multi_number


# save .png file
'''
name: save_png_file
parameters: folder, png_name, fig
function: save figure of histogram as png_name.png file to specific folder
'''

def save_png_file(folder, png_name, fig):
    is_folder = os.path.exists(folder)
    if is_folder:
        print(folder + " already exist!")
        file_exist = os.path.isfile(png_name)
        if file_exist:
            print(png_name + " already exist, now to override it!")
            fig.savefig(png_name, bbox_inches='tight', dpi=150)
            print("Histogram is saved！")
        else:
            print(png_name + " not exist, now to create it!")
            fig.savefig(png_name, bbox_inches='tight', dpi=150)
            print("Histogram is saved！")
    else:
        print(folder + " not exist, now to create it!")
        os.makedirs(folder)
        if is_folder:
            print(png_name + " not exist, now to create it!")
            fig.savefig(png_name, bbox_inches='tight', dpi=150)
            print("Histogram is saved！")
        else:
            print("Create " + png_name + " failed, please check it!")


'''
name:plot_score
parameter: score_list
function: draw hisgram according to the score_list information
'''


def plot_score(score_list):
    EID_list = []
    discourse_list = []

    for i in range(len(score_list)):
        EID_list.append(score_list[i].split(" ")[0].split(":")[1])
        discourse_list.append(int(score_list[i].split(" ")[4].split(":")[1]))

    rects = plt.bar(EID_list, discourse_list, 0.5, label='score')
    plt.legend()

    # But it's important to note that month is 1 to make special judgments.
    if month == 1:
        plt.xlabel("Period: " + str(year - 1) + "-" + str(12) + "-" + str(day) + " to " + str(year) + "-" + str(
            month) + "-" + str(day))
    else:
        plt.xlabel("Period: from " + str(year) + "-" + str(month - 1) + "-" + str(day) + " to " + str(year) + "-" + str(
            month) + "-" + str(day))
    plt.ylabel('score')

    # title
    plt.title(u'Discourse Score')

    # Set the x-axis text to rotate 45 degrees to display
    plt.xticks(rotation=45)

    # Display text on a bar chart
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')

    # Charts are saved locally
    png_name = folder + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_discourse_score.png"
    # gcf: Get Current Figure
    fig = plt.gcf()
    # plt.show()
    # adjust figure size to prevent incompletence when saving
    fig.subplots_adjust(bottom=0.25)

    # save .png file
    save_png_file(folder, png_name, fig)


# save Statistics
def save_discourse():
    file_path = folder + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_discourse.txt"
    is_folder = os.path.exists(folder)
    if is_folder:
        print(folder + " already exist!")
        file_exist = os.path.isfile(file_path)
        if file_exist:
            print(file_path + " already exist, now to override it!")
            with open(file_path, 'w') as fh:
                for i in range(len(score_list)):
                    fh.write(score_list[i] + "\n")
                fh.close()
            print("Statistics is saved successfully!")
        else:
            print(file_path + " not exist, now to create it!")
            with open(file_path, 'w') as fh:
                for i in range(len(score_list)):
                    fh.write(score_list[i] + "\n")
                fh.close()
            print("Statistics is saved successfully!")
    else:
        print(folder + " not exist, now to create it!")
        os.makedirs(folder)
        is_folder = os.path.exists(folder)
        if is_folder:
            print(file_path + " not exist, now to create it!")
            with open(file_path, 'w') as fh:
                for i in range(len(score_list)):
                    fh.write(score_list[i] + "\n")
                fh.close()
            print("Statistics is saved successfully!")
        else:
            print("Create " + file_path + " failed, please check it!")


# send fail info to hengtai.nie@ercisson.com
def send_fail_info():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    sub = 'Discourse Score on ' + str(month) + '-' + str(day) + ',' + str(year) + " send failed."
    body = 'Hi, myself\n' \
           'The score result of discourse on ' + str(month) + '-' + str(day) + ',' + str(
        year) + ' send file failed, and please check it. \n' \
                'BR \n' \
                'Hengtai Nie'

    to_address = 'hengtai.nie@ericsson.com'

    mail.To = to_address
    mail.Subject = sub
    mail.Body = body
    mail.Send()


# send email automically with attachments
def send_mail():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    sub = 'Discourse Score on ' + str(month) + '-' + str(day) + ',' + str(year)
    body = 'Hi, \n' \
           'This is score result on discourse on ' + str(month) + '-' + str(day) + ',' + str(
        year) + ', and please note it. \n' \
                'BRs \n' \
                'Hengtai Nie'

    # to_address = 'hengtai.nie@ericsson.com'
    to_address = 'tao.sha@ericsson.com' + ';' + 'ning.n.zhang@ericsson.com'

    # mail.To = receivers
    mail.To = to_address
    mail.Subject = sub
    mail.Body = body

    # current dir
    abs_folder = os.path.abspath('.') + "\\discourse_result"

    txt_path = abs_folder + "\\" + str(year) + "_" + str(month) + "_" + str(
        day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse.txt"
    png_path = abs_folder + "\\" + str(year) + "_" + str(month) + "_" + str(
        day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse_score.png"

    file_exist = os.path.isfile(txt_path)
    png_exist = os.path.isfile(png_path)

    if file_exist and png_exist:
        mail.Attachments.Add(txt_path)
        mail.Attachments.Add(png_path)
        mail.Send()
        print("Send  Email Success!")
    else:
        print("File not exist, please check it!")
        send_fail_info()


# main function
if __name__ == '__main__':

    # Each member of the statistical group PDLENCRDVT

    for i in range(len(PDLENCRDVT_MEMBERS_NAMES_AND_EIDS)):
        EID = (PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1])

        topic_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/topics"
        reply_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/replies"
        # "https://discourse.lmera.ericsson.se/u?name=eenheni&period=monthly"
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"
        solved_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        # use PhantomJS
        # driver = webdriver.PhantomJS()

        # use firefox headless mode
        # firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument('--headless')
        # webdriver.FirefoxOptions()
        # driver = webdriver.Firefox(options=firefox_options)

        # Chrome browser
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # setting option
        driver = webdriver.Chrome(options=option)

        # toady or user-defined date
        if str(user_defined).lower() == "y":
            get_topic_by_month(topic_url, driver)
            get_reply_by_month(reply_url, driver)
            get_solution_by_month(solved_url, driver)
        else:
            get_topic_reply(topic_reply_monthly_url, driver)
            get_solution_by_month(solved_url, driver)

        driver.close()

    for i in range(len(solve_list)):
        topics = topic_list[i]
        replies = reply_list[i]
        solutions = solve_list[i]

        score = int(topics) * 2 + int(replies) * 1 + int(solutions) * 3
        EID = PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1]
        score_list.append("EID:" + EID.lower() + " Topics:" + str(topics) + " Replies:" + str(replies) + " Solutions:" + str(
            solutions) + " Score:" + str(score))

# print members' topic / reply/ solved and score
print("Each member's statistics:")
print(score_list)

# Write data to a file, named by time
save_discourse()

# Draw the histogram of each person's discourse score.
plot_score(score_list)

# send score result automatically
send_mail()