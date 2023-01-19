# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:38:04 2022

@author: 39333
"""
#import streamlit_authenticator as stauth
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
#import yaml
#from yaml import SafeLoader
var_regex = re.compile(r"^\$*\w+\W")
import os
##################################################################
from pytube import YouTube
import os
from pathlib import Path

def youtube2mp3 (url,outdir):
    
    yt = YouTube(url)

    
    video = yt.streams.filter(abr='128kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        st.write(f'{yt.title} has been successfully downloaded.')
    else:
        st.write(f'ERROR: {yt.title}could not be downloaded!')

youtube2mp3(input("please enter youtube video url:"),(r'C:\Users\39333\Music'))
###################################################################
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
#youtube_stream = st.text_input('link_video_youtube':)
#st.video(st.text_input('link_video_youtube:',))    
#video =st.text_area('video link')
#yt=YouTube(video)
#audio = yt.streams.get_audio_only()
####################################################################################################################################


######################################################################################################################################
files= st.file_uploader('upload Audio File',type=['wav','mp3','m4a'])
if files is None:
    st.error("No file were uploaded")
    st.stop()
#for i in range(len(files)):
bytes_data = files.read()  # read the content of the file in binary
a=files.name
#st.write(files.name)#, bytes_data)
with open(os.path.join("/tmp", files.name), "wb") as f:
    f.write(bytes_data)  # write this content elsewhere
with open(os.path.join("/tmp",a),"rb") as r:
    #st.audio(r, format='audio/wav')
    st.download_button('DOWNLOAD MUSIC_FILE',data=r,file_name=a)

