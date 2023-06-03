# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:01:33 2023

@author: Abhishek
"""

import streamlit as st

from preprocessor import Preprocess
from analysis import Analyse

class Main:
    def __init__(self):
        
        st.sidebar.title('WhatsApp Chat Analyser')
        
        upload_file = st.sidebar.file_uploader('Choose a file')
        if upload_file is not None:
            bytes_data = upload_file.getvalue()
            data = bytes_data.decode('utf-8')
            
            preprocessor_obj = Preprocess(data)
            self.df = preprocessor_obj.text_to_df()
            
            analysis_obj = Analyse(self.df)
            users_list = analysis_obj.user_list() 
            st.sidebar.selectbox('Show Analysis',users_list)


Main()

