import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import cufflinks as cl
from yahoofinancials import YahooFinancials


#st.title("Rippr Tech, Inc")

dash_options = st.sidebar.selectbox("Choose A Scanner", ("Stock Charts", "Wallstreetbets", "Pattern Recognition"))
st.header(dash_options)


if dash_options == "Stock Charts":

    #st.subheader("This is the chart page")

    #now = st.sidebar.date_input("End date", dt.datetime.now(), key="now")
    start_date = st.sidebar.date_input("Start date", dt.date(2021, 1, 1))
    end_date = st.sidebar.date_input("End date", dt.datetime.now())

    tickers = pd.read_csv("sp500.csv")
    symbols = st.sidebar.selectbox("Stock Symbol", tickers)
    #ticker = st.sidebar.text_input("Symbol", value="AAPL")

    ticker_data = yf.Ticker(symbols)
    ticker_df = ticker_data.history(interval='1d', start=start_date, end=end_date)
    ticker_df = pd.DataFrame(ticker_df)
    ticker_df = ticker_df.drop(columns=['Dividends', 'Stock Splits'])

    recommend = ticker_data.recommendations

    logo = '<img src=%s>' % ticker_data.info['logo_url']
    name = ticker_data.info['longName']
    summary = ticker_data.info['longBusinessSummary']

    st.markdown(logo, unsafe_allow_html=True)
    st.header('**%s**' % name)
    st.info(summary)

    st.header('Stock Price Data')
    st.write(ticker_df)
    st.write("---------------------------")
    st.write("---------------------------")
    st.write(recommend)


# if dash_options == "Wallstreetbets":
#     st.subheader("This Is The WSB Scanner")