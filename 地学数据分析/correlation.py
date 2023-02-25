# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 11:23
# Author : YantaoXI
# @File : correlation.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
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
plt.show()

# 进行相关性分析
correlation = x.corr(y)
print('相关系数：', correlation)
