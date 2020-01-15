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
from Plots import fig_plot
from Maps import fig_map
from Pie import fig_pie
from Top_10 import fig_top
from Categories import fig_cat
from Bar import fig_bar
from Maps import table
from Cleaned_Data import (df,
                          df_year,
                          df_year_slider,
                          df_category_plot)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


body = dbc.Container(
    [
        dbc.Row(
                dbc.Col(
                        html.Div(
                            html.Img(
                                src=app.get_asset_url("kickstarter-logo.png"),
                                id="kickstarter-image",
                                style={
                                    "display":"block",
                                    "padding": 10,
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "width": "500px",
                                    "height": "60px",
                                    },
                             )), width={"size": 6, "offset": 3},)),
        dbc.Row(
                dbc.Col(
                            html.Div(
                                html.H4('Overview of the Crowdfunding Company "Kickstarter"'),
                                style={
                                    "color": 'black',
                                    'textAlign': 'center',
                                    'padding': 10,
                                    'margin-left': "auto",
                                    'margin-right': 'auto',
                                    },
                                    ), width={"size": 6, "offset": 3},
                        )),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Parameter Column", style={'text-align': 'center'}),
                        dbc.FormGroup(
                            [
                                dbc.Label("Choose the Year you want to analyse", html_for="slider"),
                                dcc.RangeSlider(id="slider_year",
                                                min=int(df_year_slider["deadline_years"].min()),
                                                max=int(df_year_slider["deadline_years"].max()),
                                                step=None,
                                                value=[int(df_year_slider["deadline_years"].min()), int(df_year_slider["deadline_years"].max())],
                                                marks={int(i): str(i) for i in df_year_slider['deadline_years']})
                            ],


                        ),
                        dbc.Label("Choose the state of the project", html_for="dropdown"),
                                dcc.Dropdown(
                                    id="category_selection",
                                    options=[
                                        {"label": "Successful", "value": 1},
                                        {"label": "Failed", "value": 2},
                                        {"label": "Canceled", "value": 3},
                                    ],
                                    value=[1,2],
                                    multi=True

                                ),
                    ], style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-bottom': '2px',
                                 'margin-left': '2px',
                                 'margin-right': '2px'

                                 }),

                dbc.Col(
                    [
                        html.H4("World Graph - Distribution by Countries", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_map",
                            figure=fig_map
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Choose One"),
                                dbc.RadioItems( options=[
                                {"label": "successful", "value": 1},
                                {"label": "failed", "value": 2},
                                {"label": "canceled", "value": 3},
                                ],
                                value=1,
                                id="input"
                                ),
                            ])

                            ], style={'display': 'inline-block',
                                         'border-radius': '3px',
                                         'box-shadow': '0px 0px 0px grey',
                                         'background-color': '#f9f9f9',
                                         'padding': '5px',
                                         'margin-bottom': '2px',
                                         'margin-left': '2px',
                                         'margin-right': '2px'
                                      }),

                dbc.Col(
                    [
                        html.H4('Number of Projects by Year and State', style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_plot",
                            figure=fig_plot
                        ),
                    ], style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-bottom': '2px',
                                 'margin-left': '2px',
                                 'margin-right': '2px'
                              }, width=4)]),

        dbc.Row(
            [
                dbc.Col(
                        [
                            html.H4("Top 10 Projects - Highest Pledges", style={'text-align': 'center'}),
                            dcc.Graph(
                                id="fig_top",
                                figure=fig_top
                            ),
                        ], style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-top': '10px',
                                 'margin-bottom': '2px',
                                 'margin-left': '10px',
                                 'margin-right': '10px'},
                    ),
                dbc.Col(
                    [
                        html.H4("Pledged vs Target - Category of Projects", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_bar",
                            figure=fig_bar
                        ),
                    ], style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-top': '10px',
                                 'margin-bottom': '2px',
                                 'margin-left': '10px',
                                 'margin-right': '10px'},
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
                    ], style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-top': '10px',
                                 'margin-bottom': '2px',
                                 'margin-left': '10px',
                                 'margin-right': '10px'},
                    ),
                dbc.Col(
                    [
                        html.H4("Top 10 Projects for most Money Pledged", style={'text-align': 'center'}),
                        dcc.Graph(
                            id="fig_cat",
                            figure=fig_cat
                        ),
                    ],  style={'display': 'inline-block',
                                 'border-radius': '3px',
                                 'box-shadow': '0px 0px 0px grey',
                                 'background-color': '#f9f9f9',
                                 'padding': '5px',
                                 'margin-top': '10px',
                                 'margin-bottom': '2px',
                                 'margin-left': '10px',
                                 'margin-right': '10px'},
                        )
                ], align="center"),
    ], style={'backgroundColor': '#ffffff'}, fluid=True)



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
                         line=dict(width=1,
                                   color=colors[i-1]))
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
    fig_pie.update_layout(title_text="Project Categories by State",
                          annotations=[dict(text=' All Projects', x=0.04, y=0.95, font_size=14, showarrow=False)])

    return fig_pie

@app.callback(Output('fig_cat', 'figure'),
              [Input('slider_year', 'value'),
               Input('category_selection', 'value')])
def update_pie_categories(year_value, category_value):

    year_value1 = year_value[0]
    year_value2 = year_value[1]

    top_labels = ['Successful projects', 'Failed projects', 'Canceled projects']

    colors = ['rgb(62, 83, 160)', 'rgb(72, 134, 187)', 'rgb(114, 184, 205)']

    category_value = [1,2,3]
    category_meaning = {1: "successful",
                        2: "failed",
                        3: "canceled"}

    # TODO change the x_data into the actual count of ID's per year (always all three states)

    dff = df_category_plot[df_category_plot['deadline_years'].between(year_value1, year_value2, inclusive=True)]

    i = 0
    trace_list = []
    full_data = pd.DataFrame(columns=['main_category', 'ID'])

    for i in category_value:
        values = dff[dff['state'] == category_meaning[i]]
        trace_list.append(values)
        # trace_list.append(values[['main_category', 'ID']])

    full_data = pd.concat(trace_list).fillna(0).astype(str).sort_index().reset_index(drop=True)
    full_data

    full_data = full_data.drop(columns=['deadline_years'])
    full_data
    full_data['ID'] = pd.to_numeric(full_data['ID'])
    summed = full_data.groupby(['main_category', 'state']).sum().reset_index()
    ##test = summed.sort_values(by='ID', ascending=False)
    # labels = test['main_category'].tolist()
    # summed = test.drop(columns=['main_category'])
    # summed = summed.values.tolist()

    col_one_list = summed['ID'].tolist()
    col_one_list

    total_lists = 15
    result = [col_one_list[i::total_lists] for i in range(total_lists)]
    result_df = pd.DataFrame(result)
    result_df.values
    result_df['SUM'] = result_df.sum(axis=1)
    result_df.values
    df_new = result_df.loc[:, result_df.columns != 'SUM'].div(result_df['SUM'], axis=0)
    df_new = df_new.round(2)
    df_new[df_new.select_dtypes(include=['number']).columns] *= 100
    df_new = df_new.astype(int)

    x_data = df_new.values.tolist()

    # TODO y_data should stay the same, so only change x_values
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
