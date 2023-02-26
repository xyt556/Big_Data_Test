# -*- codeing =utf-8 -*-
# @Time : 2023/2/26$ 15:09
# Author : YantaoXI
# @File : 随机取样.py
# @Software: PyCharm
import pandas as pd

# 读取Excel文件
df = pd.read_excel('实习一.xlsx', sheet_name='原始数据')

# 随机取样
sample_size = 20  # 样本大小
sample = df.sample(n=sample_size, random_state=1)  # n表示样本大小，random_state为随机种子，保证每次运行结果相同

# 将样本保存为Excel文件
sample.to_excel('随机抽样.xlsx', index=False)

# 在示例代码中，使用pd.read_excel()函数读取名为"data.xlsx"的Excel文件，
# 其中sheet_name参数指定需要读取的Sheet页的名称，若Excel中只有一个Sheet页，则可以省略该参数。
# 然后，使用df.sample()函数进行随机取样，其中n参数表示样本大小，
# random_state参数为随机种子，用于保证每次随机取样的结果相同。
# 最后，使用sample.to_excel()函数将样本保存为Excel文件，其中index=False表示不保存行索引。
#
# 需要注意的是，在进行随机取样前，需要根据具体研究问题和数据特征确定样本大小，
# 并对总体数据进行必要的筛选和清洗，以保证样本具有代表性和可靠性。