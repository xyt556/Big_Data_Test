# 位置是由三个整型数值构成，第一个代表行数，第二个代表列数，第三个代表索引位置。
# 举个列子：plt.subplot(2, 3, 5) 和 plt.subplot(235) 是一样一样的。
# 需要注意的是所有的数字不能超过10。
# 第二个参数：projection : {None, ‘aitoff’, ‘hammer’, ‘lambert’, ‘mollweide’, ‘polar’, ‘rectilinear’, str}, optional
# The projection type of the subplot (Axes). str is the name of a costum projection, see projections. The default None results in a ‘rectilinear’ projection.
# 可选参数：可以选择子图的类型，比如选择polar，就是一个极点图。默认是none就是一个线形图。
# https://blog.csdn.net/gailj/article/details/122149994?spm=1001.2101.3001.6650.10&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-10-122149994-blog-106784489.pc_relevant_aa&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-10-122149994-blog-106784489.pc_relevant_aa&utm_relevant_index=12
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 2)
y1 = np.sin(x)

y2 = np.cos(x)

ax1 = plt.subplot(2, 2, 1, frameon = False) # 两行一列，位置是1的子图
plt.plot(x, y1, 'b--')
plt.ylabel('y1')

ax2 = plt.subplot(2, 2, 2, projection = 'polar')
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.xlabel('x')

plt.subplot(2, 2, 3, sharex = ax1, facecolor = 'b')
plt.plot(x, y2, 'r--')
plt.ylabel('y2')

plt.subplot(2, 2, 4, sharex = ax1, facecolor = 'g')
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.show()
