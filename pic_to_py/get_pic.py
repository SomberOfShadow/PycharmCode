import base64
import os
# from rose_jpg import *		# 无需像原博客那样一个个导入
from rose_jpg import img as rose

tmp = open('rose.jpg', 'wb')
tmp.write(base64.b64decode(rose))
tmp.close()
#现在就能用了，用完（加载到程序里之后）删了就好
# os.remove('rose.jpg')