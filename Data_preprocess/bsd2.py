# -*- codeing =utf-8 -*-
# @Time : 2023/2/20$ 11:37
# Author : YantaoXI
# @File : bsd2.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 Excel 文件
df = pd.read_excel('ww.xlsx')

# 设置图像大小和分辨率
fig, ax = plt.subplots(figsize=(10, 8), dpi=600)

# 绘制波士顿矩阵图
scatter = ax.scatter(df.iloc[:, 1], df.iloc[:, 2], c=df.iloc[:, 0], cmap='Set1')

# 添加图例
handles, labels = scatter.legend_elements(num=10)
legend = ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5), title='Legend')

# 绘制平均值线
mean_x = np.mean(df.iloc[:, 1])
mean_y = np.mean(df.iloc[:, 2])
ax.axhline(mean_y, color='gray', linestyle='--')
ax.axvline(mean_x, color='gray', linestyle='--')

# 绘制十字线
ax.axhline(0, color='black')
ax.axvline(0, color='black')

# 设置图像标题和坐标轴标签
ax.set_title('Boston Housing Prices')
ax.set_xlabel('Per Capita Crime Rate')
ax.set_ylabel('Average Number of Rooms per Dwelling')

# 保存图像
plt.savefig('boston_housing_prices.jpg', bbox_inches='tight')
