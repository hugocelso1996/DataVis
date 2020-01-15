import Cleaned_Data
from Cleaned_Data import df
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots

#categories pie charts
labels = df.main_category.unique()

vangogh_colors = ['rgb(3, 5, 18)', 'rgb(25, 25, 51)', 'rgb(44, 42, 87)', 'rgb(58, 60, 125)', 'rgb(62, 83, 160)',
          'rgb(62, 109, 178)', 'rgb(72, 134, 187)', 'rgb(89, 159, 196)', 'rgb(114, 184, 205)', 'rgb(149, 207, 216)',
          'rgb(192, 229, 232)', 'rgb(234, 252, 253)','rgb(240, 252, 253)','rgb(245, 252, 253)','rgb(250, 252, 253)']

#values for charts
values_all = df.main_category.value_counts()

# Pie charts for each state
fig_pie = make_subplots(rows=1, cols=1, specs=[[{'type': 'domain'}]])
fig_pie.add_trace(go.Pie(labels=labels, values= values_all, marker_colors=vangogh_colors),1, 1)


# Use `hole` to create a donut-like pie chart
fig_pie.update_traces(hole=.4, hoverinfo="label+percent")

fig_pie.update_layout(
    # Add annotations in the center of the donut pies.
    annotations=[dict(text=' All Projects', x=0.04, y=0.95, font_size=14, showarrow=False)])
