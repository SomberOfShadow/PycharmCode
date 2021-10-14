"""
获取solution数值：要考虑每个月的统计数字

# url = "https://discourse.lmera.ericsson.se/u/eenheni/activity/solved"
# url = "https://discourse.lmera.ericsson.se/u/efeying/activity/solved"
# url = "https://discourse.lmera.ericsson.se/u/lmcdeka/activity/solved"

# url = "https://discourse.lmera.ericsson.se/u/eshatao/activity/solved"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# "Maxwell MA:maxwell", 替换 "Maxwell MA:exiimaa"
PDLENCRDVT_MEMBERS_NAMES_AND_EIDS = ["Bin WU A:ebinwwu", "Daisy WANG M:ewameil", "Dianny Chen:edanchn",
                                     "Hengtai Nie:eenheni", "HuanJun Jiang:EHUNJNG", "Lily Zhao:EIZLALH",
                                     "Maxwell MA:maxwell",
                                     "Ning ZHANG N:enigzhg", "Peng ZHOU:ezhopen", "Tao Sha:eshatao",
                                     "Yehui WANG:eyehwan",
                                     "YiMing Gong:EYIMGON1", "Ying FENG:efeying"]

for member in PDLENCRDVT_MEMBERS_NAMES_AND_EIDS:

    # 配置option使浏览器后台打开
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    browser = webdriver.Chrome(options=option)
    # browser.implicitly_wait(5)

    # 正常打开浏览器
    # browser = webdriver.Chrome()
    EID = (member.split(":")[1])
    solution_url = "https://discourse.lmera.ericsson.se/u/" + EID + "/activity/solved"
    browser.get(solution_url)
    # browser.add_cookie(cookie_dict=cookie)
    # browser.get(solution_url)

    # 查找solution所在的class:uesr-right, solution数量就是uesr-right下的元素个数
    solution_class = browser.find_elements_by_class_name("user-right")

    # print(browser.page_source)
    for value in solution_class:
        # m每个solution包括四个属性值：time/catagory/title/excerpt
        time_list = value.find_elements_by_class_name("time")
        # 打印每个人solution个数
        print("EID:" + EID + " Solution numbers:" + str(len(time_list)))

        # 打印每个solution的时间点, 同时对solution的数量做一个判断
        if (len(time_list) > 0):
            for i in range(len(time_list)):
                print("第" + str(i + 1) + " 个solution" + "的time:" + time_list[i].text)
            print("#########")
        else:
            print("#########")
            # print("EID:" + EID + " Solution numbers:" + str(0))



browser.close()

