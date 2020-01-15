# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
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
