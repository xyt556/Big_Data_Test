# -*- codeing =utf-8 -*-
# @Time : 2023/2/20$ 10:08
# Author : YantaoXI
# @File : Boston matrix.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

# 定义数据
data = np.array([
    [1, 3, 2, 5, 4],
    [2, 4, 1, 3, 5],
    [3, 1, 5, 2, 4],
    [5, 2, 4, 1, 3],
    [4, 5, 3, 2, 1]
])

# 绘制矩阵图
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='YlGn')

# 添加刻度尺
ax.set_xticks(np.arange(len(data)))
ax.set_yticks(np.arange(len(data)))
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
ax.set_yticklabels(['1', '2', '3', '4', '5'])

# 在每个矩阵格上添加数值
for i in range(len(data)):
    for j in range(len(data)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

# 添加图例
cbar = ax.figure.colorbar(im, ax=ax)

# 设置图例标签
cbar.ax.set_ylabel("Value", rotation=-90, va="bottom")

# 添加标题
ax.set_title("Boston Matrix")

# 显示图像
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# 生成一个随机的波士顿房价数据矩阵
data = np.random.rand(13, 13)

# 绘制矩阵图
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='hot')

# 添加颜色条
cbar = ax.figure.colorbar(im, ax=ax)

# 设置图形标题和坐标轴标签
ax.set_title("Boston House Price Data Matrix")
ax.set_xticks(np.arange(13))
ax.set_yticks(np.arange(13))
ax.set_xticklabels(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])
ax.set_yticklabels(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# 在每个单元格中添加数值标签
for i in range(13):
    for j in range(13):
        text = ax.text(j, i, round(data[i, j], 2), ha="center", va="center", color="w")

plt.show()
