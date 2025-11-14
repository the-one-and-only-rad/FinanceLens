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