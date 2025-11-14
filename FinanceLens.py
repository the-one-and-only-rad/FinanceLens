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


    #This section provides financial tips for the user

    else:
        st.header("Financial Tips:")
        st.write("Get tips and insights on how to manage and deal with money better!")
        st.write("1. It's always good to diversify your investment portfolio, many people just leave their savings in the bank, but a better way could be by put a percentage of money in the bank while leaving some in other areas such as the S&P 500.")
        st.write("")
        st.write("2. Personal finance isn't hard, but people make it much more harder then they need it to be. Many individuals don't have any way to track their money but there are many tools online in order to do so, this app being an example.")
        st.write("")
        st.write("3. Learning about taxes and other policies early can help you plan future expenses such as college much better, enabling you to excel in managing your personal finances.")
        st.write("")
        st.write("4. Index funds such as the S&P 500 can be a good way to see how the market itself is doing in a particular time frame as it is essentially a compilation of 500 different companies.")
        st.write("")
        st.write("5. Many leading tech giants recommend people to read about the economy through various articles and subjects in order to gain insights on various financial topics to better understand the market and the economy itself.")
        st.write("")
        st.write("6. Using oppurtunities such as compound interest, investments, and etcetera, building long term wealth is just as important as earning money.")
        st.write("")
        st.write("7. Many wealthy people recommend putting most of an individuals money into investments rather then leaving it as cash.")
        st.write("")
        st.write("8. Although many investments do give returns, there is a risk factor in many of them an example being in the stock market and real estate where prices are inconsistent and can change, so other investment options such as the traditional or Roth IRA could be beneficial.")
        st.write("")
        st.write("9. Many factors can affect stock prices and/or real estate prices; for example, if a company was moving its headquarters to a new city, the surrounding areas real estate could increase in price, similarily if a company were to announce a new product, the stock price of the company could go up.")
        st.write("")
        st.write("10. It is helpful to start thinking about retirement(if applicable) even at an early age as it helps plan out finances along the way or establishes a somewhat unpolished but established direction an individual is going towards in their personal finances.")