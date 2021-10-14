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

# 原始地鼠图片的位置
checkDir = 'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg'
delta = 40

# 敲击特定位置
def touchScreen(pos_x, pos_y):
    # 第一种方法实现鼠标点击
    win32api.SetCursorPos((pos_x, pos_y))  # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)  # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)  # 鼠标左键弹起


# 判断两个图片是否相似度, 如果是相同的图片, 那么敲击对应的位置
def Rugular_Pic(pic_name1, pic_name2, pos_x, pos_y):
    image1 = Image.open(pic_name1)
    image3 = Image.open(pic_name2)

    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image3.histogram()
    # result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    if(result <= 39):
        touchScreen(pos_x, pos_y);

# 每个地洞区域的屏幕截图并保存,然后判断图片相似度, 如果是地鼠则进行敲击
def get_shot_and_compare(screenshotPic, checkDir, pos_x, pos_y, delta):
    im = ImageGrab.grab((pos_x - delta, pos_y - delta, pos_x + delta, pos_y + delta))
    im.save(screenshotPic, 'jpeg');

    Rugular_Pic(screenshotPic, checkDir, pos_x, pos_y);


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
    count = 10000;
    while count > 0:
        # print("----start game thread----")
        # 单线程控制
        # get_shot_and_compare(saved_path_1, checkDir, 780, 300, delta)
        # get_shot_and_compare(saved_path_2, checkDir, 870, 300, delta)
        # get_shot_and_compare(saved_path_3, checkDir, 960, 300, delta)
        # get_shot_and_compare(saved_path_4, checkDir, 1050, 300, delta)
        # get_shot_and_compare(saved_path_5, checkDir, 1140, 300, delta)
        #
        # get_shot_and_compare(saved_path_6, checkDir, 780, 390, delta)
        # get_shot_and_compare(saved_path_7, checkDir, 870, 390, delta)
        # get_shot_and_compare(saved_path_8, checkDir, 960, 390, delta)
        # get_shot_and_compare(saved_path_9, checkDir, 1050, 390, delta)
        # get_shot_and_compare(saved_path_10, checkDir, 1140, 390, delta)
        #
        # get_shot_and_compare(saved_path_11, checkDir, 780, 490, delta)
        # get_shot_and_compare(saved_path_12, checkDir, 870, 490, delta)
        # get_shot_and_compare(saved_path_13, checkDir, 960, 490, delta)
        # get_shot_and_compare(saved_path_14, checkDir, 1050, 490, delta)
        # get_shot_and_compare(saved_path_15, checkDir, 1140, 490, delta)
        #
        # get_shot_and_compare(saved_path_16, checkDir, 780, 580, delta)
        # get_shot_and_compare(saved_path_17, checkDir, 870, 580, delta)
        # get_shot_and_compare(saved_path_18, checkDir, 960, 580, delta)
        # get_shot_and_compare(saved_path_19, checkDir, 1050, 580, delta)
        # get_shot_and_compare(saved_path_20, checkDir, 1140, 580, delta)
        #
        # get_shot_and_compare(saved_path_21, checkDir, 780, 670, delta)
        # get_shot_and_compare(saved_path_22, checkDir, 870, 670, delta)
        # get_shot_and_compare(saved_path_23, checkDir, 960, 670, delta)
        # get_shot_and_compare(saved_path_24, checkDir, 1050, 670, delta)
        # get_shot_and_compare(saved_path_25, checkDir, 1140, 670, delta)

        # 25个地洞, 每个地洞由一个线程负责, 采用多线程监控
        t1 = threading.Thread(target=get_shot_and_compare, args=(saved_path_1, checkDir, 780, 300, delta))
        t1.start();
        t2 = threading.Thread(target=get_shot_and_compare, args=(saved_path_2, checkDir, 870, 300, delta))
        t2.start();
        t3 = threading.Thread(target=get_shot_and_compare, args=(saved_path_3, checkDir, 960, 300, delta))
        t3.start()
        t4 = threading.Thread(target=get_shot_and_compare, args=(saved_path_4, checkDir, 1050, 300, delta))
        t4.start()
        t5 = threading.Thread(target=get_shot_and_compare, args=(saved_path_5, checkDir, 1140, 300, delta))
        t5.start()

        t6 = threading.Thread(target=get_shot_and_compare, args=(saved_path_6, checkDir, 780, 390, delta))
        t6.start()
        t7 = threading.Thread(target=get_shot_and_compare, args=(saved_path_7, checkDir, 870, 390, delta))
        t7.start()
        t8 = threading.Thread(target=get_shot_and_compare, args=(saved_path_8, checkDir, 960, 390, delta))
        t8.start()
        t9 = threading.Thread(target=get_shot_and_compare, args=(saved_path_9, checkDir, 1050, 390, delta))
        t9.start()
        t10 = threading.Thread(target=get_shot_and_compare, args=(saved_path_10, checkDir, 1140, 390, delta))
        t10.start()

        t11 = threading.Thread(target=get_shot_and_compare, args=(saved_path_11, checkDir, 780, 490, delta))
        t11.start()
        t12 = threading.Thread(target=get_shot_and_compare, args=(saved_path_12, checkDir, 870, 490, delta))
        t12.start()
        t13 = threading.Thread(target=get_shot_and_compare, args=(saved_path_13, checkDir, 960, 490, delta))
        t13.start()
        t14 = threading.Thread(target=get_shot_and_compare, args=(saved_path_14, checkDir, 1050, 490, delta))
        t14.start()
        t15 = threading.Thread(target=get_shot_and_compare, args=(saved_path_15, checkDir, 1140, 490, delta))
        t15.start()

        t16 = threading.Thread(target=get_shot_and_compare, args=(saved_path_16, checkDir, 780, 580, delta))
        t16.start()
        t17 = threading.Thread(target=get_shot_and_compare, args=(saved_path_17, checkDir, 870, 580, delta))
        t17.start()
        t18 = threading.Thread(target=get_shot_and_compare, args=(saved_path_18, checkDir, 960, 580, delta))
        t18.start()
        t19 = threading.Thread(target=get_shot_and_compare, args=(saved_path_19, checkDir, 1050, 580, delta))
        t19.start()
        t20 = threading.Thread(target=get_shot_and_compare, args=(saved_path_20, checkDir, 1140, 580, delta))
        t20.start()

        t21 = threading.Thread(target=get_shot_and_compare, args=(saved_path_21, checkDir, 780, 670, delta))
        t21.start()
        t22 = threading.Thread(target=get_shot_and_compare, args=(saved_path_22, checkDir, 870, 670, delta))
        t22.start()
        t23 = threading.Thread(target=get_shot_and_compare, args=(saved_path_23, checkDir, 960, 670, delta))
        t23.start()
        t24 = threading.Thread(target=get_shot_and_compare, args=(saved_path_24, checkDir, 1050, 670, delta))
        t24.start()
        t25 = threading.Thread(target=get_shot_and_compare, args=(saved_path_25, checkDir, 1140, 670, delta))
        t25.start()

        count -= 1;
        # 控制时间超过60秒的话直接停止退出
        # stop = time.time();
        # if (stop - start) > 60:
        #     endGameThread();


# 点击键盘F12退出
def endGameThread():
    # 直接退出
    sys.exit();

def main():
    # 打开游戏的界面
    # 在调用其他的浏览器的时候需要提前注册， 否则打开页面的是默认浏览器
    chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open('http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html', new=1, autoraise=True)

    # 打开页面会有延迟, 所以打开的操作执行后需要sleep一点时间
    time.sleep(3)

    # 点击开始按钮
    touchScreen(950, 890);
    # 开始游戏
    startGameThread()

if __name__ == '__main__':
    main()