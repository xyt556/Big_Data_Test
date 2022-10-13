import pandas as pd
from pyecharts.charts import Sankey
from pyecharts import options as opts
import os
from pyecharts.charts import Pie,Bar,Map,Page,Funnel
# df =  pd.DataFrame(
# {
# '类型':['遥控','遥控','遥控','非遥控','非遥控','非遥控'],
# '产品名称':['机器人','猛击赛车','莱肯赛车','机器人','猛击赛车','莱肯赛车'],
# '数量':[15,23,36,48,21,11]
# })
# print(df.head())
def get_data(df):
    nodes =[]
    for i in range(2):
        vales=df.iloc[:,i].unique()
        for value in vales:
            dic={}
            dic['name']=value
            nodes.append(dic)
            
    nodes1 = []
    for id in nodes:
        if id not in nodes1:
            nodes1.append(id)
    # print(nodes1)

    links=[]
    for i in df.values:
        dic={}
        dic['source']=i[0]
        dic['target']=i[1]
        dic['value']=i[2]
        links.append(dic)
    return nodes1,links


# print(links)
def get_tu(tablename,df):
    nodes1,links = get_data(df)
    sankey = (
        Sankey(init_opts=opts.InitOpts(width="2000px", height="800px"))
        .add(
            tablename,
            nodes1,
            links,
            pos_top="10%",
            node_width = 30,  #每个桑基图矩形的宽度
            node_gap= 12,  #桑基图中每一列任意两个矩形节点之间的间隔。
            is_draggable = True,
            layout_iterations = 5,

            # focus_node_adjacency=True,
            itemstyle_opts=opts.ItemStyleOpts(border_width=2, border_color="#aaa"),
            linestyle_opt=opts.LineStyleOpts(opacity=0.8, curve=0.5, color='source'),
            label_opts=opts.LabelOpts(position='right'),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="付费路径分析"))
    )
    return sankey
##数据输出
file ='test.xlsx'
df_0826 = pd.read_excel(file,sheet_name='0826')
# df_0929 = pd.read_excel(file,sheet_name='0929')
# df_1222 = pd.read_excel(file,sheet_name='1222')
# df_0113 = pd.read_excel(file,sheet_name='0113')

sk1 = get_tu('0826数据',df_0826)
# sk2 = get_tu('0929数据',df_0929)
# sk3 = get_tu('1222数据',df_1222)
# sk4 = get_tu('0113数据',df_0113)

sk1.render("test0217.html")


##组合图表
# page = Page(layout=Page.DraggablePageLayout)
# page.add(sk4,sk3,sk2,sk1)
# page.render("无悔各测试付费路径.html")
# page.save_resize_html('组合图表.html',dest="无悔各测试付费路径.html") 
##,cfg_file="chart_config (2).json"
 ##如果用别的IDE的小伙伴，运行Page.save_resize_html之前，一定要把前面的page.render("test.html")这句注释掉啊！！！
print('更新完毕')