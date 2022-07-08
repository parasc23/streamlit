pip install plotly
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

path = r"C:\Users\paras.chauhan\OneDrive - Mars Inc\Desktop\Agrocel\Stripping Plant\New_Model(RPM)\Streamlit_Data.xlsx"

st.set_page_config(page_title="Correlation Chart", page_icon=":bar_chart:", layout="wide")

st.title("**Correlation Chart of S5 and S7 with Efficiency**", anchor=None)
df_s5 = pd.read_excel(path,"S5",parse_dates=['Date'],na_filter=True)
df_s5['Date'] = df_s5['Date'].dt.date
df_s7 = pd.read_excel(path,"S7",parse_dates=['Date'],na_filter=True)
df_s7['Date'] = df_s7['Date'].dt.date

def date_list(list1,list2):
    for i in list2:
        list1.append(i)
    return set(list1)
    
date_set = sorted(date_list(list(df_s5['Date'].unique()),list(df_s7['Date'].unique())))

st.sidebar.header("Date Filter")
Dates = st.sidebar.multiselect(
    "Select the Date:",
    options=date_set,
    default=date_set)

Filtered_S5 = df_s5.query("Date == @Dates")
Filtered_S7 = df_s7.query("Date == @Dates")

correlation_data5 = Filtered_S5.corr()['Efficiency'][:-1]
correlation_data7 = Filtered_S7.corr()['Efficiency'][:-1]

fig = make_subplots(rows=1, cols=2,subplot_titles=("S5", "S7"))

fig.add_trace(
    go.Bar( x = correlation_data5,
    y=correlation_data5.index,orientation='h'),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
    x = correlation_data7,
    y=correlation_data7.index,orientation='h'),
    row=1, col=2
)

fig.update_layout(height=800,width=2000,showlegend=False)
fig.update_annotations(font_size=30)

st.plotly_chart(fig)
