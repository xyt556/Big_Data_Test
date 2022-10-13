# -*- codeing =utf-8 -*-
# @Time : 2022/6/14$ 13:37
# Author : YantaoXI
# @File : test.py
# @Software: PyCharm
from scipy.spatial.distance import pdist
import numpy as np
import pandas as pd

df = pd.read_excel(r'.\data.xlsx',sheet_name= 'Sheet2', header= 0)
fields = df.columns.values
data = np.array(df.values)[:,2:]
# print(data)
a = np.array(data[0:1,:]).flatten()
b = np.array(data[1:2,:]).flatten()
s=np.array([0.27 for i in range(len(a))])
# a=np.array([1.5 for i in range(128)])
# b=np.array([2 for i in range(128)])
# s=np.array([0.27 for i in range(128)])
# print(type(a))
print(a)
print(b)

# print(s)
print("使用python标准库的计算结果: ")
print("欧氏距离 = ", pdist(np.vstack([a,b]),'euclidean'))           #欧氏距离
print("曼哈顿距离 = ", pdist(np.vstack([a,b]),'cityblock'))         #曼哈顿距离
print("闵科夫斯基距离 = ", pdist(np.vstack([a,b]),'minkowski', p=3))#闵可夫斯基距离 (p=2时相当于欧氏距离)
print("标准欧氏距离 = ", pdist(np.vstack([a,b]),'seuclidean', V=s)) #标准欧氏距离
print("余弦距离 = ", 1-pdist(np.vstack([a,b]),'cosine'))            #余弦距离(pdist中求得的是1-余弦距离)