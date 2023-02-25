# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 20:24
# Author : YantaoXI
# @File : variogram.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

# 定义变差函数
def variogram(h, nugget, sill, range_val, model):
    if model == 'exponential':
        return nugget + (sill - nugget) * (1 - np.exp(-h / range_val))
    elif model == 'gaussian':
        return nugget + (sill - nugget) * (1 - np.exp(-h ** 2 / range_val ** 2))
    elif model == 'spherical':
        if h <= range_val:
            return nugget + (sill - nugget) * (1.5 * h / range_val - 0.5 * (h / range_val) ** 3)
        else:
            return nugget + (sill - nugget)

# 定义变差函数参数
nugget = 0
sill = 1
range_val = 100
model = 'exponential'

# 定义距离范围
h_min = 0
h_max = 2 * range_val
n_h = 50
h = np.linspace(h_min, h_max, n_h)

# 计算变差函数值
gamma = [variogram(h_val, nugget, sill, range_val, model) for h_val in h]

# 绘制变差函数图像
plt.plot(h, gamma, 'bo-')
plt.title('Variogram')
plt.xlabel('Distance (h)')
plt.ylabel('Gamma(h)')
plt.show()
