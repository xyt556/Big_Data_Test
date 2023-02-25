# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 11:01
# Author : YantaoXI
# @File : hist.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data.xlsx',sheet_name='test',header=0)


# 选择需要绘制直方图的变量列
variable = 'U'

# 统计变量的频率分布
bins = 10 # 设定直方图的区间数
freq, edges = pd.cut(df[variable], bins=bins, retbins=True, include_lowest=True)
freq_table = pd.DataFrame({'频率': freq.value_counts(), '区间': pd.cut(edges, bins=bins, include_lowest=True)})

# 将频率分布保存为csv文件
freq_table.to_csv('freq_table.csv', index=False)

# 绘制直方图
plt.hist(df[variable], bins=edges, edgecolor='black')
plt.xlabel(variable)
plt.ylabel('频数')
plt.show()
