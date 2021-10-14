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

    print (pos_rgba)


def touchScreen(pos_x, pos_y):
    m = PyMouse()
    m.click(pos_x, pos_y)


def thread_getPic(pic_name, pos_x, pos_y, delta):
    originalRGB = [(255, 239, 255), (255, 233, 255), (255, 249, 253), (171, 124, 196), (188, 136, 218), (121, 61, 121)]
    getAreaScreenshot(pic_name, pos_x, pos_y, delta)

    if (originalRGB[0] in getPicRgba(pic_name).values() or originalRGB[1] in getPicRgba(pic_name).values() or
            originalRGB[2] in getPicRgba(pic_name).values() or originalRGB[3] in getPicRgba(pic_name).values() or
            originalRGB[4] in getPicRgba(pic_name).values() or originalRGB[5] in getPicRgba(pic_name).values()):
        print (pos_x, pos_y, touchScreen(pos_x, pos_y ) )



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

    while 1:
        print ("start game thread......")
        thread_getPic(saved_path_1, 355, 168, 20)
        thread_getPic(saved_path_2, 632, 161, 20)
        thread_getPic(saved_path_3, 886, 154, 20)
        thread_getPic(saved_path_4, 266, 313, 20)
        thread_getPic(saved_path_5, 573, 311, 20)
        thread_getPic(saved_path_6, 876, 315, 20)
        thread_getPic(saved_path_7, 325, 474, 20)
        thread_getPic(saved_path_8, 607, 479, 20)
        thread_getPic(saved_path_9, 870, 473, 20)

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
    # return False


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
        time.sleep(1)
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