from time import sleep

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

# Monthly statistics about topics and replies
def get_topic_reply(topic_reply_monthly_url, EID):

    print("topic and reply url:" + topic_reply_monthly_url)

    # 配置option使Chrome浏览器后台打开
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    browser = webdriver.Chrome(options=option)
    browser.get(topic_reply_monthly_url)

    topic_reply_list = browser.find_elements_by_class_name("number")

    # 统计topic和reply数量
    if (len(topic_reply_list) > 0):
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
    if (len(topic_reply_list) > 0):
        print("Topics:" + topic_reply_list[2].text)
        print("Replies:" + topic_reply_list[3].text)

    browser.close()


# get solution
def get_solution(solution_url, EID):
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


# 主函数
if __name__ == '__main__':
    # Each member of the statistical group PDLENCRDVT

    # for member in PDLENCRDVT_MEMBERS_NAMES_AND_EIDS:
    for i in range(len(PDLENCRDVT_MEMBERS_NAMES_AND_EIDS)):

        # EID = (member.split(":")[1])

        EID = (PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1])
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"

        solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        get_topic_reply(topic_reply_monthly_url, EID)

        get_solution(solution_url, EID)

    for i in range(len(solution_list)):
        topics = topic_list[i]
        replies = reply_list[i]
        solutions = solution_list[i]

        score = int(topics) * 2 + int(replies) * 1 + int(solutions) * 3
        EID = PDLENCRDVT_MEMBERS_NAMES_AND_EIDS[i].split(":")[1]
        score_list.append("EID:" + EID + " Topics:" + str(topics) + " Replies:" + str(replies) + " Solutions:" + str(solutions) + " Score:" + str(score))

print("下面打印信息:")
print(score_list)

# 将数据写入文件
path = "C:\\MySoftWare\\Pycharm\\PycharmTest\\discourse\\score.txt"
with open(path, 'w') as fh:
    for i in range(len(score_list)):
        # print("开始写入第" + str(i) + "行：")
        fh.write(score_list[i] + "\n")
    fh.close()
print("信息写入完成!")







