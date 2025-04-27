import streamlit as st

def intro():
    import streamlit as st
    import duckdb as db
    import pandas as pd
    st.write("# Welcome to Streamlit! 👋")
    #st.sidebar.success("Select a demo above.")

    df = pd.read_csv("Starbucks.csv")
    st.write(df)

def ownership_demo():
    import streamlit as st
    import duckdb as db
    import pandas as pd
    import pydeck as pdk
    import plotly.express as px

    st.write("# Welcome to Streamlit! 👋")

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

def top10_demo():
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

def map_demo():
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

page_names_to_funcs = {
    #"my_intro": intro,
    #"Plotting Demo": plotting_demo,
    #"Mapping Demo": mapping_demo,
    #"DataFrame Demo": data_frame_demo,
    #"my_page2": intro2,
    "Ownership" : ownership_demo,
    "👑Top 10 Country" : top10_demo,
    "🌏Mapping" : map_demo
}

st.sidebar.write("my sidebar")
demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()