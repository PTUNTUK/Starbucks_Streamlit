import streamlit as st
import duckdb as db
import pandas as pd
import pydeck as pdk
import plotly.express as px

st.write("# Welcome to Streamlit! 👋")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)

#Results3 - Map
results3 = db.sql("""
    SELECT Latitude, Longitude, COUNT(*) AS shop_count
    FROM df
    GROUP BY Latitude, Longitude
""").df()

#st.write(results3)

st.subheader('🌏Starbucks Map by Location')
st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=results3["Latitude"].mean(),  
            longitude=results3["Longitude"].mean(),
            zoom=2,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=results3,
                get_position='[Longitude, Latitude]',
                get_radius='shop_count * 1000',  
                get_fill_color='[200, 30, 0, 160]',
                pickable=True,
            )
        ],
    )
)

#Results5 - Plotly Map
st.subheader('🚩Number of Starbucks by Location')

# Create scatter_mapbox with clustering and black color
fig = px.scatter_mapbox(
    results3,
    lat="Latitude",
    lon="Longitude",
    #size="shop_count",
    #size_max=30, 
    hover_data={"shop_count": True},
    zoom=1.5,
    height=600,
)

# Use open-source map style
fig.update_layout(mapbox_style="open-street-map")

fig.update_traces(
    cluster=dict(enabled=True),
    marker=dict(color="green")
)

st.plotly_chart(fig)