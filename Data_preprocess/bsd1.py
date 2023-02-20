# -*- codeing =utf-8 -*-
# @Time : 2023/2/20$ 11:13
# Author : YantaoXI
# @File : bsd1.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']     # 用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False       # 用来正常
# 读取 Excel 数据
df = pd.read_excel('ww.xlsx',header=0)
# 获取类别、数据列的列名
category_col = df.columns[0]
data_col1 = df.columns[1]
data_col2 = df.columns[2]

# 绘制波士顿矩阵图
fig, ax = plt.subplots()
ax.scatter(df[data_col1], df[data_col2], c='b', alpha=0.5)
ax.axhline(y=df[data_col2].mean(), color='r')
ax.axvline(x=df[data_col1].mean(), color='r')
ax.set_xlabel(data_col1)
ax.set_ylabel(data_col2)
ax.set_title('2022年各科室住院收入明细表')
ax.legend()
# ax.grid(True)

# 将图例放在图之外
# fig.subplots_adjust(right=0.7)
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

# 保存为 jpg 文件
fig.savefig('boston_housing.jpg', dpi=600)

# 显示图形
plt.show()