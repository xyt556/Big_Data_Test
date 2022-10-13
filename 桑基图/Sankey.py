# -*- codeing =utf-8 -*-
# @Time : 2022/7/12$ 11:55
# Author : YantaoXI
# @File : Sankey.py
# @Software: PyCharm


if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.sankey import Sankey

    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    # 消费收入与支出数据
    flows = [0.7, 0.3, -0.3, -0.1, -0.3, -0.1, -0.1, -0.1]
    # 流的标签列表
    labels = ["工资", "副业", "生活", "购物", "深造", "运动", "其他", "买书"]
    # 流的方向
    orientations = [1, 1, 0, -1, 1, -1, 1, 0]
    # 创建Sankey类对象
    sankey = Sankey()
    sankey.add(flows=flows,  # 收入与支出数据
               labels=labels,  # 数据标签
               orientations=orientations,  # 标签显示的方向
               color='black',  # 边缘线条颜色
               fc="lightgreen",  # 填充颜色
               patchlabel="生活消费",  # 图表中国心的标签
               alpha=0.7)

    # 桑基图绘制完成的对象
    diagrams = sankey.finish()
    diagrams[0].texts[4].set_color("r")  # 将下标为4的数据标签设为红色
    diagrams[0].texts[4].set_weight("bold")  # 将下标为4的数据标签设为字体标签
    diagrams[0].text.set_fontsize(20)  # 将中心标签的字体大小设为20
    diagrams[0].text.set_fontweight("bold")  # 将中心标签的字体设为加粗
    plt.title('日常生活开支的桑基图')
    plt.show()

