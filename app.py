import pandas as pd
import datetime as datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State
import assets as assets



import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#! pip install plotly
#!pip install chart_studio

import chart_studio.plotly as py
import plotly.graph_objs as go

############


# read data
path = 'data/ks-projects-201801.csv'
df = pd.read_csv(path, header = 0, sep = ',')

# get dataframe info
df.info()

df.head()

#Remove month and day from launched column
new = df['launched'].str.split('-', n = 1, expand = True)
df['launched year'] = new[0]

#Remove month and day from launched column
new = df['deadline'].str.split('-', n = 2, expand = True)
df['deadline_YM'] = new[0].add('-').add(new[1])

#Remove launched year < 1990
df['launched year'] = df['launched year'].astype(int)

df = df[df['launched year'] > 1990]

#Removing a country with an unreadable name
df = df[df.country != 'N,0"']

cols = list(df.columns.values)
df = df[['ID',
 'name',
 'category',
 'main_category',
 'currency',
 'deadline',
 'deadline_YM',
 'goal',
 'launched',
 'launched year',
 'pledged',
 'state',
 'backers',
 'country',
 'usd pledged',
 'usd_pledged_real',
 'usd_goal_real']]

# Easy way pass parameter to every callback (year parameter as input to each graph)
# Global variables do not work
# Use state if we are changing variables, then it updates the graphs /
# Create DataFrame with the calculations beforehand -> Queries to Dataframe

#TODO df_year needs to be able to process year ranges (e.g. 2011-2013) so we can plot the ranges

df.drop(columns=['goal', 'pledged'])
df[['deadline_years', 'deadline_months']] = df['deadline_YM'].str.split('-', expand=True)

#Create df for different plots

df_year = pd.DataFrame(df.groupby(['deadline_years', 'deadline_YM', 'state'])['ID'].count()).reset_index()
df_year['deadline_years'] = pd.to_numeric(df_year['deadline_years'])


#df for range slider
df_year_slider =df_year.copy()

#df for category plot
df_category_plot = pd.DataFrame(df.groupby(['deadline_years', 'main_category', 'state'])['ID'].count()).reset_index()
df_category_plot['deadline_years'] = pd.to_numeric(df_category_plot['deadline_years'])




codes = ["AUT","AUS","BEL","CAN","CHE","DEU","DNK","ESP","FRA","GBR","HKG","IRL","ITA","JPN","LUX","MEX","NLD","NOR","NZL","SWE","SGP","USA"]
table = df.groupby(['country','launched year','state'])['ID'].count()
table = table.to_frame().reset_index()
table['%'] = (100 * table['ID'] / table.groupby(['launched year', 'country'])['ID'].transform('sum')).round(1)

table
count = 0
for i in range(len(table["country"])):
    count += 1
    print(count)
    for h in range(len(codes)):
        if table["country"][i] == codes[h][0:2]:
            if table["country"][i] == "AU":
                table["country"][i] = "AUS"
                continue
            #             if table["country"][i]=="AT":
            #                 table["country"][i]="AUT"
            #                 continue
            print(table["country"][i], "", codes[h][0:2], "1stIf ", codes[h])
            table["country"][i] = codes[h]
            continue
        elif table["country"][i] == codes[h][0::2]:
            print(table["country"][i], "", codes[h][0::2], "2ndIf ", codes[h])
            table["country"][i] = codes[h]
            continue
        else:
            if table["country"][i] == "IE":
                print(table["country"][i], "else")
                table["country"][i] = "IRL"
                continue
table.country.unique()
table[(table["state"] == "failed") & (table['launched year'] == 2015)]["country"]
table.country.unique()

