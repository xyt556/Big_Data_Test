# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 11:23
# Author : YantaoXI
# @File : correlation.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
# 读取Excel文件
df = pd.read_excel('data.xlsx', sheet_name='test',header=0)

# 选取两列
x = df['Pb']
y = df['Ni']

# 绘制散点图
plt.scatter(x, y)
plt.xlabel('Pb')
plt.ylabel('Ni')
# 计算趋势线的斜率、截距和相关系数
slope, intercept, r_value, p_value, std_err = linregress(x, y)
r_squared = r_value ** 2

# 绘制趋势线和相关系数
line_x = np.array([x.min(), x.max()])
line_y = intercept + slope * line_x
plt.plot(line_x, line_y, color='red', label=f'拟合方程：y={slope:.2f}x+{intercept:.2f}\n$R^2$={r_squared:.2f}')
plt.legend()

# 将相关系数添加到图上
cor_label = f"相关系数：{r_squared:.2f}"
plt.annotate(cor_label, xy=(0.5, 0.95), xycoords='axes fraction', fontsize=12)
# 进行相关性分析
correlation = x.corr(y)
# 在图上展示相关系数
plt.text(0.9, 0.9, f'相关系数：{correlation:.2f}', transform=plt.gca().transAxes, ha='right')
print('相关系数：', correlation)
plt.show()