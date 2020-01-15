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

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig_bar.update_layout(barmode='group', xaxis_tickangle=45)