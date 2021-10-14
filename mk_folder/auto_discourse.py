import datetime
import os


# 如果是统计很久之前的数据，难么topic、reply、solved的threshold应该设置的很大
print("Please input whether to customize time：Y/N?")
user_defined = input()  # Y/y/N/n


def execute_script(user_defined, year, month, day):
    calculate_script = ('python calculate_score.py ' + user_defined + " " + str(year) + " " + str(month) + " " + str(day))
    send_script = ('python send_score.py ' + user_defined + " " + str(year) + " " + str(month) + " " + str(day))

    is_calculate_success = os.system(calculate_script)
    print("Calculate result:", is_calculate_success)  # 打印执行结果 0表示 success ， 1表示 fail
    if is_calculate_success == 0:
        print("calculate script execute succes.")
        is_send_success = os.system(send_script)
        print("send result:", is_send_success)
        if is_send_success == 0:
            print("send script execute success.")


def input_parameters():
    if user_defined.lower() == "y":
        print("Please input year:")  # 2019
        year = input()
        print("Please input month:")  # 3 / 11
        month = input()
        print("Please input day:")  # 1 / 11
        day = input()

        execute_script(user_defined, year, month, day)
    else:
        time_today = datetime.datetime.now()
        year = time_today.year
        month = time_today.month
        day = time_today.day

        execute_script(user_defined, year, month, day)


if __name__ == '__main__':
    input_parameters()




