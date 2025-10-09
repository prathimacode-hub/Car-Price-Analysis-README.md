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

    st.subheader('PROBLEM STATEMENT')
    
    st.markdown('', 
         unsafe_allow_html=True)

    
elif add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Project Goals</h4>', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    
    st.markdown('<h4>Developments Made</h4>', unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)
    st.markdown('•  &nbsp; ',unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)
    st.markdown('• ',unsafe_allow_html=True)


elif add_selectbox == 'Features':

    st.subheader('PROJECT ENDORSEMENTS')

    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)

elif add_selectbox == 'Car Price by Date':

    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)

elif add_selectbox == 'Car Price by Monthly':

    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)

elif add_selectbox == 'Visualizations':
    
    st.subheader('PROJECT VISUALIZATIONS')
    st.markdown('<h4>Title1</h4>', unsafe_allow_html=True)
    st.image(".png", width=400)
    st.markdown('<h4>Title2</h4>', unsafe_allow_html=True)
    st.image(".png", width=400)
    st.markdown('<h4>Title3</h4>', unsafe_allow_html=True)
    st.image(".png", width=400)
    st.markdown('<h4>Title4</h4>', unsafe_allow_html=True)
    st.image(".png", width=500)
   
    
else add_selectbox == 'Conclusion':

    st.subheader('TECH STACK')

    st.markdown('• Data Collection - Google Earth Datasets', unsafe_allow_html=True)
    st.markdown('• Data Visualization - Google Earth Engine', unsafe_allow_html=True)
    st.markdown('• Satellite Imagery Analysis - Google Earth Engine', unsafe_allow_html=True) 
    st.markdown('• Machine Learning - Python, Jupyter Notebooks, Random Forest', unsafe_allow_html=True) 
    st.markdown('• Dashboard - Streamlit, Heroku', unsafe_allow_html=True) 

    st.subheader('PROJECT SUMMARY')

    st.markdown('', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    
    st.subheader('CONCLUSION')

    st.markdown('', unsafe_allow_html=True) 

    
