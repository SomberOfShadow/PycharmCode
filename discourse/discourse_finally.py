import datetime
from selenium import webdriver
import matplotlib.pyplot as plt

"""
Scores are calculated based on the following parameters:
Topics: each topic is 2 points
Replies: each reply is 1 point
Solutions: each solution is 3 points
Scores = 2*Topics + Replies + 3*Solutions
"""

# PDLENCRDVT Group members and EIDS:
# replace "Maxwell MA:maxwell" with "Maxwell MA:exiimaa"
# PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
#                                      "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
#                                      "Maxwell MA:maxwell","Ning ZHANG N:enigzhg", "Peng ZHOU:ezhopen",
#                                      "Tao Sha:eshatao","Yehui WANG:eyehwan","YiMing Gong:EYIMGON1", "Ying FENG:efeying"]

# Finally Members
PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
                                     "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
                                     "Maxwell MA:maxwell", "Peng ZHOU:ezhopen","YiMing Gong:EYIMGON1", "Ying FENG:efeying"]

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

    # Configure option to open the Chrome browser implicitly
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # setting option
    browser = webdriver.Chrome(options=option)
    browser.get(topic_reply_monthly_url)

    topic_reply_list = browser.find_elements_by_class_name("number")
    number = len(topic_reply_list)

    # if number is 0, get it again
    if number > 0:
        topic_number = topic_reply_list[2].text
        reply_number = topic_reply_list[3].text
    else:
        count = 3
        while(count > 0):
            print("Fail to get topics and replies, trying again ... please wait " + count + " times !")
            browser.close()
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            browser = webdriver.Chrome(options=option)
            browser.get(topic_reply_monthly_url)

            topic_reply_list = browser.find_elements_by_class_name("number")
            topic_number = topic_reply_list[2].text
            reply_number = topic_reply_list[3].text
            count -= 1
            number = len(topic_reply_list)
            if number > 0:
                 count = -1

    # append topic and reply to the list
    topic_list.append(topic_number)
    reply_list.append(reply_number)

    print("EID:" + EID)
    if len(topic_reply_list) > 0:
        print("Topics:" + topic_reply_list[2].text)
        print("Replies:" + topic_reply_list[3].text)

    browser.close()


# get solution by month

def get_solution_by_month(solution_url):
    print("solution url :" + solution_url)

    # Configure option to open the Chrome browser implicitly
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # setting option
    browser = webdriver.Chrome(options=option)

    browser.get(solution_url)

    # find class:uesr-right, the number of solution is equal to the length of uesr-right
    solution_class = browser.find_elements_by_class_name("user-right")

    # if fail to get solution, try to get it again
    if len(solution_class) <= 0:
        print("fail to get solution, trying again ... please wait !")
        browser.close()
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # setting option
        browser = webdriver.Chrome(options=option)

        browser.get(solution_url)
        solution_class = browser.find_elements_by_class_name("user-right")

    # each solution has four properties：time/catagory/title/excerpt
    time_list = solution_class[0].find_elements_by_class_name("time")

    # get solution by month
    length = transfer_time(time_list)

    # print solution number
    print("Solution numbers:" + str(length))
    print("#########")
    # append solution to the list
    solution_list.append(length)
    browser.close()


# There are several main formats for processing solution time:
# 3 days or 5 hours  -->2019-03-19
# Mar 13  -->2019-03-13
# Oct 17,'18  -->2018-10-17

def transfer_time(time_list):
    # Get the current year/month/day
    solution_time = datetime.datetime.now()
    year = solution_time.year
    month = solution_time.month
    day = solution_time.day

    # init solution year/month/day
    solution_year = year
    solution_month = month
    solution_day = day

    solution_number = 0
    days = "days"
    dayy = "day"
    hours = "hours"
    split_char = ","

    # Judging whether time belongs to the current month
    for tm in time_list:

        # 1. 3 days /1 day /5 hours
        if days in tm.text or dayy in tm.text or hours in tm.text:
            print("first case, original time:" + tm.text)
            solution_number += 1
        # 2. Mar 13
        elif not(split_char in tm.text) and not(days in tm.text) :
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
            #  solution_time: Feb 21 or Mar 12  Toady: Mar 19 , then Feb 21 and Mar 12 is included
            if ((month - solution_month) == 1 and day <= solution_day) or ((month - solution_month) == 0 and day >= solution_day):
                solution_number += 1
        # 3. Dec 17, '18
        else:
            print("third case, original time:" + tm.text)

            # If it is December of the previous year and the date is larger than today,
            # then count in the statistical month.

            if (year - int(str(tm.text).split("'")[1]) == 1) \
              and (str(tm.text).split(",")[0].split(" ")[0] == "Dec") \
              and int((str(tm.text).split(",")[0].split(" ")[1])) >= day:
                solution_number += 1
    return solution_number


# Drawing Histogram
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
    pic_name = str(year) + "_" + str(month) + "_" + str(day) + "_discourse_score.png"

    # gcf: Get Current Figure
    fig = plt.gcf()
    plt.show()
    fig.savefig(pic_name, dpi=100)
    print("Histogram is saved！")


# save information

def save_discourse():
    path = str(year) + "_" + str(month) + "_" + str(day) + "_discourse.txt"
    with open(path, 'w') as fh:
        for i in range(len(score_list)):
            fh.write(score_list[i] + "\n")
        fh.close()
    print("Information is saved successfully!")


# main function
if __name__ == '__main__':

    # Each member of the statistical group PDLENCRDVT

    for i in range(len(PDLENCRDVT_MEMBERS_NAMES_AND_EIDS)):

        EID = (PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1])
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"

        solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        get_topic_reply(topic_reply_monthly_url, EID)

        get_solution_by_month(solution_url)

    for i in range(len(solution_list)):
        topics = topic_list[i]
        replies = reply_list[i]
        solutions = solution_list[i]

        score = int(topics) * 2 + int(replies) * 1 + int(solutions) * 3
        EID = PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1]
        score_list.append("EID:" + EID + " Topics:" + str(topics) + " Replies:" + str(replies) + " Solutions:" + str(solutions) + " Score:" + str(score))

print("Each member's statistics:")
print(score_list)

# Write data to a file, named by time
save_discourse()

# Draw the histogram of each person's discourse score.
plot_score(score_list)