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


# ???????????????
def onKeyboardEvent(event):
    if 'F12' == event.Key:
        sys.exit()
    # return False??????????????????????????????
    # return False


def onMouseEvent(event):
    # ??????????????????
    if 'mouserightdown' == event.MessageName.replace("\r\n", "").replace(" ", ""):
        sys.exit()
    # ?????? True ???????????????????????????????????????
    # ??????????????????????????? False ????????????????????????????????????
    # ????????????????????????????????????????????????????????????????????????
    return False


# ????????????F12??????
def endGameThread():
    hm = pyHook.HookManager()
    # ????????????????????????
    hm.KeyDown = onKeyboardEvent
    # ????????????????????????
    hm.HookKeyboard()
    # ????????????????????????
    # hm.MouseAll = onMouseEvent
    # # ????????????????????????
    # hm.HookMouse()
    # ?????????????????????????????????????????????????????????????????????
    pythoncom.PumpMessages()


def resetGameWindowPos():
    # ??????????????????????????????????????????
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_int),
                    ('top', ctypes.c_int),
                    ('right', ctypes.c_int),
                    ('bottom', ctypes.c_int)]

    rect = RECT()
    # ????????????????????????
    while 1:
        HWND = win32gui.GetForegroundWindow()
        print (u"?????????????????????.....")
        HWND_Name = win32gui.GetWindowText(HWND)
        # print chardet.detect(HWND_Name)
        time.sleep(1)
        if '???????????????' in HWND_Name.decode('GB2312').encode('utf-8'):
            print (u"?????????????????????????????????.....")
            break
    # ????????????????????????
    ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))
    print ("?????????????????????:", ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect)))
    # ??????????????????(0, 0)
    win32gui.SetWindowPos(HWND, None, 0, 0, rect.right - rect.left, rect.bottom - rect.top,
                          win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)


def main():
    # ????????????????????????
    check_pic1 = r'C:\MySoftWare\Pycharm\PycharmTest\Whac-A-Mole-Game\check\check.jpg'
    getPointRgba(check_pic1, 30, 40)

    # ??????????????????
    # resetGamePos()

    # ????????????
    startGameThread()
    # ????????????
    # startGame = threading.Thread(target=startGameThread, args=())
    # startGame.start()

    # ????????????:??????????????????F12??????
    endGameThread()
    # ????????????
    # endGame = threading.Thread(target = endGameThread, args = ())
    # endGame.start()


if __name__ == '__main__':
    main()