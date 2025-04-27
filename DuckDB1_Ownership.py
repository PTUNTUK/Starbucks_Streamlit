import streamlit as st
import duckdb as db
import pandas as pd
import pydeck as pdk
import plotly.express as px

st.write("# Welcome to Streamlit! 👋")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)

#Result1 - Ownership type
results1 = db.sql(f'SELECT  "Ownership Type" as Ownership  , COUNT(*) as Total FROM df GROUP BY "Ownership Type" ORDER BY Total DESC').df()
fig = px.bar(results1, x='Ownership', y='Total')
st.subheader('Ownership Type📊')
st.write(results1)
st.plotly_chart(fig)

#Result 4 - Percentage Ownership Pie Chart
result_4 = db.sql(f'SELECT "Ownership Type" As "Ownership", count(*) as count FROM df group by "Ownership Type" ').df()
st.subheader('Percentage Ownership Pie Chart🥧')

#st.write(result_4)
fig_3 = px.pie(result_4, values='count', names='Ownership', title='Ownership Type')
st.plotly_chart(fig_3)