import Cleaned_Data
from Cleaned_Data import df
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# category names
categories = df.main_category.unique().astype(str)
# df with only successful projects
succ = df[df.state == 'successful']
# sum usd_goal_real per category for succ projects
pub_g = succ.usd_goal_real[df.main_category == 'Publishing'].sum()
film_g = succ.usd_goal_real[df.main_category == 'Film & Video'].sum()
music_g = succ.usd_goal_real[df.main_category == 'Music'].sum()
food_g = succ.usd_goal_real[df.main_category == 'Food'].sum()
design_g = succ.usd_goal_real[df.main_category == 'Design'].sum()
crafts_g = succ.usd_goal_real[df.main_category == 'Crafts'].sum()
games_g = succ.usd_goal_real[df.main_category == 'Games'].sum()
comics_g = succ.usd_goal_real[df.main_category == 'Comics'].sum()
fashion_g = succ.usd_goal_real[df.main_category == 'Fashion'].sum()
theater_g = succ.usd_goal_real[df.main_category == 'Theater'].sum()
art_g = succ.usd_goal_real[df.main_category == 'Art'].sum()
photo_g = succ.usd_goal_real[df.main_category == 'Photography'].sum()
tech_g = succ.usd_goal_real[df.main_category == 'Technology'].sum()
dance_g = succ.usd_goal_real[df.main_category == 'Dance'].sum()
journ_g = succ.usd_goal_real[df.main_category == 'Journalism'].sum()

# sum usd_pledged_real per category for succ projects
pub_m = succ.usd_pledged_real[df.main_category == 'Publishing'].sum()
film_m = succ.usd_pledged_real[df.main_category == 'Film & Video'].sum()
music_m = succ.usd_pledged_real[df.main_category == 'Music'].sum()
food_m = succ.usd_pledged_real[df.main_category == 'Food'].sum()
design_m = succ.usd_pledged_real[df.main_category == 'Design'].sum()
crafts_m = succ.usd_pledged_real[df.main_category == 'Crafts'].sum()
games_m = succ.usd_pledged_real[df.main_category == 'Games'].sum()
comics_m = succ.usd_pledged_real[df.main_category == 'Comics'].sum()
fashion_m = succ.usd_pledged_real[df.main_category == 'Fashion'].sum()
theater_m = succ.usd_pledged_real[df.main_category == 'Theater'].sum()
art_m = succ.usd_pledged_real[df.main_category == 'Art'].sum()
photo_m = succ.usd_pledged_real[df.main_category == 'Photography'].sum()
tech_m = succ.usd_pledged_real[df.main_category == 'Technology'].sum()
dance_m = succ.usd_pledged_real[df.main_category == 'Dance'].sum()
journ_m = succ.usd_pledged_real[df.main_category == 'Journalism'].sum()

# BAR CHART code
fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    x=categories,
    y=[pub_g, film_g, music_g, food_g, design_g, crafts_g, games_g, comics_g,
       fashion_g, theater_g, art_g, photo_g, tech_g, dance_g, journ_g],
    name='Goal Real (USD)',
    marker_color='rgb(62, 109, 178)'
))
fig_bar.add_trace(go.Bar(
    x=categories,
    y=[pub_m, film_m, music_m, food_m, design_m, crafts_m, games_m, comics_m,
       fashion_m, theater_m, art_m, photo_m, tech_m, dance_m, journ_m],
    name='Pledged Real (USD)',
    marker_color='rgb(44, 42, 87)'
))

fig_bar.update_layout(barmode='group', xaxis_tickangle=45)

import plotly.graph_objs as go
from plotly.subplots import make_subplots

top_labels = ['Successful projects','Failed projects', 'Canceled projects']

colors = ['rgb(62, 83, 160)', 'rgb(72, 134, 187)','rgb(114, 184, 205)']

#TODO change the x_data into the actual count of ID's per year (always all three states)
#Numbers display numbers of IDs per year per category
#First row is Art label, Second Comics...

