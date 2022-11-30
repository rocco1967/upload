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
############################################################################
#youtube_streams='https://www.youtube.com/watch?v=qod03PVTLqk'
#fp = tempfile.TemporaryFile()
#a=st.text_input('Insert YouTube ')

#st.video(a)

import urllib.request as urllib2

link = st.text_input('Insert YouTube ')
file_name = 'trial_video.mp4' 

rsp = urllib2.urlopen(link)
with open(file_name,'wb') as f:
     a=f.write(rsp.read())
     binary = b'a'
     st.download_button('press',data=binary)    
    
##########################################################################
import urllib.request #as urllib2
url = st.text_input("Enter the Youtube")
#name = st.text_input("Enter the name for the video")
#name=name
try:
    st.write("Downloading starts...\n")
    urllib.request.urlretrieve(url) 
    st.write("Download completed..!!")
except Exception as e:
    st.write(e)
##################################################################################    
youtube_streams=st.text_input('Insert YouTube Link')#
var_regex = re.compile(r"^\$*\w+\W")
if youtube_streams is not None:
    
    yt=YouTube(youtube_streams)#.streams.first().download()
    #st.write(yt.streams.filter(only_audio=True))
    try:
           
    #time.sleep(2)
        #audio= yt.streams.get_by_itag(140)#yt.streams.filter(only_audio = True)
        audio=yt.streams.get_audio_only()
    except pytube.exceptions.RegexMatchError:
        st.write('Video is unavaialable, skipping.') 
    except pytube.exceptions.VideoUnavailable:
        st.write('Video is unavaialable, skipping.') 
    else:    
        audio=audio.download()
    #audio=BytesIO(audio)
        audio_file=open(audio,'rb')
        audio_bytes = audio_file.read()
        st.download_button('download_file',data=audio_bytes)
        st.audio(audio_bytes, format='audio/ogg')
        st.write(audio)

