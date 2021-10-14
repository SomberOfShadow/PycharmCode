import win32gui, win32api, win32con
# 获取鼠标当前位置的坐标

# win32api.SetCursorPos((100, 100))

position = win32api.GetCursorPos()

print(position)
