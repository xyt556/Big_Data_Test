# -*- codeing =utf-8 -*-
# @Time : 2023/2/26$ 15:23
# Author : YantaoXI
# @File : 系统抽样.py
# @Software: PyCharm
# 读取Excel数据，进行系统取样可以通过以下步骤实现：
#
# 导入需要的库，如pandas、numpy等；
# 读取Excel数据，将数据存储为DataFrame类型的变量；
# 确定总体大小和样本大小，计算每个样本的间隔；
# 使用pandas的iloc函数进行抽样，选取第一个样本，以及每隔固定间隔的样本。
# 以下是一个Python代码示例：

import pandas as pd
import numpy as np

# 读取Excel数据
df = pd.read_excel('实习一.xlsx', sheet_name='原始数据')


# 确定系统取样的间隔
interval = 3

# 计算样本个数
n = len(df)

# 计算样本序号
sample_indices = range(0, n, interval)

# 选择样本数据
sample = df.iloc[sample_indices]

# 将样本数据保存为Excel文件
sample.to_excel('系统抽样.xlsx', index=False)
