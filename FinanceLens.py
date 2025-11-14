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