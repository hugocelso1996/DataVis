import Cleaned_Data
from Cleaned_Data import (df, df_year)
import chart_studio.plotly as py
import plotly.graph_objs as go

# plot values
# getting top 10 projects
top = df.sort_values(by=['usd_pledged_real'], ascending=False).iloc[0:10]

proj_names = ['Project 10', 'Project 9', 'Project 8', 'Project 7', 'Project 6',
              'Project 5', 'Project 4', 'Project 3', 'Project 2', 'Project 1']
backers_num = [26, 44, 63, 22, 45, 69, 19, 66, 62, 79]

money = [6565782, 7072757, 8596474, 8782571, 9192055, 10266845, 12393139, 12779843, 13285226, 20338986]
# colors - Design- 'rgb(62, 109, 178)', Games - 'rgb(44, 42, 87)'


# plot
fig_top = go.Figure(data=[go.Scatter(
    x=proj_names,
    y=money,
    mode='markers',
    marker=dict(
        color=['rgb(62, 109, 178)', 'rgb(44, 42, 87)', 'rgb(44, 42, 87)', 'rgb(44, 42, 87)', 'rgb(62, 109, 178)',
               'rgb(62, 109, 178)', 'rgb(44, 42, 87)', 'rgb(62, 109, 178)', 'rgb(62, 109, 178)', 'rgb(62, 109, 178)'],
        size=backers_num, )
)])
# fig.update_layout(showlegend=True)
