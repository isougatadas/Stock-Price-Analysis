import yfinance as yf
import streamlit as st

st.write("""
# Stock Price Analysis
Shown are the stock closing ***price*** and ***volume***
""")

option = st.selectbox('Which stock price and volume you want to see?',
('GOOGL', 'AAPL', 'MSFT','AMZN','FB', 'TSLA', 'JPM', 'NVDA', 'UNH', 'JNJ', 'BAC', 'PG', 'MA', 'ADBE', 'PFE', 'DIS'))
st.write('You selected:', option)

tickerSymbol = option
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2001-1-31', end='2021-11-30')

st.write("""##### Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""##### Traded Volume""")
st.line_chart(tickerDf.Volume)