import streamlit as st
import duckdb as db
import pandas as pd
st.write("# Welcome to Streamlit! 👋")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
st.write(df)
#x = 'Bangkok'
x = st.sidebar.selectbox('Choose your city',['Bangkok','Ajman','Phuket'])
results = db.sql(f"SELECT count(*) FROM df where City='{x}'") #.df()
st.write(results)

st.markdown(
    """
    1 intro
    """
)
