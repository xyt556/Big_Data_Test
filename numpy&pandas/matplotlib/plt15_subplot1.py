# 位置是由三个整型数值构成，第一个代表行数，第二个代表列数，第三个代表索引位置。
# 举个列子：plt.subplot(2, 3, 5) 和 plt.subplot(235) 是一样一样的。
# 需要注意的是所有的数字不能超过10。

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
