#!/usr/bin/python
# coding=utf-8

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


def getAllScreenshot(screenshotPic):
    im = ImageGrab.grab()
    im.save(screenshotPic, 'jpeg')


def getPicRgba(pic):
    pos_rgba = {}
    img = Image.open(pic)
    for width in range(0, img.size[0]):
        for height in range(0, img.size[1]):
            rgba = img.getpixel((width, height))
            pos_rgba[(width, height)] = rgba
    print("picture gba:", pos_rgba)
    return pos_rgba


def getAreaScreenshot(screenshotPic, pos_x, pos_y, delta):
    im = ImageGrab.grab((pos_x - delta, pos_y - delta, pos_x + delta, pos_y + delta))
    im.save(screenshotPic, 'jpeg')


def getPointRgba(pic, pos_x, pos_y):
    pos_rgba = {}
    img = Image.open(pic)
    for width in range(pos_x, pos_x + 1):
        for height in range(pos_y, pos_y + 1):
            rgba = img.getpixel((width, height))
            pos_rgba[(width, height)] = rgba

    # print("point gba:", pos_rgba)


def touchScreen(pos_x, pos_y):
    m = PyMouse()
    m.click(pos_x, pos_y)
    print("click done!")

# judge whether to click
def thread_getPic(pic_name, pos_x, pos_y, delta):
    originalRGB = [(255, 239, 255), (255, 233, 255), (255, 249, 253), (171, 124, 196), (188, 136, 218), (121, 61, 121)]
    getAreaScreenshot(pic_name, pos_x, pos_y, delta)

    print("values:", getPicRgba(pic_name).values())

    if (originalRGB[0] in getPicRgba(pic_name).values() or originalRGB[1] in getPicRgba(pic_name).values() or
            originalRGB[2] in getPicRgba(pic_name).values() or originalRGB[3] in getPicRgba(pic_name).values() or
            originalRGB[4] in getPicRgba(pic_name).values() or originalRGB[5] in getPicRgba(pic_name).values()):
        print(pos_x, pos_y, touchScreen(pos_x, pos_y))



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
        thread_getPic(saved_path_1, 780, 310, 20)
        sys.exit()
        thread_getPic(saved_path_2, 880, 310, 20)
        thread_getPic(saved_path_3, 980, 310, 20)
        thread_getPic(saved_path_4, 1080, 310, 20)
        thread_getPic(saved_path_5, 1180, 310, 20)

        thread_getPic(saved_path_6, 780, 410, 20)
        thread_getPic(saved_path_7, 880, 410, 20)
        thread_getPic(saved_path_8, 980, 410, 20)
        thread_getPic(saved_path_9, 1080, 410, 20)
        thread_getPic(saved_path_10, 1180, 410, 20)

        thread_getPic(saved_path_11, 780, 510, 20)
        thread_getPic(saved_path_12, 880, 510, 20)
        thread_getPic(saved_path_13, 980, 510, 20)
        thread_getPic(saved_path_14, 1080, 510, 20)
        thread_getPic(saved_path_15, 1180, 510, 20)

        thread_getPic(saved_path_16, 780, 610, 20)
        thread_getPic(saved_path_17, 880, 610, 20)
        thread_getPic(saved_path_18, 980, 610, 20)
        thread_getPic(saved_path_19, 1080, 610, 20)
        thread_getPic(saved_path_20, 1180, 610, 20)

        thread_getPic(saved_path_21, 780, 710, 20)
        thread_getPic(saved_path_22, 880, 710, 20)
        thread_getPic(saved_path_23, 980, 710, 20)
        thread_getPic(saved_path_24, 1080, 710, 20)
        thread_getPic(saved_path_25, 1180, 710, 20)
        # 控制时间超过60秒的话直接停止退出
        stop = time.time();
        if (stop - start) > 60:
            sys.exit();

    # t1 = threading.Thread(target = thread_getPic, args = (saved_path_1, 355, 168, 20, ))
    # t1.start()
    # t2 = threading.Thread(target = thread_getPic, args = (saved_path_2, 632, 161, 20, ))
    # t2.start()
    # t3 = threading.Thread(target = thread_getPic, args = (saved_path_3, 886, 154, 20, ))
    # t3.start()
    # t4 = threading.Thread(target = thread_getPic, args = (saved_path_4, 266, 313, 20, ))
    # t4.start()
    # t5 = threading.Thread(target = thread_getPic, args = (saved_path_5, 573, 311, 20, ))
    # t5.start()
    # t6 = threading.Thread(target = thread_getPic, args = (saved_path_6, 876, 315, 20, ))
    # t6.start()
    # t7 = threading.Thread(target = thread_getPic, args = (saved_path_7, 325, 474, 20, ))
    # t7.start()
    # t8 = threading.Thread(target = thread_getPic, args = (saved_path_8, 607, 479, 20, ))
    # t8.start()
    # t9 = threading.Thread(target = thread_getPic, args = (saved_path_9, 870, 473, 20, ))
    # t9.start()

    # while 1:
    #     if not t1.is_alive():
    #         t1 = threading.Thread(target = thread_getPic, args = (saved_path_1, 355, 168, 20, ))
    #         t1.start()

    #     if not t2.is_alive():
    #         t2 = threading.Thread(target = thread_getPic, args = (saved_path_2, 632, 161, 20, ))
    #         t2.start()

    #     if not t3.is_alive():
    #         t3 = threading.Thread(target = thread_getPic, args = (saved_path_3, 886, 154, 20, ))
    #         t3.start()

    #     if not t4.is_alive():
    #         t4 = threading.Thread(target = thread_getPic, args = (saved_path_4, 266, 313, 20, ))
    #         t4.start()

    #     if not t5.is_alive():
    #         t5 = threading.Thread(target = thread_getPic, args = (saved_path_5, 573, 311, 20, ))
    #         t5.start()

    #     if not t6.is_alive():
    #         t6 = threading.Thread(target = thread_getPic, args = (saved_path_6, 876, 315, 20, ))
    #         t6.start()

    #     if not t7.is_alive():
    #         t7 = threading.Thread(target = thread_getPic, args = (saved_path_7, 325, 474, 20, ))
    #         t7.start()

    #     if not t8.is_alive():
    #         t8 = threading.Thread(target = thread_getPic, args = (saved_path_8, 607, 479, 20, ))
    #         t8.start()

    #     if not t9.is_alive():
    #         t9 = threading.Thread(target = thread_getPic, args = (saved_path_9, 870, 473, 20, ))
    #         t9.start()


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
    # 获取检测的颜色值
    check_pic1 = r'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg'
    getPointRgba(check_pic1, 30, 40)
    getPicRgba(check_pic1);
    # sys.exit();

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