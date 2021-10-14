#!/usr/bin/python
# coding=utf-8


#使用第三方库：Pillow
import math
import operator
from functools import reduce
# python lib
import os
import sys
from PIL import Image
from PIL import ImageGrab
from pymouse import PyMouse
import threading
import win32gui
import win32api, win32con, win32com.client
import ctypes
import time
import chardet
import pythoncom
import pyHook


# 整屏的截图
def getAllScreenshot(screenshotPic):
    im = ImageGrab.grab()
    im.save(screenshotPic, 'jpeg')


# 特定区域的屏幕截图
def getAreaScreenshot(screenshotPic, pos_x, pos_y, delta):
    im = ImageGrab.grab((pos_x - delta, pos_y - delta, pos_x + delta, pos_y + delta))
    im.save(screenshotPic, 'jpeg')


# 敲击特定位置
def touchScreen(pos_x, pos_y):
    m = PyMouse()
    m.click(pos_x, pos_y)
    print("click done!")


# 判断两个图片是否相似度, 如果是相同的图片, 那么敲击对应的位置
def Rugular_Pic(pic_name1, pic_name2, pos_x, pos_y):
    image1 = Image.open(pic_name1)
    image3 = Image.open(pic_name2)

    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image3.histogram()
    # result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    if(result < 100):
        touchScreen(pos_x, pos_y);
    else :
        print("click not done!")



def startGameThread():
    saved_path_1 = os.path.join(sys.path[0], "pic", "1.jpeg")
    saved_path_2 = os.path.join(sys.path[0], "pic", "2.jpeg")
    saved_path_3 = os.path.join(sys.path[0], "pic", "3.jpeg")
    saved_path_4 = os.path.join(sys.path[0], "pic", "4.jpeg")
    saved_path_5 = os.path.join(sys.path[0], "pic", "5.jpeg")
    saved_path_6 = os.path.join(sys.path[0], "pic", "6.jpeg")
    saved_path_7 = os.path.join(sys.path[0], "pic", "7.jpeg")
    saved_path_8 = os.path.join(sys.path[0], "pic", "8.jpeg")
    saved_path_9 = os.path.join(sys.path[0], "pic", "9.jpeg")
    saved_path_10 = os.path.join(sys.path[0], "pic", "10.jpeg")
    saved_path_11 = os.path.join(sys.path[0], "pic", "11.jpeg")
    saved_path_12 = os.path.join(sys.path[0], "pic", "12.jpeg")
    saved_path_13 = os.path.join(sys.path[0], "pic", "13.jpeg")
    saved_path_14 = os.path.join(sys.path[0], "pic", "14.jpeg")
    saved_path_15 = os.path.join(sys.path[0], "pic", "15.jpeg")
    saved_path_16 = os.path.join(sys.path[0], "pic", "16.jpeg")
    saved_path_17 = os.path.join(sys.path[0], "pic", "17.jpeg")
    saved_path_18 = os.path.join(sys.path[0], "pic", "18.jpeg")
    saved_path_19 = os.path.join(sys.path[0], "pic", "19.jpeg")
    saved_path_20 = os.path.join(sys.path[0], "pic", "20.jpeg")
    saved_path_21 = os.path.join(sys.path[0], "pic", "21.jpeg")
    saved_path_22 = os.path.join(sys.path[0], "pic", "22.jpeg")
    saved_path_23 = os.path.join(sys.path[0], "pic", "23.jpeg")
    saved_path_24 = os.path.join(sys.path[0], "pic", "24.jpeg")
    saved_path_25 = os.path.join(sys.path[0], "pic", "25.jpeg")

    start = time.time();
    while 1:
        print("start game thread......")
        # 对屏幕上特定25块区域进行截图保存
        getAreaScreenshot(saved_path_1, 780, 310, 30)
        # 奖截图和check的图片进行比较,然后根据比较的结果进行敲击
        Rugular_Pic(saved_path_1, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 780, 310);
        getAreaScreenshot(saved_path_2, 880, 310, 30)
        Rugular_Pic(saved_path_2, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 310);
        getAreaScreenshot(saved_path_3, 980, 310, 30)
        Rugular_Pic(saved_path_3, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 980, 310);
        getAreaScreenshot(saved_path_4, 1080, 310, 30)
        Rugular_Pic(saved_path_4, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1080, 310);
        getAreaScreenshot(saved_path_5, 1180, 310, 30)
        Rugular_Pic(saved_path_5, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1180, 310);

        getAreaScreenshot(saved_path_6, 780, 410, 30)
        Rugular_Pic(saved_path_6, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 780, 410);
        getAreaScreenshot(saved_path_7, 880, 410, 30)
        Rugular_Pic(saved_path_7, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 410);
        getAreaScreenshot(saved_path_8, 980, 410, 30)
        Rugular_Pic(saved_path_8, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 980, 410);
        getAreaScreenshot(saved_path_9, 1080, 410, 30)
        Rugular_Pic(saved_path_9, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1080, 410);
        getAreaScreenshot(saved_path_10, 1180, 410, 30)
        Rugular_Pic(saved_path_10, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1180, 410);

        getAreaScreenshot(saved_path_11, 780, 510, 30)
        Rugular_Pic(saved_path_11, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 780, 510);
        getAreaScreenshot(saved_path_12, 880, 510, 30)
        Rugular_Pic(saved_path_12, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 510);
        getAreaScreenshot(saved_path_13, 980, 510, 30)
        Rugular_Pic(saved_path_13, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 980, 510);
        getAreaScreenshot(saved_path_14, 1080, 510, 30)
        Rugular_Pic(saved_path_14, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1080, 510);
        getAreaScreenshot(saved_path_15, 1180, 510, 30)
        Rugular_Pic(saved_path_15, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1180, 510);

        getAreaScreenshot(saved_path_16, 780, 610, 30)
        Rugular_Pic(saved_path_16, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 780, 610);
        getAreaScreenshot(saved_path_17, 880, 610, 30)
        Rugular_Pic(saved_path_17, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 610);
        getAreaScreenshot(saved_path_18, 980, 610, 30)
        Rugular_Pic(saved_path_18, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 980, 610);
        getAreaScreenshot(saved_path_19, 1080, 610, 30)
        Rugular_Pic(saved_path_19, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1080, 610);
        getAreaScreenshot(saved_path_20, 1180, 610, 30)
        Rugular_Pic(saved_path_20, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1180, 610);

        getAreaScreenshot(saved_path_21, 780, 710, 30)
        Rugular_Pic(saved_path_21, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 780, 710);
        getAreaScreenshot(saved_path_22, 880, 710, 30)
        Rugular_Pic(saved_path_22, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 710);
        getAreaScreenshot(saved_path_23, 980, 710, 30)
        Rugular_Pic(saved_path_23, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 980, 710);
        getAreaScreenshot(saved_path_24, 1080, 710, 30)
        Rugular_Pic(saved_path_24, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1080, 710);
        getAreaScreenshot(saved_path_25, 1180, 710, 30)
        Rugular_Pic(saved_path_25, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1180, 710);


        # 控制时间超过60秒的话直接停止退出
        stop = time.time();
        if (stop - start) > 60:
            sys.exit();

