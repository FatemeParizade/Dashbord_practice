import streamlit as st 
import pandas as pd
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

login_option = st.sidebar.radio('LogIn/SignUp', ('LogIn', 'SignUp'))
if login_option == 'LogIn':
    with st.sidebar.form("LogIn"):
        st.write("LogIn Here.")
        suername = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("LogIn")
        if submitted:
            pass

else:
    with st.sidebar.form("SignUp"):
            st.write("SIgnUP Here.")
            suername = st.text_input("Username")
            password = st.text_input("Password", type="password")
            email = st.text_input("Email")

            submitted = st.form_submit_button("SignUp")
            if submitted:
                pass


banner = Image.open('./data/banner.jfif')
st.image(banner)
st.title(':zap: Movie Time')


col1, col2, col3 = st.columns(3)
col1.metric(label="Ticket Price", value="16$")
col2.metric(label="Showtime", value="3h")
col3.metric(label="Rating", value="4.5", delta="1")

with st.expander('More Information'):
     col1, col2 = st.columns(2)
     col1.text_input('Film:')
     col2.text_input('Cinema:')
    
