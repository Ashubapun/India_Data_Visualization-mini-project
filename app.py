import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India_census.csv')
#print(df)
pd.set_option('display.max_columns', 1000)
df['State'].replace('Orissa','Odisha', inplace = True)
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

cols = ['Population','Male', 'Female', 'Literate', 'Male_Literate', 'Female_Literate',
       'Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains',
       'Households_with_Internet']
#print(cols)
st.sidebar.title('India Data Vizualization')

selected_state = st.sidebar.selectbox("Select a State", list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', sorted(cols))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(cols))

plot = st.sidebar.button('Plot Graph')

st.title(f"Map of {selected_state}")

if plot:
    st.text('Primary parameter represents Size')
    st.text('Secondary parameter represents Color')
    if selected_state == 'Overall India':
        # plot for India
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size = primary, color = secondary, size_max =30,
                                zoom=3, mapbox_style='carto-positron',
                                width = 1200, height = 700, hover_name= 'District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for State

        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=30, zoom=6,
                                mapbox_style='carto-positron',
                                width=1200, height=700, hover_name= 'District')
        st.plotly_chart(fig, use_container_width=True)
