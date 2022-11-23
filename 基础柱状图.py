from  pyecharts.charts import Bar
from pyecharts.options import *

bar = Bar()
bar.add_xaxis(["4月","5月","6月","7月","8月","9月","10月"])
bar.add_yaxis("新增人数", [1320,143,517,803,721,356,583])
bar.render("基础柱状图.html")



