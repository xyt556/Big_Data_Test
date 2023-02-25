# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 15:43
# Author : YantaoXI
# @File : rend Surface Analysis.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取Excel文件
data = pd.read_excel("data.xlsx", sheet_name='test',header=0)

# 获取X、Y、Z三列数据
x = data.iloc[:, 1]
y = data.iloc[:, 2]
z = data.iloc[:, 3]

# 进行多项式拟合
degree = 2  # 多项式次数
coeffs = np.polyfit(x, y, degree)  # 拟合系数

# 生成网格数据
X, Y = np.meshgrid(x, y)
Z = np.zeros((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        Z[i, j] = coeffs[0] * X[i, j] ** 2 + coeffs[1] * X[i, j] + coeffs[2] * Y[i, j]

# 绘制三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 展示图形
plt.show()