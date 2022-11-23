from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.faker import Faker

line1=(
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis('新增患者人数',Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title='12月份新增患者'))
)
line1.render('折线图.html')



