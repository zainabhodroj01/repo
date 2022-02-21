import streamlit as st
import pandas as pd
deaths = pd.read_csv("Death Cause Reason by Country.csv")
import pandas as pd 
import numpy as np 
import seaborn as sns 
import plotly.express as px 
import plotly as plt

#adding a new column with the total number of deaths 
deaths1= list(deaths)
deaths1.remove("Country Name")

deaths["total_deaths_per_country"] = deaths[deaths1].sum(axis=1)

@st.cache
def load_data(nrows):
    return deaths
deaths= load_data(10)

st.write("""
# Death Cause by country
""")
if st.button("Overview of data")== True :
    st.write(load_data(10))

import plotly.graph_objects as go 

st.write(px.line(deaths, x="Country Name", y='total_deaths_per_country', labels={"x": "Country Name", "y": "total_deaths_per_country"}))


deaths2 = pd.read_csv("Death Cause Reason by Country.csv")
total_deaths = deaths2.sum(axis=0)[1:].sort_values(ascending=True).values
causes_of_death= deaths2.sum(axis=0)[1:].sort_values(ascending=True).index

fig = go.Figure(go.Bar(
            x=total_deaths,
            y=causes_of_death,
            orientation='h'))
st.write("## Top Reasons for Deaths in the world")
st.write(fig)

import plotly.express as px 
fig2 = px.choropleth(deaths, locations = 'Country Name', locationmode = 'country names', color = 'Covid-19 Deaths')

st.write("## Global spread of Covid19 Deaths")
st.write(fig2)


top_10_countries_with_Diabetes = deaths.loc[deaths["Diabetes "].sort_values(ascending=False)[:10].index]["Country Name"].values
total_death_Diabetes  = deaths["Diabetes "].sort_values(ascending=False)[:10].values
import plotly.express as px
fig3 = px.pie(deaths, values=deaths["Diabetes "].sort_values(ascending=False)[:10].values, names=deaths.loc[deaths["Diabetes "].sort_values(ascending=False)[:10].index]["Country Name"].values)
st.write('## Top Countries suffering fom Diabetes')
st.write(fig3)

st.write('#### Scatter plot showing death causes due to Alzheimer and Parkinson diseases')
st.write(px.scatter(deaths, x= "Parkinson's disease", y= " Alzheimer's disease", color="Country Name"))


st.write('#### Scatter plot showing death causes due to Drug use and Road Injuries')
fig4 = go.Figure(go.Scatter(x=deaths["Drug use disorders"], y=deaths["Road injuries"], text=deaths["Country Name"], mode='markers', name='Deaths Cause'))
fig4.update_xaxes(title_text='Drug use disorders', type='log')
fig4.update_yaxes(title_text='Road injuries')

st.write(fig4)

st.write('#### Line graph showing death causes due to Covid-19 and Resporiratory diseases')
fig5= px.line_3d(deaths, x="Country Name",y="Covid-19 Deaths", z="Respiratory diseases ")
st.write(fig5)

st.write ("## Most deaths worldwide")

fig6 = px.line(deaths, x=deaths.loc[deaths["total_deaths_per_country"].sort_values(ascending=False)[:50].index]["Country Name"].values
        , y=deaths["total_deaths_per_country"].sort_values(ascending=False)[:50].values
        ,labels={"x": "top_50_countries_with_most_deaths", "y": "total_death_per_country"})
        
st.write(fig6)
# Most deaths worldwide
st.write ("## Top Countries with Violence and Conflict")

top_countries_with_Conflict = deaths.loc[deaths[" Conflict and terrorism"].sort_values(ascending=False)[:15].index]["Country Name"].values
top_countries_with_violence = deaths.loc[deaths["Interpersonal violence"].sort_values(ascending=False)[:15].index]["Country Name"].values


if st.button("top_countries_with_Conflict") ==True:
        st.write(top_countries_with_Conflict)

if st.button("top_countries_with_violence") ==True:
        st.write(top_countries_with_violence)
