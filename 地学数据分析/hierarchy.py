# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 21:11
# Author : YantaoXI
# @File : hierarchy.py
# @Software: PyCharm
import pandas as pd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data.xlsx', sheet_name='聚类分析2',header=0)

# 选择需要进行聚类的变量
vars_to_cluster = ['Ni', 'Co', 'Cu','Cr','S','As']

# 计算变量间的距离矩阵
dist = hierarchy.distance.pdist(df[vars_to_cluster].values)

# 对距离矩阵进行层次聚类
linkage = hierarchy.linkage(dist, method='average')

# 绘制树状图
fig, ax = plt.subplots(figsize=(10, 10))
hierarchy.dendrogram(linkage, labels=df.index, ax=ax)
plt.show()
