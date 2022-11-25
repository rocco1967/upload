# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:38:04 2022

@author: 39333
"""
import streamlit as st
from io import StringIO
import pandas as pd
from PIL import Image
#uploaded_files = st.file_uploader("scegli un file csv", 
                                  #accept_multiple_files=False)
option=  st.selectbox('large or normal view?',('LARGE', 'NORMAL'))
st.write('You selected:', option)
selectbox = st.selectbox(
    "How would you like to see ?",
    ("file_csv", "photo"))
if selectbox == 'file_csv':
    uploaded_file = st.file_uploader("Choose a file_csv")
    if uploaded_file is not None:
    # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
        tring_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
if selectbox =='photo':
    uploaded_file = st.file_uploader("Choose a photo")
    #bytes_data = uploaded_file.getvalue()
#if uploaded_file is not None:
    # To read file as bytes:
    if uploaded_file is not None:
        st.image(uploaded_file)
    else:
        st.write('make your choice')
#st.image(uploaded_filcached_image=fil.getvalue()
