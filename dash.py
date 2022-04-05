import streamlit as st
import pandas as pd
import numpy as np
import sqlite3


st.title("Rippr Tech, Inc")


dash_options = st.sidebar.selectbox("Choose A Scanner", ("Stock Charts", "Wallstreetbets", "Pattern Recognition"))
st.header(dash_options)

if dash_options == "Stock Charts":
    st.subheader("This is the chart page")
    ticker = st.sidebar.text_input("Symbol", value="AAPL")

if dash_options == "Wallstreetbets":
    st.subheader("This Is The WSB Scanner")