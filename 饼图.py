from pyecharts import options as opts
from pyecharts.charts import Pie

teacher = ['境外病例', '本土病例', ]
num = [10, 9, ]
c = Pie()

c.add("", [list(z) for z in zip(teacher, num)])  # 设置圆环的粗细和大小
c.set_global_opts(title_opts=opts.TitleOpts(title="单日新增患者"))
c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
c.render()
c.render('饼图.html')