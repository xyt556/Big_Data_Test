# -*- codeing =utf-8 -*-
# @Time : 2023/2/20$ 11:45
# Author : YantaoXI
# @File : bsd3.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']     # 用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False       # 用来正常
# 读取 Excel 数据

df = pd.read_excel('ww.xlsx',sheet_name='住院收入排名')

# 获取类别、数据和列名
categories = df.iloc[:, 0]
x = df.iloc[:, 1]#总收入x
y = df.iloc[:, 2]#//服务收入y
columns = df.columns
colors = np.random.rand(columns.size)
# 计算数据的平均值
meanx = np.mean(x)
meany = np.mean(y)

# 绘制波士顿矩阵图
fig, ax = plt.subplots()
ax.scatter(x, y,s=2,c=colors)

# 绘制平均值线
ax.axhline(meany, color='r', linestyle='--')
ax.axvline(meanx, color='r', linestyle='--')

# 添加十字线
# ax.axhline(0, color='k')
# ax.axvline(0, color='k')

# 添加类别的图例
for i, category in enumerate(categories):
    ax.text(x[i], y[i], category, fontsize=5)

# 设置图形标题和轴标签
ax.set_title('2022年各科室住院收入波士顿矩阵图')
ax.set_xlabel(columns[1])
ax.set_ylabel(columns[2])

# 将图例放在图之外
# ax.legend(labels=['Category'], loc='center left', bbox_to_anchor=(1, 0.5))

# 保存图像
plt.savefig('住院收入.jpg', dpi=1200, bbox_inches='tight')

# 显示图像
plt.show()
