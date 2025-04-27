import streamlit as st
import duckdb as db
import pandas as pd
import pydeck as pdk
import plotly.express as px

st.write("# Welcome to Streamlit! 👋")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)

#Result2 - Count By Country
result_2 = db.sql(f"SELECT Country, count(*) as count FROM df group by Country order by count desc limit 10").df()
st.subheader('👑Top 10 Country by Number of Starbucks')
#st.write(result_2)
 
fig = px.bar(result_2, x='Country', y='count')
st.plotly_chart(fig)