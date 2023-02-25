# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 15:47
# Author : YantaoXI
# @File : rend Surface Analysis1.py
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

# 计算X、Y、Z的平均值
x_mean = np.mean(x)
y_mean = np.mean(y)
z_mean = np.mean(z)

# 计算X、Y、Z的标准差
x_std = np.std(x)
y_std = np.std(y)
z_std = np.std(z)

# 计算协方差矩阵
cov_mat = np.cov([x, y, z])

# 计算特征值和特征向量
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# 找到最大特征值对应的特征向量
max_eig_val_idx = np.argmax(eig_vals)
max_eig_vec = eig_vecs[:, max_eig_val_idx]

# 计算斜率
slope = max_eig_vec[1] / max_eig_vec[0]

# 计算截距
intercept = y_mean - slope * x_mean

# 输出拟合方程
print(f"趋势面方程为：z = {slope:.2f}x + {intercept:.2f}")

# 绘制散点图和趋势面
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
xx, yy = np.meshgrid(range(int(min(x)), int(max(x))), range(int(min(y)), int(max(y))))
zz = slope * xx + intercept
ax.plot_surface(xx, yy, zz, alpha=0.2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# 展示图形
plt.show()
