# -*- codeing =utf-8 -*-
# @Time : 2023/2/20$ 10:49
# Author : YantaoXI
# @File : bst.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt



import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']     # 用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False       # 用来正常
# 读取Excel文件
df = pd.read_excel(r'D:\ww.xlsx')

# 按照类别进行分组
groups = df.groupby('科室/科室组')

# 创建波士顿矩阵图
fig, ax = plt.subplots()
for name, group in groups:
    ax.plot(group['总收入'], group['医疗服务收入'], marker='o', linestyle='', ms=12, label=name)
ax.legend( loc='upper left', title='Legend')
ax.set_xlabel('总收入')
ax.set_ylabel('医疗服务收入')
# 保存结果为600dpi的jpg文件
plt.savefig('boston_matrix.jpg', dpi=600)
plt.show()
