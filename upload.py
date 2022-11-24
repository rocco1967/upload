# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:38:04 2022

@author: 39333
"""
import streamlit as st
from io import StringIO
import pandas as pd
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
    
    from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

...

if choice == "Image":
		st.subheader("Image")
		image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

		if image_file is not None:

			  # To See details
			  file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
			  st.write(file_details)

              # To View Uploaded Image
			  st.image(load_image(image_file),width=250)

    
     
           