x_data = [[31, 58, 9],
          [37, 52, 10],
          [46, 42, 7],
          [25, 65, 9],
          [35,50,14],
          [24, 65, 10],
          [36, 45, 18],
          [54, 37, 8],
          [24, 62, 12],
          [60, 34, 5],
          [41, 50, 8],
          [30, 60, 9],
          [20, 63, 15],
          [62, 33, 5],
          [21, 66, 11],]

#TODO y_data should stay the same, so only change x_values
y_data = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts',
       'Games', 'Comics', 'Fashion', 'Theater', 'Art', 'Photography',
       'Technology', 'Dance', 'Journalism']

fig_cat = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig_cat.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig_cat.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.04, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=110, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.03, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig_cat.update_layout(annotations=annotations)

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



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = app.server

style = {'display': 'inline-block',
         'border-radius': '3px',
         'box-shadow': '5px 5px 5px grey',
         'background-color': '#FFFFFF',
         'padding': '5px',
         'margin-top': '20px',
         'margin-bottom': '30px',
         'margin-left': '30px',
         'margin-right': '30px'}

body = dbc.Container(
    [
        dbc.Row(
                dbc.Col(
                        dbc.NavbarSimple(
                            children=[
                                dbc.DropdownMenu(
                                    children=[
                                        dbc.DropdownMenuItem(dbc.Label("Choose the year you want to display (2009 - 2018)", html_for="slider")),
                                        dcc.RangeSlider(id="slider_year",
                                                        min=int(df_year_slider["deadline_years"].min()),
                                                        max=int(df_year_slider["deadline_years"].max()),
                                                        step=None,
                                                        value=[int(df_year_slider["deadline_years"].min()),
                                                               int(df_year_slider["deadline_years"].max())],
                                                        marks={int(i): str(i) for i in
                                                               df_year_slider['deadline_years']}),
                                        dbc.DropdownMenuItem(dbc.Label("Choose between different Project States", html_for="dropdown")),
                                        dcc.Dropdown(
                                            id="category_selection",
                                            options=[
                                                {"label": "Successful", "value": 1},
                                                {"label": "Failed", "value": 2},
                                                {"label": "Canceled", "value": 3},
                                            ],
                                            value=[1, 2],
                                            multi=True

                                        ),
                                        dbc.DropdownMenuItem(dbc.Label("Choose one Project State for the World Map")),
                                        dbc.RadioItems(
                                            options=[
                                                {"label": "successful", "value": 1},
                                                {"label": "failed", "value": 2},
                                                {"label": "canceled", "value": 3},
                                            ],
                                        value=1,
                                        id="input"),
                                    ],
                                    nav=True,
                                    in_navbar=True,
                                    label="Project Parameter Menu",
                                ),
                            ],
                            brand="Overview of Crowdfunding Project on Kickstarter",
                            brand_href="#",
                            color='#084489',
                            dark=True,
                        ))),
        dbc.Row(
            [
                dbc.Col(
                        [
                            html.H4("World Graph - Countries Distribution", style={'text-align': 'center'}),
                            dcc.Graph(
                                id="fig_map",
                                figure=fig_map
                            ),
                        ], style=style
                    ),
                dbc.Col(
                        [
                            html.H4('Number of Projects by Year and State', style={'text-align': 'center'}),
                            dcc.Graph(
                                id="fig_plot",
                                figure=fig_plot
                            ),
                        ], style=style
                            )
            ], align="center"),

        dbc.Row(
            [
                dbc.Col(
                        [
                            html.H4("Top 10 Projects - Highest Pledges", style={'text-align': 'center'}),
                            dcc.Graph(
                                id="fig_top",
                                figure=fig_top
                            ),
                        ], style=style
                    ),
                dbc.Col(
                    [
                        html.H4("Pledged vs Target - Category of Projects", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_bar",
                            figure=fig_bar
                        ),
                    ], style=style,
                        )
            ], align="center"),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Project Categories Comparison by State", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_pie",
                            figure=fig_pie
                        ),
                    ], style=style,
                    ),
                dbc.Col(
                    [
                        html.H4("Top 10 Projects for most Money Pledged", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_cat",
                            figure=fig_cat
                        ),
                    ],  style=style,
                        )
                ], align="center"),
    ], style={'backgroundColor': '#FAFAFA'}, fluid=True)



