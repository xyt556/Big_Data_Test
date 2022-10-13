# -*- codeing =utf-8 -*-
# @Time : 2022/7/12$ 14:37
# Author : YantaoXI
# @File : Sankey_test.py
# @Software: PyCharm
from pysankey2 import Sankey
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('sample_all_1.xlsx',sheet_name='sample',header=0)
print(df)
sky_auto_global_colors = Sankey(df,colorMode="global")

fig,ax = sky_auto_global_colors.plot()
plt.show()