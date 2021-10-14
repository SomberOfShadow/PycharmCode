import numpy as np

# 创建Axes3D主要有两种方式，一种是利用关键字projection='3d'l来实现，
# 另一种则是通过从mpl_toolkits.mplot3d导入对象Axes3D来实现，目的都是生成具有三维格式的对象Axes3D.
#方法一，利用关键字
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')
# ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图


# #方法二，利用三维轴方法
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# #定义图像和三维格式坐标轴
# fig=plt.figure()
# ax2 = Axes3D(fig)


z = np.linspace(0,13,1000)
x = 5*np.sin(z)
y = 5*np.cos(z)
zd = 13*np.random.random(100)
xd = 5*np.sin(zd)
yd = 5*np.cos(zd)
ax1.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图
ax1.plot3D(x,y,z,'gray')    #绘制空间曲线
plt.show()

fig = plt.figure()  #定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

#定义三维数据
xx = np.arange(-10,10,100)
yy = np.arange(-10,10,100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+np.cos(Y)


#作图
ax3.plot_surface(X,Y,Z,cmap='rainbow')
#ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
plt.show()
