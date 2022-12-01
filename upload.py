# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:38:04 2022

@author: 39333
"""

import streamlit as st
import time
from io import StringIO,BytesIO
import pandas as pd
from PIL import Image
from pytube import YouTube
import pytube
from typing import Pattern, Union
import regex
import tempfile
import re
var_regex = re.compile(r"^\$*\w+\W")
#st.write(pytube.__version__)
#uploaded_files = st.file_uploader("scegli un file csv", 
                                  #accept_multiple_files=False)
select =  st.selectbox("large or normal view?",("LARGE", "NORMAL"))
#LARGE=st.set_page_config(layout=select)
#NORMAL=st.set_page_config(layout=select)
#if selectbox == 'LARGE':
#
#   LARGE=st.set_page_config(layout="wide")
#else:
#    NORMAL=st.set_page_config(layout="centered")
#st.write('You selected:', option)
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
        string_data = stringio.read()
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
###############################################################################################################################
rom PyPDF2 import PdfReader   #######     PDF
import base64
import tempfile
import streamlit as st
from pdf2image import convert_from_path
from pathlib import Path

def show_pdf(file_path:str):
    """Show the PDF in Streamlit
    That returns as html component

    Parameters
    ----------
    file_path : [str]
        Uploaded PDF file path
    """

    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)


def main():
    """Streamlit application
    """

    st.title("PDF file uplodaer")
    uploaded_file = st.file_uploader("Choose your .pdf file", type="pdf")

    if uploaded_file is not None:
        # Make temp file path from uploaded file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            st.markdown("## Original PDF file")
            fp = Path(tmp_file.name)
            fp.write_bytes(uploaded_file.getvalue())
            st.write(show_pdf(tmp_file.name))

            imgs = convert_from_path(tmp_file.name)

            st.markdown(f"Converted images from PDF")
            st.image(imgs)


if __name__ == "__main__":
    main()
