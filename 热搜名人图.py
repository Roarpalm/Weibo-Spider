from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add(
        "热搜次数",
        [('特朗普', 205), ('肖战', 90), ('易烊千玺', 88), ('李佳琦', 72), ('詹姆斯', 67), ('张文宏', 62), ('卫健委', 59), ('迪士尼', 58), ('鹿晗', 56), ('李兰娟', 56), ('王一博', 55), ('蔡徐坤', 50), ('白岩松', 48), ('李文亮', 47), ('王俊凯', 45)],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="热搜次数"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_radius.html")
)
