# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 21:11
# Author : YantaoXI
# @File : hierarchy.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
# 读取Excel文件
df = pd.read_excel('data.xlsx', sheet_name='聚类分析3',header=0, index_col=0)

# 对变量进行层次聚类
Z = linkage(df.T, 'ward')

# 绘制树状图
fig = plt.figure(figsize=(12, 8))
dn = dendrogram(Z, labels=df.columns)
plt.title('聚类树状图')
plt.xlabel('变量')
plt.ylabel('距离')
plt.show()