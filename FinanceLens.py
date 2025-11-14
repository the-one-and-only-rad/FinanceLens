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


    #The code below creates the section Budget Tracking which is designed to track your budget on a base level
    elif section == ("Budget Tracking 💰"):


        #This block of code sets the header and description for the page

        st.header("Budget Tracking:")
        st.write("Track your overall budget by your income, expenses, and savings!")


        #This block of code asks the user for their income and expenses and uses the variables to provide further information to the user

        income = st.number_input("On average, how much would you say your monthly income is? ")
        expenses = st.number_input("On average, how much would you say your monthly expenses are? ")
        balance = (income-expenses)


        #This block of code gives the user information on how to manage their money on a base level

        st.write("After your expenses are deducted from your income, the amount of money you have left is(without taxes into consideration, as it varies by state and income bracket): $", str(balance))
        st.write("Diversifying your savings is very important!")
        fourty = balance*0.4
        sixty = balance*0.6
        profit = ((((((fourty)*1.1)*1.1)*1.1)*1.1)*1.1)-fourty
        st.write("If possible invest 40 percent of your balance, which is $" + str(fourty) + " into investments like the S&P 500 which will give you a return of about 10 percent annually.")
        st.write("This investment after just 5 years will give you a profit of: $" + str(profit))
        st.write("With the remaining 60 percent of your balance, which is $" + str(sixty) + ", put the money in your bank account.")
        st.write("This allows you to build up your savings portfolio as well as gradually increase your return through both your bank as well as the S&P 500.")