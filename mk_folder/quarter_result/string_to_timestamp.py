import time

# def str_to_timestamp(str_time=None, format='%Y-%m-%d %H:%M:%S'):
def str_to_timestamp(str_time=None, format='%Y-%m-%d'):
    if str_time:
        time_tuple = time.strptime(str_time, format)  # 把格式化好的时间转换成元祖
        result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
        return int(result)
    return int(time.time())


# print(str_to_timestamp('2019-04-27 07:01:46'))
# print(str_to_timestamp()) #1556349904


print(str_to_timestamp('2021-01-01'))
