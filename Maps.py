from Cleaned_Data import table
import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

colorscale = ['rgb(3, 5, 18)', 'rgb(25, 25, 51)', 'rgb(44, 42, 87)', 'rgb(58, 60, 125)', 'rgb(62, 83, 160)',
          'rgb(62, 109, 178)', 'rgb(72, 134, 187)', 'rgb(89, 159, 196)', 'rgb(114, 184, 205)', 'rgb(149, 207, 216)',
          'rgb(192, 229, 232)', 'rgb(234, 252, 253)','rgb(240, 252, 253)','rgb(245, 252, 253)','rgb(250, 252, 253)']

fig_map = go.Figure(data=go.Choropleth(
    locations = table[(table["state"]=="failed") & (table['launched year']==2015)]["country"],
    z = table[(table["state"]=="failed") & (table['launched year']==2015)]["%"],
    #text = table[(table["state"]=="failed") & (table['launched year']==2017)]['country'],
    colorscale = colorscale,
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    #colorbar_title = 'Canceled Projects',
))

fig_map.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        showarrow = True
    )]
)

