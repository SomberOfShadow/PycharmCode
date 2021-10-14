import datetime
import win32com.client as win32

time = datetime.datetime.now()
year = time.year
month = time.month
day = time.day

# 自动发送多附件多人邮件

def sendmail():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    # mail = outlook.CreateItem(win32.constants.olMailItem)

    sub = 'Discourse Score on ' + str(day) + ',' + str(month) + ',' + str(year)
    body = 'Hi, \n' \
           'This is score result on discourse on ' + str(month) + '-' + str(day) + ',' + str(year) + ', and please note it. \n' \
            'BR \n' \
            'Hengtai Nie'

    # 可以使用循环列表逐个发送
    # receivers = ['1904719059@qq.com', 'hengtai.nie@ericsson.com']

    # 收件人地址
    toAddress = '1904719059@qq.com' + ';' + 'hengtai.nie@ericsson.com'
    # toAddress = 'tao.sha@ericsson.com' + ';' + 'ning.n.zhang@ericsson.com'
    # 抄送人地址
    # cc = '1904719059@qq.com' + ';' + 'just649@gmail.com'

    # mail.To = receivers
    mail.To = toAddress

    mail.Subject = sub
    mail.Body = body

    # 这里增加一个检测 是否存在要发送的文件，如果有则发送，如果没有则发送一个fail的提示

    # txtPath = "C:\MySoftWare\Pycharm\PycharmTest\discourse\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse.txt"
    # pngPath = "C:\MySoftWare\Pycharm\PycharmTest\discourse\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse_score.png"
    testTxtPath = "C:\Discourse Results\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse.txt"
    testPngPath = "C:\Discourse Results\\" + str(year) + "_" + str(month) + "_" + str(day) + "_" + "discourse_score.png"
    mail.Attachments.Add(testTxtPath)
    mail.Attachments.Add(testPngPath)


    mail.Send()
    print("Send  Email Success!")

if __name__ == '__main__':
    sendmail()