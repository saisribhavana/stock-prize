import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

section = st.sidebar.radio("Select Section", ["Prediction", "Graphs", "Information", "About"])

model = joblib.load('random_forest_regressor_model.pkl')

stock_data = """Apple Inc. Stock Overview

Apple Inc. (AAPL) is a technology giant that needs no introduction. Founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976, Apple has become one of the most valuable and iconic companies globally. As of my knowledge cutoff in 2022, Apple is headquartered in Cupertino, California.

Market Performance:

Apple's stock (AAPL) has been a consistent performer in the stock market. It is listed on the NASDAQ stock exchange and is a component of major indices like the S&P 500 and the Dow Jones Industrial Average. Over the years, Apple's market capitalization has reached unprecedented levels, making it one of the largest publicly traded companies.

Product Innovations Impact:

The stock's performance is intricately linked to Apple's product launches and innovations. Major product releases, such as the iPhone, iPad, Mac, and more recently, wearables like the Apple Watch, have had a significant impact on the company's revenue and, consequently, its stock value.

Financial Health:

Apple's financial health is robust, often boasting substantial revenue and profits. The company has a history of smart financial management and a loyal customer base, contributing to its overall stability.

Dividends and Share Buybacks:

In addition to stock value appreciation, Apple has returned value to its shareholders through dividends and share buyback programs. This strategy is indicative of the company's confidence in its financial position and its commitment to providing value to its investors.

Market Influence:

As one of the largest technology companies globally, Apple's stock performance can also be influenced by broader market trends, global economic conditions, and shifts in consumer sentiment toward technology companies."""


team_details = """
##
We have done this project under the guidence of Ms.Baishalini Sahu (AI Scientist) from INTRAINTECH.

Our team members are
-   G Chaitanya
-   M Hemanth Kumar Yadav
-   Sai Sri Bhavna
-   Jyothirmayee
-   Sai Siva Krishna
"""

if section == "Prediction":
    st.header("Prediction")
    date = st.date_input('Date', value=None)
    open_price = st.number_input('Open Price', value=0.0)
    high_price = st.number_input('High Price', value=0.0)
    low_price = st.number_input('Low Price', value=0.0)
    adj_close = st.number_input('Adj Close', value=0.0)
    volume = st.number_input('Volume', value=0.0)
    if st.button('Predict'):
        user_input = pd.DataFrame({
            'Date': [date],
            'Open': [open_price],
            'High': [high_price],
            'Low': [low_price],
            'Adj Close': [adj_close],
            'Volume': [volume],
        })
        user_input['Date'] = user_input['Date'].astype(str)
        user_input['Date'] = user_input['Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').timestamp())
        prediction = model.predict(user_input)
        st.subheader('Predicted Close Price')
        st.write(prediction[0])

elif section == "Graphs":
    st.header("Graphs")
    st.image('Open.png', caption='Open price over Time', use_column_width=True)
    st.image('AvgOpenClose.png', caption='Avg.Open and Avg.Close price over Time', use_column_width=True)
    st.image('HighLow.png', caption='High and Low over Time', use_column_width=True)
    st.image('AvgHighLow.png', caption='Avg.High and Avg.Low over Time', use_column_width=True)
    st.image('CloseAdj.png', caption='Close and Adj Close over Time', use_column_width=True)
    st.image('Corr.png', caption='Correlation graph', use_column_width=True)
    st.image('Accuracy graph.png', caption='Accuracy Graph', use_column_width=True)

elif section == "Information":
    st.header("Information")
    st.markdown(stock_data)

elif section == "About":
    st.header("About Us")
    st.markdown(team_details)

