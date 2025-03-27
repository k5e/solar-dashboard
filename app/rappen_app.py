import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import datetime as dt

st.set_page_config(
    page_title="Solar-Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

df_reshaped = pd.read_csv('./app/data/solar.csv')

with st.sidebar:
    st.title('☀️ Solar-Dashboard')
    
    day_list = list(df_reshaped.DATE.unique())[::-1]
    day_list.sort()
     
    selected_day = st.selectbox('Tag auswählen', day_list, index=len(day_list)-1)
    day_index = day_list.index(selected_day)
    if day_index > len(day_list)-7:
        day_index = len(day_list)-7
        
    selected_days = list()
    
    for d in range(0, 7):
        selected_days.append(day_list[day_index+d]) 
    
    df_selected_days = df_reshaped[df_reshaped.DATE.isin(selected_days)]

    color_theme_list = ['magma', 'plasma', 'blues', 'cividis', 'greens', 'inferno', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Farben auswählen', color_theme_list)

def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Datum", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap


col = st.columns((1), gap='medium')

with col[0]:
    st.markdown('## Energieertrag')
       
    heatmap = make_heatmap(df_selected_days, 'DATE', 'TIME', 'AC_POWER', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)
    
   # st.subheader('Raw data')
   # st.write(selected_days)