app.layout = html.Div([body])

@app.callback(Output('fig_plot', 'figure'),
              [Input('slider_year', 'value'),
               Input('category_selection', 'value')])
def update_time_series(year_value, category_value):

    year_value1 = year_value[0]
    year_value2 = year_value[1]

    dff = df_year[df_year['deadline_years'].between(year_value1, year_value2, inclusive=True)]
    #dff2 = df_year[df_year['deadline_years'].between(year_value1, year_value2, inclusive=True)]


    colors = ['rgb(3, 5, 18)', 'rgb(62, 83, 160)', 'rgb(89, 159, 196)']
    category_meaning = {1: "successful",
                        2: "failed",
                        3: "canceled"}

    fig_plot = go.Figure()

    i = 0
    trace_list = []

    for i in category_value:

        trace = go.Scatter(x=dff[dff['state'] == category_meaning.get(i)].deadline_YM,
                         y=dff[dff['state'] == category_meaning.get(i)].ID,
                         name=category_meaning.get(i),
                         line=dict(width=2.5,color=colors[i-1]))
        trace_list.append(trace)

    layout = go.Layout(title='Time Series Plot',
                       hovermode='closest',
                       legend_orientation="h")

    fig_plot.add_traces(trace_list)

    return fig_plot


@app.callback(Output('fig_pie', 'figure'),
              [Input('slider_year', 'value'),
               Input('category_selection', 'value')])
def update_pie_categories(year_value, category_value):

    vangogh_colors = ['rgb(3, 5, 18)', 'rgb(25, 25, 51)', 'rgb(44, 42, 87)', 'rgb(58, 60, 125)', 'rgb(62, 83, 160)',
              'rgb(62, 109, 178)', 'rgb(72, 134, 187)', 'rgb(89, 159, 196)', 'rgb(114, 184, 205)', 'rgb(149, 207, 216)',
              'rgb(192, 229, 232)', 'rgb(234, 252, 253)','rgb(240, 252, 253)','rgb(245, 252, 253)','rgb(250, 252, 253)']

    category_meaning = {1: "successful",
                        2: "failed",
                        3: "canceled"}

    year_value1 = year_value[0]
    year_value2 = year_value[1]

    dff = df_category_plot[df_category_plot['deadline_years'].between(year_value1, year_value2, inclusive=True)]

    i = 0
    trace_list = []
    full_data = pd.DataFrame(columns=['main_category', 'ID'])

    for i in category_value:
        values = dff[dff['state'] == category_meaning[i]]
        trace_list.append(values)
        # trace_list.append(values[['main_category', 'ID']])

    full_data = pd.concat(trace_list).fillna(0).astype(str).sort_index().reset_index(drop=True)
    # full_data = full_data.groupby(['main_category']).sum()
    full_data = full_data.drop(columns=['deadline_years', 'state'])
    full_data['ID'] = pd.to_numeric(full_data['ID'])
    summed = full_data.groupby('main_category').sum().reset_index()
    test = summed.sort_values(by='ID', ascending=False)
    labels = test['main_category'].tolist()
    summed = test.drop(columns=['main_category'])
    summed = summed.values.tolist()

    values_list = []
    for sublist in summed:
        for val in sublist:
            values_list.append(val)

    fig_pie = go.Figure()

    trace = go.Pie(labels=labels, values=values_list, marker_colors=vangogh_colors)
    fig_pie.add_traces(trace)

    fig_pie.update_traces(hole=.4, hoverinfo="label+percent")
    fig_pie.update_layout(annotations=[dict(text=' All Projects', x=0.04, y=0.95, font_size=14, showarrow=False)])

    return fig_pie

