import datetime
score_list = ['EID:ebinwwu Topics:2 Replies:28 Solutions:2 Score:38', 'EID:ewameil Topics:1 Replies:0 Solutions:0 Score:2',
              'EID:edanchn Topics:3 Replies:10 Solutions:0 Score:16', 'EID:eenheni Topics:0 Replies:1 Solutions:1 Score:4',
              'EID:EHUNJNG Topics:0 Replies:10 Solutions:2 Score:16', 'EID:EIZLALH Topics:1 Replies:0 Solutions:0 Score:2',
              'EID:maxwell Topics:0 Replies:0 Solutions:0 Score:0', 'EID:ezhopen Topics:0 Replies:1 Solutions:0 Score:1',
              'EID:EYIMGON1 Topics:1 Replies:8 Solutions:0 Score:10','EID:efeying Topics:0 Replies:2 Solutions:0 Score:2']
EID_list = []
topic_list = []
reply_list = []
solution_list = []
score = []

solution_time = datetime.datetime.now()
year = solution_time.year
month = solution_time.month
day = solution_time.day

for i in range(len(score_list)):
    EID_list.append(score_list[i].split(" ")[0].split(":")[1])
    topic_list.append(int(score_list[i].split(" ")[1].split(":")[1]))
    reply_list.append(int(score_list[i].split(" ")[2].split(":")[1]))
    solution_list.append(int(score_list[i].split(" ")[3].split(":")[1]))
    score.append(int(score_list[i].split(" ")[4].split(":")[1]))

# print(EID_list)
# print(topic_list)
# print(reply_list)
# print(solution_list)
# print(score)

import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-

# index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
bar_width = 0.5

rects = plt.bar(index, score, 0.5, label='score', tick_label=EID_list)

# rects1 = plt.bar(index, score, 0.4, label='score')
#
# for i in range(len(index)):
#     index[i] = index[i] + bar_width
# rects2 = plt.bar(index, topic_list, 0.4, label='topic')
#
# for i in range(len(index)):
#     index[i] = index[i] + bar_width
# rects3 = plt.bar(index, reply_list, 0.4, label='reply')
#
# for i in range(len(index)):
#     index[i] = index[i] + bar_width
# rects4 = plt.bar(index, solution_list, 0.4, label='solution', tick_label=EID_list)



# params

# x: ?????????x???
# y?????????????????????
# width????????????????????? ?????????0.8
# bottom??????????????????y????????? ?????????0
# align???center / edge ??????????????????x?????????????????????????????????x??????????????????

plt.legend()

# X/Y ?????????
if month ==1:
    plt.xlabel("Period: " + str(year-1) + "-" + str(12) + "-" + str(day) + " to " + str(year) + "-" + str(
        month) + "-" + str(day))
else:
    plt.xlabel("Period: from " + str(year) + "-" + str(month - 1) + "-" + str(day) + " to " + str(year) + "-" + str(
        month) + "-" + str(day))

plt.ylabel('score')


# title
plt.title(u'Discourse Score')



# ??????x?????????
# plt.xticks(index, EID_list)


plt.xticks(rotation=45) # ??????EID??????90???

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')

add_labels(rects)
# add_labels(rects1)
# add_labels(rects2)
# add_labels(rects3)
# add_labels(rects4)

# plt.savefig('C:\Discourse Results\h.png', dpi=200)
# plt.savefig('C:\Discourse Results\h.png', bbox_inches='tight', dpi=100)
# plt.savefig('double_histogram.png', bbox_inches='tight', dpi=100)
plt.savefig('double_histogram.png', dpi=100)
# plt.savefig('C:\Discourse Results\h.png', bbox_inches=None)
plt.show()





