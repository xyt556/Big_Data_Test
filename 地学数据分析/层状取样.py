# -*- codeing =utf-8 -*-
# @Time : 2023/2/26$ 15:16
# Author : YantaoXI
# @File : 层状取样.py
# @Software: PyCharm
# 层状取样是一种常用的采样方法，可以对样本进行有序的分层抽样，以保证样本的代表性和可靠性。
# 下面是一个基于Python的读取Excel并进行层状取样的示例程序：
import pandas as pd

# 读取Excel文件
df = pd.read_excel('实习一.xlsx', sheet_name='原始数据', header=0)

# 设定抽样层数和每层样本数
n_layers = 5
n_samples_per_layer = 2

# 获取变量列名
var_name = df.columns[1]
print(var_name)
# 计算每层的取样间隔
n_total_samples = len(df)
interval = int(n_total_samples / n_layers)

# 对每层进行取样
sampled_rows = []
for i in range(n_layers):
    start = i * interval
    end = start + n_samples_per_layer
    sampled_rows += list(range(start, end))

# 从数据框中提取样本
sampled_df = df.iloc[sampled_rows, :]

# 保存样本到Excel文件
sampled_df.to_excel('层状抽样.xlsx', index=False)