@app.callback(Output('fig_cat', 'figure'),
              [Input('slider_year', 'value'),
               Input('category_selection', 'value')])
def update_category_states(year_value, category_value):

    year_value1 = year_value[0]
    year_value2 = year_value[1]

    top_labels = ['Successful projects', 'Failed projects', 'Canceled projects']

    colors = ['rgb(62, 83, 160)', 'rgb(72, 134, 187)', 'rgb(114, 184, 205)']

    category_value = [1,2,3]
    category_meaning = {1: "successful",
                        2: "failed",
                        3: "canceled"}

    dff = df_category_plot[df_category_plot['deadline_years'].between(year_value1, year_value2, inclusive=True)]

    i = 0
    trace_list = []
    full_data = pd.DataFrame(columns=['main_category', 'ID'])

    for i in category_value:
        values = dff[dff['state'] == category_meaning[i]]
        trace_list.append(values)
        # trace_list.append(values[['main_category', 'ID']])

    full_data = pd.concat(trace_list).fillna(0).astype(str).sort_index().reset_index(drop=True)

    full_data = full_data.drop(columns=['deadline_years'])

    full_data['ID'] = pd.to_numeric(full_data['ID'])
    summed = full_data.groupby(['main_category', 'state']).sum().reset_index()
    ##test = summed.sort_values(by='ID', ascending=False)
    # labels = test['main_category'].tolist()
    # summed = test.drop(columns=['main_category'])
    # summed = summed.values.tolist()

    col_one_list = summed['ID'].tolist()


    total_lists = 15
    result = [col_one_list[i::total_lists] for i in range(total_lists)]
    result_df = pd.DataFrame(result)
    result_df['SUM'] = result_df.sum(axis=1)
    df_new = result_df.loc[:, result_df.columns != 'SUM'].div(result_df['SUM'], axis=0)
    df_new = df_new.round(2)
    df_new[df_new.select_dtypes(include=['number']).columns] *= 100
    df_new = df_new.astype(int)

    x_data = df_new.values.tolist()
    y_data = ['Theater', 'Technology', 'Publishing', 'Photography', 'Music', 'Journalism',
              'Games', 'Food', 'Film & Video', 'Fashion', 'Design', 'Dance', 'Crafts', 'Comics', 'Art']

    fig_cat = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig_cat.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))

    fig_cat.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.04, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        #paper_bgcolor='rgb(248, 248, 255)',
        #plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=110, r=10, t=140, b=80),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.03, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=14,
                                              color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i] / 2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i] / 2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

    fig_cat.update_layout(annotations=annotations)

    return fig_cat


@app.callback(Output("fig_map","figure"),
              [Input('slider_year', 'value'),
               Input("input", "value")])
def update_map(year_value, radio_item):

    year_value1 = year_value[0]
    year_value2 = year_value[1]

    category_meaning = {1: "successful",
                       2: "failed",
                       3: "canceled"}

    co = table[table['launched year'].between(year_value1, year_value2, inclusive=True)]
    co = co.drop(["launched year"], axis=1)
    co = co[co["state"] == category_meaning[radio_item]]
    co["ID"] = pd.to_numeric(co["ID"])
    co = co.drop("state", axis=1)
    new_co = co.groupby(["country"])['ID'].agg(sum)
    # percentage=table.groupby(["country"]).agg({"ID":'sum'})   new_table.div(country, level="country")*100
    new_co = pd.DataFrame(new_co)
    new_co = new_co.reset_index()
    sum_ = new_co["ID"].sum()
    new_co["percent"] = (new_co["ID"].div(sum_)).apply(lambda x: x * 100)

    fig_map = go.Figure(data=go.Choropleth(
        locations=new_co["country"],
        z=new_co["percent"],
        # text = table[(table["state"]=="failed") & (table['launched year']==2017)]['country'],
        colorscale='Blues',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))

    return fig_map



if __name__ == "__main__":
    app.run_server(debug=True)
