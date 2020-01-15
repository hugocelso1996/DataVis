import Cleaned_Data
from Cleaned_Data import (df, df_year)



import chart_studio.plotly as py
import plotly.graph_objs as go

#Create a df for this plot
#TODO we need to change the

trace_1 = go.Scatter(x = df_year[df_year['state'] =='canceled'].deadline_years, y = df_year[df_year['state'] =='canceled'].ID,
                    name = 'Canceled',
                    line = dict(width = 1,
                                color = 'rgb(3, 5, 18)'))

trace_2 = go.Scatter(x = df_year[df_year['state'] =='failed'].deadline_years, y = df_year[df_year['state'] =='failed'].ID,
                    name = 'Failed',
                    line = dict(width = 1,
                                color = 'rgb(62, 83, 160)'))

trace_3 = go.Scatter(x = df_year[df_year['state'] =='successful'].deadline_years, y = df_year[df_year['state'] =='successful'].ID,
                    name = 'Successful',
                    line = dict(width = 1,
                                color = 'rgb(89, 159, 196)'))



layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')


fig_plot = go.Figure(data = [trace_1, trace_2, trace_3], layout=layout)
fig_plot.update_layout(legend_orientation="h")
