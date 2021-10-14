import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  #定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

#定义三维数据
z = np.linspace(0,13,1000)
x = 5*np.sin(z)
y = 5*np.cos(z)
xx = np.arange(-10,10,100)
yy = np.arange(-10,10,100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+np.cos(Y)


#作图
ax3.plot_surface(X,Y,Z,cmap='rainbow')

# 如果加入渲染时的步长，会得到更加清晰细腻的图像：其中的row和cloum_stride为横竖方向的步长
# ax3.plot_surface(X,Y,Z,rstride = 1, cstride = 1,cmap='rainbow')
#ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
plt.show()
