# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 20:24
# Author : YantaoXI
# @File : variogram.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data.xlsx',sheet_name='test',header=0)

# 取出需要计算变差函数的列
variable = 'Mn'

# 计算变差函数
max_dist = 100  # 最大距离
lag_dist = 10  # 拉格距离
lags = np.arange(lag_dist, max_dist, lag_dist)  # 拉格朗日距离序列
vario = [0]*len(lags)  # 变差函数序列

for i, lag in enumerate(lags):
    diff = []
    for j in range(len(df)-lag):
        d = df.iloc[j+lag][variable] - df.iloc[j][variable]
        diff.append(d*d)
    if len(diff)>0:
        vario[i] = np.mean(diff)/2
        print('Lag %d: %f'%(lag, vario[i]))

# 绘制变差函数图像
plt.plot(lags, vario, 'bo-', label='Variogram')
plt.xlabel('Lag Distance')
plt.ylabel('Semivariance')
plt.title('Variogram of %s'%variable)
plt.legend()
plt.show()

