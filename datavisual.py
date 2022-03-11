import numpy as np
from pyecharts.charts import Map,Timeline,Grid,Line,Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from dataset import dataset
tl=Timeline(init_opts=opts.InitOpts(
        # 图表画布宽度，css 长度单位。
        width="1527px",
        height="744px",
        # 图表画布高度，css 长度单位。
        page_title="电力数据可视化",
        theme=ThemeType.PURPLE_PASSION,

        ))
#print([list(z) for z in zip(Faker.choose(), Faker.values())])
year=["{}年".format(i) for i in range(2012,2022)]
data=[int(i) for i in np.random.randint(0,140,10)]
#data=[type(i) for i in range(10)]


for i in range(2012, 2022):
    j = i - 2012#j从零开始
    x, y1,y2,y3 =year,dataset.powersupply,dataset.powergrid,dataset.powerconstruct#Faker.choose(),Faker.values()#
    line= (
        Line(init_opts=opts.InitOpts(chart_id="0003"))
        #旋转函数
            .add_js_funcs(
            """
        var rotation = 0;
        setInterval(function () {
            chart_1234.setOption({
                graphic: {
                    id: 'logo',
                    rotation: (rotation += Math.PI / 360) % (Math.PI * 2)
                }
            });
        }, 30);
            """
        )
            .add_xaxis(x)
            .add_yaxis(
            "-",
            y_axis=y3,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="电力建设总投资(单位：亿元)",
                                         coord=[x[j],y3[j]],
                                         value=y3[j],
                                         itemstyle_opts=opts.ItemStyleOpts(
                                             color="rgb(37, 186, 165)"))],
                                        symbol=""
                #label_opts=opts.LabelOpts(color="rgb(106, 176, 184)")
            ),
            linestyle_opts=opts.LineStyleOpts(color="rgb(37, 186, 165)",),
            is_symbol_show=False,

                )
            #is_symbol_show=False
        .add_yaxis(
            "-",
            y_axis=y1,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="电源建设总投资(单位：亿元)",
                                         coord=[x[j],y1[j]],
                                         value=y1[j],
                                         itemstyle_opts=opts.ItemStyleOpts(
                                             color="rgb(252, 85, 49)"))],
                #label_opts=opts.LabelOpts(color="rgb(106, 176, 184)")
            ),
            linestyle_opts=opts.LineStyleOpts(color="rgb(252, 85, 49)",),
            is_symbol_show=False,

        )
        .add_yaxis(
            "-",
            y_axis=y2,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="电网建设总投资(单位：亿元)",
                                         coord=[x[j],y2[j]],
                                         value=y2[j],
                                         itemstyle_opts=opts.ItemStyleOpts(
                                             color="rgb(223, 191, 23)"))],
                #label_opts=opts.LabelOpts(color="rgb(106, 176, 184)")
            ),
            linestyle_opts=opts.LineStyleOpts(color="rgb(223, 191, 23)",),
            is_symbol_show=False
            #is_symbol_show=False
        )
        .set_global_opts(
                        title_opts=opts.TitleOpts(subtitle="总投资/电网总投资/电源总投资(单位：亿元)",pos_top="18%",pos_left="80%"),
                         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45),
                                                  interval=0),
                        yaxis_opts=opts.AxisOpts(min_=2000,max_=8500),
                         legend_opts=opts.LegendOpts(is_show=False),

                         visualmap_opts=opts.VisualMapOpts(max_=300000,
                                                           pos_left="1%",
                                                            pos_top="5%",
                                                           dimension=0,
                                                           range_text=['High', 'Low'],
                                                           textstyle_opts=opts.TextStyleOpts(color="rgb(205, 205, 211)")),

                         #tooltip_opts=opts.TooltipOpts(is_show=False)
                         graphic_opts=opts.GraphicImage(
                             graphic_item=opts.GraphicItem(
                                 left=160,
                                 top=50,
                                 bounding="raw",
                                 id_='logo',
                                 origin=(75,75)
                             ),
                             graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                                 image=r'..\dataset\bingdwendwen.png',
                                 opacity=1,
                                 width=200,
                                 height=200,
                             )
                        )
                )
         )


    bar = (
        Bar(init_opts=opts.InitOpts(chart_id="0001"))
            .add_xaxis(dataset.province)
            .add_yaxis("",dataset.ele[j])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(subtitle="全国各省用电量(单位：)",pos_top="32%",
                                                       ),

         )
    )
    map0 = (
        Map(init_opts=opts.InitOpts(chart_id="0002"))
        .add(series_name="年发电量",##############################################
             data_pair=[list(z) for z in zip(dataset.province, dataset.ele[j])],
             maptype="china",
             zoom=1.1,
             is_map_symbol_show=False,
             emphasis_itemstyle_opts=opts.ItemStyleOpts(area_color="",),

             )

        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(border_color="",area_color="",color0="rbg(39, 40, 34)"),
            text_style_opts=opts.TextStyleOpts(color="#0000")
            )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="全国{}年度电力相关数据可视化".format(i),
                subtitle="各省份年发电量(单位：)",
                pos_left="center",
                item_gap=180),
            legend_opts=opts.LegendOpts(pos_top="100px",is_show=False),


            )
            #graphic_imagestyle_opts=opts.GraphicImage()


        )
           #     visualmap_opts=opts.VisualMapOpts(
           #
           #     max_=max([num[1][0] for num in data]),
           # min_ = min([num[1][0] for num in data]),
           #
           #                     pos_left = '5%',
           #                                pos_bottom = 'center'


    # page = Page(layout=Page.DraggablePageLayout,)
    # page.add(map0,liquid,funnel,pie,radar)
    grid_chart=(
            Grid(init_opts=opts.InitOpts())
                .add(line, grid_opts=opts.GridOpts(pos_left="79%", pos_right="5%", pos_top="25%", pos_bottom="10%"))
                .add(bar, grid_opts=opts.GridOpts(pos_left="3%", pos_right="40%", pos_top="40%", pos_bottom="%2"))
                .add(map0, grid_opts=opts.GridOpts())
    )
    tl.add(grid_chart,"{}年".format(i))#只接受基本类型
    tl.add_schema(
        label_opts=opts.LabelOpts(
            interval=0,
            position="right",
            rotate=-45
            ),
        width = "50px",
        height = "700px",
        pos_bottom= "-5px",
        pos_right="-2px",
        orient='vertical',
        control_position="right",
        is_inverse=True,
        #is_rewind_play=True
        #is_timeline_show=False,
            )
tl.add_js_funcs("""
                var rotation = 0;
                setInterval(function () 
                    {
                    chart_1234.setOption({
                        graphic: {
                            id:"logo",
                            rotation: (rotation += Math.PI / 360) % (Math.PI * 2)
                        }
                    });
                });
                """)
#grid_chart.render()
tl.render(r"..\visual\datavisual.html")
    #page.save_resize_html("render.html",dest="visual.html",cfg_file="pos.json")


