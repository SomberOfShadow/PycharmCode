# from pyecharts.charts import Map
#
Mapvalue = [155,10,66,78,33,80,190,53,49.6,88]
attr = ["湖南","广东","北京","上海","江苏", "新疆","河南","甘肃","西藏","黑龙江"]
# # map = Map("中国地图", width=600, height=600)
#
# map = Map()
# map.add("示例", attr, Mapvalue, maptype="china", visual_text_color="#000",is_label_show=True)
# map.render()


from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map


def map_base() -> Map:
    c = (
        Map()
        # .add("商家", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .add("示例", [(Mapvalue, attr)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    return c

map_base().render()
