from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

c = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=Faker.week, type_="category"))
    .add("境外输入", [10, 20, 30, 40, 30, 50, 10], type_="bar", stack="stack0")
    .add("新增本土", [20, 40, 60, 10, 20, 30, 25], type_="bar", stack="stack0")
    .add("无症状患者", [11, 22, 35, 45, 10, 20, 20], type_="bar", stack="stack0")
    .set_global_opts(title_opts=opts.TitleOpts(title="本周患者数")))
c.render('柱状坐标图.html')