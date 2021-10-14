#!/usr/bin/python
# -*- coding:UTF=8 -*-

import webbrowser
import win32gui
import win32con

# url = 'http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html';
# webbrowser.open(url, 0, True);

# 注册使用ie浏览器打开网页


# ie_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
# webbrowser.register('IE', None, webbrowser.BackgroundBrowser(ie_path))
# webbrowser.get('IE').open('http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html', new=1, autoraise=True)
#
#


# # 在调用其他的浏览器的时候需要提前注册， 否则打开页面的是默认浏览器
chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'            # 例如我的：D:\Google\Chrome\Application\chrome.exe
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  #这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
webbrowser.get('chrome').open('http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html', new=1, autoraise=True)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)