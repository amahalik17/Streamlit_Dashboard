import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt

#st.title("Rippr Tech, Inc")

dash_options = st.sidebar.selectbox("Choose A Scanner", ("Stock Charts", "Fundamentals"))

#now = st.sidebar.date_input("End date", dt.datetime.now(), key="now")
start_date = st.sidebar.date_input("Start date", dt.date(2020, 1, 1))
end_date = st.sidebar.date_input("End date", dt.datetime.now())

tickers = pd.read_csv("sp500.csv")
symbols = st.sidebar.selectbox("Stock Symbol", tickers)
#ticker = st.sidebar.text_input("Symbol", value="AAPL")

ticker_data = yf.Ticker(symbols)
ticker_df = ticker_data.history(interval='1d', start=start_date, end=end_date)

ticker_df = pd.DataFrame(ticker_df)
ticker_df = ticker_df.drop(columns=['Dividends', 'Stock Splits'])

logo = '<img src=%s>' % ticker_data.info['logo_url']
name = ticker_data.info['longName']
summary = ticker_data.info['longBusinessSummary']
recommend = ticker_data.recommendations
earnings = ticker_data.quarterly_earnings
holders = ticker_data.major_holders

if dash_options == "Stock Charts":

    st.markdown(logo, unsafe_allow_html=True)
    st.header('**%s**' % name)

    st.write("---------------------------")
    st.line_chart(ticker_df['Close'])


elif dash_options == "Fundamentals":

    st.markdown(logo, unsafe_allow_html=True)
    st.header('**%s**' % name)
    st.info(summary)

    st.header('Stock Price Data')
    st.write(ticker_df)
    st.write("---------------------------")
    st.header("Top Analyst Recommendations")
    st.write(recommend)
    st.write("---------------------------")
    st.header("Quarterly Earnings")
    st.write(earnings)
    st.write("---------------------------")
    st.header("Major Share Holders")
    st.write(holders)
    st.write("---------------------------")

else:
    print("Please choose an option.")

    