# 记录键盘值
def onKeyboardEvent(event):
    if 'F12' == event.Key:
        sys.exit()
    # return False表示不记录键盘输入值
    return False


def onMouseEvent(event):
    # 监听鼠标事件
    if 'mouserightdown' == event.MessageName.replace("\r\n", "").replace(" ", ""):
        sys.exit()
    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return False


# 点击键盘F12退出
def endGameThread():
    # 直接退出
    sys.exit();

    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 监听所有鼠标事件
    # hm.MouseAll = onMouseEvent
    # # 设置鼠标“钩子”
    # hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


def resetGameWindowPos():
    # 定义结构体，存储当前窗口坐标
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_int),
                    ('top', ctypes.c_int),
                    ('right', ctypes.c_int),
                    ('bottom', ctypes.c_int)]

    rect = RECT()
    # 获取当前窗口句柄
    while 1:
        HWND = win32gui.GetForegroundWindow()
        print (u"请打开游戏界面.....")
        HWND_Name = win32gui.GetWindowText(HWND)
        # print chardet.detect(HWND_Name)
        time.sleep(0.1)
        if '疯狂打地鼠' in HWND_Name.decode('GB2312').encode('utf-8'):
            print (u"已经打开了打开游戏界面.....")
            break
    # 获取当前窗口坐标
    ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))
    print ("当前窗口位置是:", ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect)))
    # 将窗口恢复至(0, 0)
    win32gui.SetWindowPos(HWND, None, 0, 0, rect.right - rect.left, rect.bottom - rect.top,
                          win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)


def main():
    # 重置游戏界面
    # resetGamePos()

    # 开始游戏
    startGameThread()
    # 线程开启
    # startGame = threading.Thread(target=startGameThread, args=())
    # startGame.start()

    # 退出脚本:在此中开启，F12退出
    endGameThread()
    # 线程开启
    # endGame = threading.Thread(target = endGameThread, args = ())
    # endGame.start()


if __name__ == '__main__':
    main()