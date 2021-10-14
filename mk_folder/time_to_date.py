import time

# 1558469965688
data_time = time.localtime(1558469965.688)
date_time = time.strftime('%Y-%m-%d', data_time)
print("time", date_time)

# ms = 1558469965688/1000
# print(ms)

year = date_time.split("-")[0]
day = date_time.split("-")[2]
month = date_time.split("-")[1]

print("year cha:", int(year) - 2019)
print(month)
print(type(month))
chazhi = int(month) - 4
print(chazhi)

# list copy
reply = ["1", "2", "3"]
reply_copy = []

for i in range(0, 3):
    reply_copy.append(reply[i])

print("reply_copy:", reply_copy)

