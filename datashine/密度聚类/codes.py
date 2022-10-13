# 导入模块
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing  # 用于变量的标准化处理
from sklearn import cluster
import numpy as np
import seaborn as sns  # 用于绘制聚类的效果散点图


# 用于DataFrame显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# 用于最后输出的图形汉字显示正常
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 读取外部数据
Province = pd.read_excel('./Province.xlsx')
Province.head()  # 显示表格的前五行
# 绘制出生率与死亡率散点图
plt.scatter(Province.Birth_Rate, Province.Death_Rate)  # Birth_Rate作为x Death_Rate作为y
# 添加轴标签
plt.xlabel('Birth_Rate')
plt.ylabel('Death_Rate')
# 显示图形
# plt.show()


# 选取建模的变量
predictors = ['Birth_Rate', 'Death_Rate']
# 变量的标准化处理
X = preprocessing.scale(Province[predictors])
X = pd.DataFrame(X)

# 构建空列表，用于保存不同参数组合下的结果
res = []
# 迭代不同的eps值
for eps in np.arange(0.001, 1, 0.05):
    # 迭代不同的min_samples值
    for min_samples in range(2, 10):
        dbscan = cluster.DBSCAN(eps=eps, min_samples=min_samples)
        # 模型拟合
        dbscan.fit(X)
        # 统计各参数组合下的聚类个数（-1表示异常点）
        n_clusters = len([i for i in set(dbscan.labels_) if i != -1])  # set函数用来创造一个无序不重复元素集合
        # 异常点的个数
        outlines = np.sum(np.where(dbscan.labels_ == -1, 1, 0))
        # 统计每个簇的样本个数
        stats = str(pd.Series([i for i in dbscan.labels_ if i != -1]).value_counts().values)
        res.append({'eps': eps, 'min_samples': min_samples, 'n_clusters': n_clusters, 'outlines': outlines, 'stats': stats})

# 将迭代后的结果存储到数据框中
df = pd.DataFrame(res)
# 根据条件筛选合理的参数组合
print(df.loc[df.n_clusters == 3, :])


# 利用上述的参数组合值，重建密度聚类算法
dbscan = cluster.DBSCAN(eps=0.801, min_samples=3)
# 模型拟合
dbscan.fit(X)
Province['dbscan_label'] = dbscan.labels_
# 绘制聚类的效果散点图  hue用于分类
sns.lmplot(x='Birth_Rate', y='Death_Rate', hue='dbscan_label', data=Province,
           markers=['*', 'd', '^', 'o'], fit_reg=False, legend=False)
# 添加省份标签
for x, y, text in zip(Province.Birth_Rate, Province.Death_Rate, Province.Province):
    plt.text(x+0.1, y-0.1, text, size=8)
# 添加参考线
plt.hlines(y=5.8, xmin=Province.Birth_Rate.min(), xmax=Province.Birth_Rate.max(),
           linestyles='--', colors='red')
plt.vlines(x=10, ymin=Province.Death_Rate.min(), ymax=Province.Death_Rate.max(),
           linestyles='--', colors='red')
# 添加轴标签
plt.xlabel('Birth_Rate')
plt.ylabel('Death_Rate')
# 显示图形
plt.show()
