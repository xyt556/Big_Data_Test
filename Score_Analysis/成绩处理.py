import pandas as pd
import numpy as np


data = pd.read_excel(r'计算机地质制图（实验+平时）.xlsx',sheet_name='实验',header=0)
# 归一化
max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))

data['实验总评'] = round(75 + 15 * data[['期末(必填)']].apply(max_min_scaler),0)
data['实验(必填)'] = data['实验总评']
data.to_excel('实验成绩.xlsx',index=False)

# data = pd.read_excel(r'C:\Users\xyt556\PycharmProjects\RS_Ocean\test\地理信息系统B实验成绩.xlsx',sheet_name='能源',header=0)
# # 归一化
# max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
#
# data['实验总评'] = round(75 + 15 * data[['期末(必填)']].apply(max_min_scaler),0)
# data['实验(必填)'] = data['实验总评']
# data.to_excel('能源.xlsx',index=False)
#
# data = pd.read_excel(r'C:\Users\xyt556\PycharmProjects\RS_Ocean\test\地理信息系统B实验成绩.xlsx',sheet_name='地信',header=0)
# # 归一化
# max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
#
# data['实验总评'] = round(75 + 15 * data[['期末(必填)']].apply(max_min_scaler),0)
# data['实验(必填)'] = data['实验总评']
# data.to_excel('地信.xlsx',index=False)