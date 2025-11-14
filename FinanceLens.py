import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

if "app_started" not in st.session_state:
    st.session_state.app_started = False


# Lines 10-21 were made by the AI tool ChatGPT to generate a starting screen with a button to enter the application

if not st.session_state.app_started:
    st.markdown("<h1 style='text-align: center;'>💵 Welcome to FinanceLens 💵</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Click below to start exploring your finances!</p>", unsafe_allow_html=True)

    start = st.button("Start FinanceLens")
    
    if start:
        st.session_state.app_started = True
        st.rerun()  


# Once the user clicks the button the main app shows

if st.session_state.app_started:

    st.set_page_config(page_title="FinanceLens", page_icon="💵", layout="wide")


    #This sets the title of the page

    st.title("💵 FinanceLens - An Outlook on Your Finances")


    #This creates a sidebar with categories

    st.sidebar.header("Tools:")
    section = st.sidebar.radio("Options:", ["Stock Insights 📈", "Budget Tracking 💰", "Financial Tips 💡"])


    #The code below creates the section Stock Insights which is designed to give simple insights on select stocks and risk analysis

    if section == "Stock Insights 📈":


        #Adds a header to the category

        st.header("Stock Insights:")
        st.write("Get simple insights on the performance and risk analysis of stocks over the past 10 days!")


        #Asks the user for a stock symbol to retrieve and give data on the stock.

        Stock = st.text_input("Please enter a stock symbol: ").upper()
        if Stock:
            data = yf.Ticker(Stock)
            hist = data.history(period = "10d")
            st.subheader("Closing Prices of the last 10 days:")
            st.dataframe(hist[['Close']])


            #The code from lines 64 to 68 was coded with the help of the AI tool ChatGPT

            latest = hist['Close'][-1]
            previous = hist['Close'][0]
            change_percent = (latest-previous)/previous*100
            st.write(f"The stock changed **{change_percent:.2f}%** in the last 10 days.")
            st.line_chart(hist['Close'])


