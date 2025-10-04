import datetime
import streamlit as st
import streamlit.components.v1 as components
import numpy
import pandas
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Car Price Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Car Price Analysis Dashboard </h1>',
                    unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("Home", "About", "Features", "Car Price by Date", "Car Price by Monthly", "Visualizations", "Conclusion")
)

if add_selectbox == 'Home':
    
    LOGO_IMAGE = ".png"
    
    st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .logo-text {
             font-weight:700 !important;
             font-size:50px !important;
             color: #f9a01b !important;
             padding-top: 75px !important;
        }
        .logo-img {
             float:right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
