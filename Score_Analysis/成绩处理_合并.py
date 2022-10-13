import pandas as pd


data_K = pd.read_excel(r'实验成绩.xlsx')

data_P = pd.read_excel(r'雨课堂.xlsx')

data_H = pd.merge(data_K, data_P, on="学号", how="outer")

# data_H['平时(必填)'] = round(data_H['平时'],0)
#
# data_H.rename(columns={'姓名_x': '姓名', '学号_x': '学号'}, inplace=True) # 修改列名

data_H.to_excel('最终.xlsx',index=False)