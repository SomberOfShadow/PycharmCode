import time
import datetime


s = "Dec 17, '18"
print(s.split("'")[1])

#
# time.time()
# # print(time.localtime())
# print(datetime.date.today())
#
# local_time = time.localtime()
# str_time = time.strftime("%Y-%m-%d", local_time)
#
# print(str_time)
#
i = datetime.datetime.now()
string = int(str(i.year)[-2:])
print(int(str(i.year)[-2:]))
print(type(string))

# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是 %s" %i.day)
#
# # print ("当前的日期和时间是 %s" % i)
# # print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# # print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# # print ("当前小时是 %s" %i.hour)
# # print ("当前分钟是 %s" %i.minute)
# # print ("当前秒是  %s" %i.second)