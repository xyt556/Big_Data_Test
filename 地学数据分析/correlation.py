# -*- codeing =utf-8 -*-
# @Time : 2023/2/25$ 11:23
# Author : YantaoXI
# @File : correlation.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
# 读取Excel文件
df = pd.read_excel('data.xlsx', sheet_name='test',header=0)
x_val='Co'
y_val='Zn'
# 选取两列
x = df[x_val]
y = df[y_val]

# 绘制散点图
plt.scatter(x, y)
plt.xlabel(x_val)
plt.ylabel(y_val)
# 计算趋势线的斜率、截距和相关系数
slope, intercept, r_value, p_value, std_err = linregress(x, y)
r_squared = r_value ** 2

# 绘制趋势线和相关系数
line_x = np.array([x.min(), x.max()])
line_y = intercept + slope * line_x
plt.plot(line_x, line_y, color='red', label=f'拟合方程：y={slope:.2f}x+{intercept:.2f}\n$R^2$={r_squared:.2f}')
plt.legend()

# 将相关系数添加到图上
# cor_label = f"相关系数：{r_squared:.2f}"
# plt.annotate(cor_label, xy=(0.5, 0.95), xycoords='axes fraction', fontsize=12)
# 进行相关性分析
correlation = x.corr(y)
cov=np.cov(x,y)
# 在图上展示相关系数
plt.text(0.9, 0.1, f'皮尔逊相关系数：{correlation:.2f}', transform=plt.gca().transAxes, ha='right')
# plt.text(0.9, 0.2, f'协方差：{cov:.2f}', transform=plt.gca().transAxes, ha='right')
print('皮尔逊相关系数：', correlation)
print('协方差：', cov)
plt.savefig('correlation.jpg',dpi=600)
plt.show()

# corr函数和linregress函数计算的相关系数并不完全相同，因为它们使用的方法和定义不同。
#
# corr函数计算的是两个变量之间的皮尔逊相关系数，它的定义是两个变量之间的协方差除以它们各自标准差的乘积。皮尔逊相关系数衡量的是两个变量之间的线性关系程度，它的取值范围在-1到1之间，其中1表示完全正相关，-1表示完全负相关，0表示没有线性相关性。
#
# 而linregress函数计算的是两个变量之间的线性回归方程，它的输出结果包括斜率、截距、相关系数、标准误差和t值等统计量。其中，相关系数表示的是两个变量之间的线性相关程度，与皮尔逊相关系数类似，取值范围也在-1到1之间。
#
# 但是，这两个函数计算相关系数的方式是不同的，linregress函数计算的是简单线性回归模型的相关系数，而corr函数可以计算任意两个变量之间的相关系数，包括非线性关系。因此，两个函数计算的相关系数可能不完全相同，具体取决于变量之间的关系形式。