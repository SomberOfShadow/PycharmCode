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
                                     "Maxwell MA:maxwell",
                                     "Ning ZHANG N:enigzhg", "Peng ZHOU:ezhopen", "Tao Sha:eshatao",
                                     "Yehui WANG:eyehwan",
                                     "YiMing Gong:EYIMGON1", "Ying FENG:efeying"]
list_score = []

# Monthly statistics about topics and replies
def get_topic_reply(topic_reply_monthly_url, EID):
    browser.get(topic_reply_monthly_url)
    topic_reply_list = browser.find_elements_by_class_name("number")

    # 统计topic和reply数量
    topic_number = topic_reply_list[2].text
    reply_number = topic_reply_list[3].text

    print("topic and reply url:" + topic_reply_monthly_url)
    # print("length:" + str(len(topic_reply_list)))
    print("EID:" + EID)
    print("Topics:" + topic_reply_list[2].text)
    print("Replies:" + topic_reply_list[3].text)
    # print("############")

def get_solution(solution_url, EID):

    print("solution url :" + solution_url)
    browser.get(solution_url)
    solution_number = 0

    # 查找solution所在的class:uesr-right, solution数量就是uesr-right下的元素个数
    solution = browser.find_elements_by_class_name("user-right")

    # m每个solution包括四个属性值：time/catagory/title/excerpt
    time_list = solution[0].find_elements_by_class_name("time")
    solution_number = len(time_list)


    print("Solutions:" + str(solution_number))
    print("###########")


#  主函数
if __name__ == '__main__':
    # Each member of the statistical group PDLENCRDVT

    for member in PDLENCRDVT_MEMBERS_NAMES_AND_EIDS:
        # 配置option使Chrome浏览器后台打开
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option
        browser = webdriver.Chrome(options=option)

        # # 正常打开浏览器
        # browser = webdriver.Chrome()
        EID = (member.split(":")[1])
        topic_reply_monthly_url = "https://discourse.lmera.ericsson.se/u?name=" + EID + "&period=monthly"
        solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"

        get_topic_reply(topic_reply_monthly_url, EID)
        get_solution(solution_url, EID)

        browser.close()

# print("score:\n")
# print(list_score)

# 将数据写入文件
# path = "C:\\MySoftWare\\Pycharm\\PycharmTest\\discourse\\list_score.txt"
# with open(path, 'w') as fh:
#     for i in range(len(list_score)):
#         fh.write(list_score[i] + "\n")
#     fh.close()





