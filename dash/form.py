from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line

df1 = pd.read_csv("canhui.csv",encoding = 'gbk')


app = Flask(__name__)

# 准备工作

regions_available = list(df1.CountryName.dropna().unique())
# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()



@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df2.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)

@app.route('/hurun',methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df2.query("CountryName=='{}'".format(the_region))
#     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
#     print(df_summary.head(5)) # 在后台检查描述性统计
#     ## user select
    # print(dfs)
#     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="CountryName", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

#     # plotly.offline.plot(data, filename='file.html')
	
#     with open("render.html", encoding="utf8", mode="r") as f:
#         plot_all = "".join(f.readlines())
			
    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )




if __name__ == '__main__':
    app.run(debug=True,port=8000)