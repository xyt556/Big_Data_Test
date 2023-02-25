# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 11:23
# Author : YantaoXI
# @File : correlation.py
# @Software: PyCharm
import pandas as pd
from scipy import stats
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
# 添加趋势线
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.plot(x, slope*x+intercept, color='red')
# 进行相关性分析
correlation = x.corr(y)
# 在图上展示相关系数
plt.text(0.9, 0.9, f'相关系数：{correlation:.2f}', transform=plt.gca().transAxes, ha='right')
print('相关系数：', correlation)
plt.show()