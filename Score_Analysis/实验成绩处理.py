# -*- codeing =utf-8 -*-
# @Time : 2021/7/15$ 10:36
# Author : YantaoXI
# @File : 合并表格.py
# @Software: PyCharm
import pandas as pd


# data_K = pd.read_excel(r'合并考试成绩.xlsx')
#
# data_P = pd.read_excel(r'地理信息系统实验学生成绩录入模板(奚砚涛).xlsx')
#
# data_H = pd.merge(data_P, data_K, on="学号", how="outer")
#
# # data_H['平时(必填)'] = round(data_H['平时成绩'],0)
#
# # data_H.rename(columns={'姓名_x': '姓名', '学号_x': '学号'}, inplace=True) # 修改列名
#
# data_H.to_excel('最终.xlsx',index=False)

data_H = pd.read_excel(r'实验成绩.xlsx',header= 0)
# print(data_H)
print(len(data_H))
for i in range(0,len(data_H)):
    if data_H['总评'][i] > 88:
        # data_H['期末(必填)_x'][i] = '优秀'
        data_H['实验1'][i] = '优秀'
        data_H['实验2'][i] = '优秀'
        data_H['实验3'][i] = '优秀'
        # data_H['实验4'][i] = '优秀'
        # data_H['实验5'][i] = '优秀'
        # data_H['实验6'][i] = '优秀'
        # data_H['实验7'][i] = '优秀'
        # data_H['实验8'][i] = '优秀'
    else:
        # data_H['期末(必填)_x'][i] = '良好'
        data_H['实验1'][i] = '良好'
        data_H['实验2'][i] = '良好'
        data_H['实验3'][i] = '良好'
        # data_H['实验4'][i] = '良好'
        # data_H['实验5'][i] = '良好'
        # data_H['实验6'][i] = '良好'
        # data_H['实验7'][i] = '良好'
        # data_H['实验8'][i] = '良好'
# data_H['期末(必填)_x'] = data_H['期末(必填)_y']
data_H.to_excel('最终实验成绩.xlsx',index=False)
