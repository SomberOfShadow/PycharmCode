import datetime
import os
import sys

import win32com.client as win32

# print("Whether to customize input time：Y/N")
# user_defined = input()
user_defined = sys.argv[0]
if user_defined == "Y" or user_defined == "y":
    print("Please input year:")
    year = int(input())
    print("Please input month:")
    month = int(input())
    print("Please input day:")
    day = int(input())
else:
    solution_time = datetime.datetime.now()
    year = solution_time.year
    month = solution_time.month
    day = solution_time.day


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

    toAddress = 'hengtai.nie@ericsson.com'

    mail.To = toAddress
    mail.Subject = sub
    mail.Body = body
    mail.Send()


# send email automically with attachments
def sendmail():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    sub = 'Discourse Score on ' + str(month) + '-' + str(day) + ',' + str(year)
    body = 'Hi, \n' \
           'This is score result on discourse on ' + str(month) + '-' + str(day) + ',' + str(
        year) + ', and please note it. \n' \
                'BRs \n' \
                'Hengtai Nie'

    # 可以使用循环列表逐个发送
    # receivers = ['1904719059@qq.com', 'hengtai.nie@ericsson.com']

    # following receiver's address format
    toAddress = 'hengtai.nie@ericsson.com'
    # toAddress = '1904719059@qq.com' + ';' + 'hengtai.nie@ericsson.com'
    # toAddress = 'tao.sha@ericsson.com' + ';' + 'ning.n.zhang@ericsson.com'
    # cc address list
    # cc = '1904719059@qq.com' + ';' + 'just649@gmail.com'

    # mail.To = receivers
    mail.To = toAddress
    mail.Subject = sub
    mail.Body = body

    # current dir
    abs_folder = os.path.abspath('.') + "\\discourse_result"

    txt_path = abs_folder + "\\" + str(year) + "_" + str(month) + "_" + str(
        day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse.txt"
    png_path = abs_folder + "\\" + str(year) + "_" + str(month) + "_" + str(
        day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse_score.png"

    # specify a dir
    # txt_path = "C:\\MySoftWare\\PycharmTest\\mk_folder\\" + str(year) + "_" + str(month) + "_" + str(
    #     day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse.txt"
    # png_path = "C:\\MySoftWare\\PycharmTest\\mk_folder\\" + str(year) + "_" + str(month) + "_" + str(
    #     day) + "\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse_score.png"

    # 这里增加一个检测 是否存在要发送的文件，如果有则发送，如果没有则发送一个fail的提示
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


if __name__ == '__main__':
    sendmail()
