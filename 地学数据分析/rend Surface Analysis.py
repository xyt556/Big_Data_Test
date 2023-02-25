# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 15:43
# Author : YantaoXI
# @File : rend Surface Analysis.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# 定义自变量
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

# 定义因变量
z = np.array([0.5, 1.2, 2.1, 3.0, 4.2])

# 定义多项式函数
def poly_func(xy, a, b, c):
    x, y = xy
    return a + b*x + c*y

# 使用curve_fit拟合多项式函数
popt, pcov = optimize.curve_fit(poly_func, (x, y), z)

# 打印拟合结果
print(f"拟合结果：{popt}")

# 绘制趋势面
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义趋势面的网格
xx, yy = np.meshgrid(x, y)
zz = poly_func((xx,yy), *popt)

# 绘制趋势面
ax.plot_surface(xx, yy, zz, alpha=0.5)

# 绘制散点图
ax.scatter(x, y, z, color='r')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
