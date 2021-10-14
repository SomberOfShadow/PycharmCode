#!/usr/bin/python
# coding=utf-8


#使用第三方库：Pillow
import webbrowser
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
    # 第一种方法实现鼠标点击
    win32api.SetCursorPos((pos_x, pos_y))  # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)  # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)  # 鼠标左键弹起

    # 第二种方法实现鼠标点击, 这种方法存在问题
    # m = PyMouse()
    # m.move(pos_x, pos_y)
    # m.click(pos_x, pos_y)


# 判断两个图片是否相似度, 如果是相同的图片, 那么敲击对应的位置
def Rugular_Pic(pic_name1, pic_name2, pos_x, pos_y):
    image1 = Image.open(pic_name1)
    image3 = Image.open(pic_name2)

    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image3.histogram()
    # result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    if(result < 40):
        touchScreen(pos_x, pos_y);



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
        print("----start game thread----")
        # 对屏幕上特定25块区域进行截图保存
        getAreaScreenshot(saved_path_1, 800, 270, 30)
        # 奖截图和check的图片进行比较,然后根据比较的结果进行敲击
        Rugular_Pic(saved_path_1, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 800, 270);
        getAreaScreenshot(saved_path_2, 880, 270, 30)
        Rugular_Pic(saved_path_2, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 270);
        getAreaScreenshot(saved_path_3, 960, 270, 30)
        Rugular_Pic(saved_path_3, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 960, 270);
        getAreaScreenshot(saved_path_4, 1040, 270, 30)
        Rugular_Pic(saved_path_4, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1040, 270);
        getAreaScreenshot(saved_path_5, 1120, 270, 30)
        Rugular_Pic(saved_path_5, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1120, 270);

        getAreaScreenshot(saved_path_6, 800, 355, 30)
        Rugular_Pic(saved_path_6, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 800, 355);
        getAreaScreenshot(saved_path_7, 880, 355, 30)
        Rugular_Pic(saved_path_7, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 355);
        getAreaScreenshot(saved_path_8, 960, 355, 30)
        Rugular_Pic(saved_path_8, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 960, 355);
        getAreaScreenshot(saved_path_9, 1040, 355, 30)
        Rugular_Pic(saved_path_9, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1040, 355);
        getAreaScreenshot(saved_path_10, 1120, 355, 30)
        Rugular_Pic(saved_path_10, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1120, 355);

        getAreaScreenshot(saved_path_11, 800, 440, 30)
        Rugular_Pic(saved_path_11, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 800, 440);
        getAreaScreenshot(saved_path_12, 880, 440, 30)
        Rugular_Pic(saved_path_12, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 440);
        getAreaScreenshot(saved_path_13, 960, 440, 30)
        Rugular_Pic(saved_path_13, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 960, 440);
        getAreaScreenshot(saved_path_14, 1040, 440, 30)
        Rugular_Pic(saved_path_14, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1040, 440);
        getAreaScreenshot(saved_path_15, 1120, 440, 30)
        Rugular_Pic(saved_path_15, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1120, 440);

        getAreaScreenshot(saved_path_16, 800, 525, 30)
        Rugular_Pic(saved_path_16, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 800, 525);
        getAreaScreenshot(saved_path_17, 880, 525, 30)
        Rugular_Pic(saved_path_17, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 525);
        getAreaScreenshot(saved_path_18, 960, 525, 30)
        Rugular_Pic(saved_path_18, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 960, 525);
        getAreaScreenshot(saved_path_19, 1040, 525, 30)
        Rugular_Pic(saved_path_19, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1040, 525);
        getAreaScreenshot(saved_path_20, 1120, 525, 30)
        Rugular_Pic(saved_path_20, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1120, 525);

        getAreaScreenshot(saved_path_21, 800, 610, 30)
        Rugular_Pic(saved_path_21, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 800, 610);
        getAreaScreenshot(saved_path_22, 880, 610, 30)
        Rugular_Pic(saved_path_22, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 880, 610);
        getAreaScreenshot(saved_path_23, 960, 610, 30)
        Rugular_Pic(saved_path_23, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 960, 610);
        getAreaScreenshot(saved_path_24, 1040, 610, 30)
        Rugular_Pic(saved_path_24, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1040, 610);
        getAreaScreenshot(saved_path_25, 1120, 610, 30)
        Rugular_Pic(saved_path_25, 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg', 1120, 610);


        # 控制时间超过60秒的话直接停止退出
        stop = time.time();
        if (stop - start) > 60:
            sys.exit();


# 点击键盘F12退出
def endGameThread():
    # 直接退出
    sys.exit();

    # hm = pyHook.HookManager()
    # # 监听所有键盘事件
    # hm.KeyDown = onKeyboardEvent
    # # 设置键盘“钩子”
    # hm.HookKeyboard()
    # # 监听所有鼠标事件
    # # hm.MouseAll = onMouseEvent
    # # # 设置鼠标“钩子”
    # # hm.HookMouse()
    # # 进入循环，如不手动关闭，程序将一直处于监听状态
    # pythoncom.PumpMessages()


def main():
    # 注册使用ie浏览器打开游戏网页
    ie_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
    webbrowser.register('IE', None, webbrowser.BackgroundBrowser(ie_path))
    webbrowser.get('IE').open('http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html', new=1, autoraise=True)

    # 打开网页之后等5秒,防止页面的延迟
    time.sleep(3)

    # 自动点击开始
    touchScreen(950, 900);

    # 开始游戏
    startGameThread()
    # 退出脚本:在此中开启，F12退出
    endGameThread()


if __name__ == '__main__':
    main()