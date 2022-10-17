import PCA as pc
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
if __name__ == "__main__":
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    df = pd.read_excel(r'.\data.xlsx',sheet_name= '因子分析2', header= 0, index_col= '编号')
    print(df)
    data = np.array(df)
    print(data)

    pca = pc.PCA(n_components=2)
    pca.fit(data,rowvar=False)
    res = pca.transform(data,rowvar=False)
    ratio = pca.variance_ratio(only=True)
    print("各特征的权重为: ratio = ",ratio)
    print("使用本库进行计算得到的PCA降维结果为: res = ", res)

    pca1 = PCA(n_components=2)
    res = pca1.fit_transform(data)
    ratio = pca1.explained_variance_ratio_
    print("各特征的权重为: ratio = ",ratio)
    print("使用sklearn.decomposition.PCA 验证的结果为: res = ", res)


    

