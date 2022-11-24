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

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    st.line_chart(dataframe['charges'])
def main():
  file1=st.file_uploader('upload file'):
    show_file1=st.empty()
    if not file1:
      show_file1.info('please upload a file)
      return
    content=file1.getvalue()
    if instance(file1,BytesIO):
       show_file1.image(file1)
    else:
        df=pd.read_csv(file1)
        st.dataframe(df)
    file.close()
main()                     
  

     
           
