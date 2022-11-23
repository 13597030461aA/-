from pyecharts.charts import  Map
from  pyecharts.options import *
# 准备数据
data=[
    ('南宁市',110),
    ('柳州市',20),
    ('桂林市',50),
    ('玉林市',19),
    ('百色市',29),
    ('河池市',32),
    ('贵港市',49),
    ('北海市',88),
    ('钦州市',19),
    ('贺州市',4),
    ('梧州市',21),
    ('来宾市',12),
    ('崇左市',13),
    ('防城港市',9),
]
# 创进地图对象
map = Map()
map.add('广西省确诊人数',data,'广西')
map.set_global_opts(
    # 显示地图色块
    # title_opts=TitleOpts('广西疫情地图'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':0,'max':9,'label':'0-9人','color':'#4aae83'},
            {'min': 10, 'max': 19,'label': '10-19人', 'color': '#de9ba1'},
            {'min': 20, 'max': 29, 'label': '20-29人', 'color': '#c85863'},
            {'min': 30, 'max': 49, 'label': '30-49人', 'color': '#ffd633'},
            {'min': 50, 'max': 9999, 'label': '>50人', 'color': '#ff3300'},
        ]
          ),
)
#绘图
map.render('广西疫情确诊人数.html')




