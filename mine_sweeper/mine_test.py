#saolei.py
# coding: cp936
import win32gui
import win32process
import win32con
import win32api
from ctypes import *
'''
��˵��ԭ��ԭ����ʵ�ܼ򵥣��跨��á������������ݣ�Ȼ��ͨ��ģ����궯������������Ϸǵ��׵ĵĸ��ӣ��͸㶨��:)  
���Լ����ѵ�ֻ������������������ݡ��ҵ�ɨ�׳����ģ����궯���� 
��˵�򵥵ģ��ҵ�ɨ�׳���ͨ��win32gui.FindWindow("ɨ��", "ɨ��") �Ϳ����ҵ�ɨ�׳�����������ˣ�
�ܼ򵥰ɡ�FindWindow���API��������ο�MSDN. 
Ȼ����ģ���������������Ҳ�ܼ򵥣�ͨ��win32api.SendMessage�����巢�����İ���WM_LBUTTONDOWN���ɿ�WM_LBUTTONUP��Ϣ�����ˣ�
���api����Ҫ�����ǣ�������Ϣ�Ĵ�������������ɨ�׳���������壩������������ꡣ���api��ʹ�ò��ѣ�����ο�MSDN:) 
�Ƚ����Ѷȵ�����λ���������ݡ���������������Ҫ��������Ҫ�ҳ������ڳ����ڲ�����α�ʾ�ģ�������ָ��������׻������ף�
���֪���������Ӵ�С���Լ���Щ���ݱ����ڳ���ʲôλ�ã��ǹ̶�λ�û��Ǳ仯�ġ�Ū����Щ�鱨��

�ڶ�������ͼ��ˣ����ǿ���ͨ������api���������ɵؾͻ�ȡ�����Ķ�̬���ݡ� 
Ҫ��ɵ�һ�����飬������Ҫһ����ollydbg�ķ������Թ��ߡ�һЩЩ���֪ʶ�Լ��ܴ�����ģ��Ǻǣ������������Ͳ�˵�ˣ�
��Ҫ�ǲ�֪������˵������о��������һЩ��
ͨ�����ٻ����룬���ǿ��Է������׵ĸ���������0x0F�����׵���0x8F���������������Ǵ�0x1005340 ����߼���ַ��ʼ��
���������õ����ݼ�����Դ�롣 

������Щ���ݺ�����ͨ��win32process.GetWindowThreadProcessId��á�ɨ�ס��Ľ���id�� ͨ��OpenProcess �򿪸ý��̣�Ȼ��ͨ��ReadProcessMemory ��ȡ0x1005340��ʼ���������ݣ���������Щ����ͨ��SendMessage��ɨ�׳����������Ϣ���͸㶨�ˣ���֤ÿ��ɨ�׶��ǡ���ɱ��
ת��:www.hbxcyz.cn
'''
#�������������
MAX_ROWS = 24
MAX_COLUMNS = 30

#���������ڴ����ϵ���ʼ���꼰ÿ�����ӵĿ��
MINE_BEGIN_X = 0xC
MINE_BEGIN_Y = 0x37
MINE_GRID_WIDTH = 0x10
MINE_GRID_HEIGHT = 0x10

#�߿����ס����׵��ڲ���ʾ
MINE_BOARDER = 0x10
MINE_SAFE = 0x0F
MINE_DANGER = 0x8F

#���������� ɨ�׳����еĴ洢��ַ
BOARD_ADDR = 0x1005340

class SMineCtrl(Structure):
    _fields_ = [("hWnd", c_uint),
                ("board", (c_byte * (MAX_COLUMNS + 2)) * (MAX_ROWS + 2)),
                ("rows", c_byte),
                ("columns", c_byte)
                ]
    kernel32 = windll.LoadLibrary("kernel32.dll")
    ReadProcessMemory = kernel32.ReadProcessMemory
    WriteProcessMemory = kernel32.WriteProcessMemory
    OpenProcess = kernel32.OpenProcess


ctrlData = SMineCtrl()

#�ҵ�ɨ�׳��򲢴򿪶�Ӧ����
try:
    ctrlData.hWnd = win32gui.FindWindow("ɨ��", "ɨ��")
except:
    win32api.MessageBox(0, "��������ɨ�׳���", "����", win32con.MB_ICONERROR)
    exit(0)
hreadID, processID = win32process.GetWindowThreadProcessId(ctrlData.hWnd)
hProc = windll.LoadLibrary("kernel32.dll").OpenProcess (win32con.PROCESS_ALL_ACCESS, 0, processID)

#��ȡ��������
bytesRead = c_ulong(0)
windll.LoadLibrary("kernel32.dll").ReadProcessMemory(hProc, BOARD_ADDR, byref(ctrlData.board), SMineCtrl.board.size, byref(bytesRead))
if(bytesRead.value != SMineCtrl.board.size):
    str = "ReadProcessMemory error, only read ", bytesRead.value, " should read ", SMineCtrl.board.size
    win32api.MessageBox(0, str, "����", win32con.MB_ICONERROR)
    exit()

#��ȡ���γ���������ʵ�ʴ�С
ctrlData.rows = 0
ctrlData.columns = 0
for i in range(0, MAX_COLUMNS + 2):
    if MINE_BOARDER == ctrlData.board[0][i]:
        ctrlData.columns += 1
    else :
        break
ctrlData.columns -= 2

for i in range(1, MAX_ROWS + 1):
    if MINE_BOARDER != ctrlData.board[i][1]:
        ctrlData.rows += 1
    else:
        break

#ģ�����������
for i in range(0, ctrlData.rows):
    for j in range(0, ctrlData.columns):
        if MINE_SAFE == ctrlData.board[i + 1][j + 1]:
            win32api.SendMessage(ctrlData.hWnd,
                                win32con.WM_LBUTTONDOWN,
                                win32con.MK_LBUTTON,
                                win32api.MAKELONG(MINE_BEGIN_X + MINE_GRID_WIDTH * j + MINE_GRID_WIDTH / 2,
                                                  MINE_BEGIN_Y + MINE_GRID_HEIGHT * i + MINE_GRID_HEIGHT / 2))
            win32api.SendMessage(ctrlData.hWnd,
                                win32con.WM_LBUTTONUP,
                                win32con.MK_LBUTTON,
                                win32api.MAKELONG(MINE_BEGIN_X + MINE_GRID_WIDTH * j + MINE_GRID_WIDTH / 2,
                                                  MINE_BEGIN_Y + MINE_GRID_HEIGHT * i + MINE_GRID_HEIGHT / 2))

#�㶨!
win32api.MessageBox(0, "�㶨��", "��Ϣ", win32con.MB_ICONINFORMATION)
