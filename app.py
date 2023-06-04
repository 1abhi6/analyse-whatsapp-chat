# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:01:33 2023

@author: Abhishek Santosh Gupta
"""

import streamlit as st
from abc import ABC, abstractclassmethod

from preprocessor import Preprocess
from analysis import Analyse, UserList

class Sidebar(ABC):
    def __init__(self):
        
        st.sidebar.title('WhatsApp Chat Analyser')
        
        self.sidebar()
            
    def sidebar(self):
        upload_file = st.sidebar.file_uploader('Choose a text file')
        if upload_file is not None:
            bytes_data = upload_file.getvalue()
            data = bytes_data.decode('utf-8')
            
            preprocessor_obj = Preprocess(data)
            self.df = preprocessor_obj.text_to_df()
            
            self.user_list_obj = UserList(self.df)
            users_list = self.user_list_obj.user_list()
            self.selected_user = st.sidebar.selectbox('Show Analysis',users_list)
            
            self.analysis_obj = Analyse(self.df,self.selected_user)
            
            self.show_analysis_btn()
    
    @abstractclassmethod
    def show_analysis_btn(self):
        pass
    

class Main(Sidebar):
    def __init__(self):
        super().__init__()
    
    def show_analysis_btn(self):
        if st.sidebar.button('Show Analysis'):
            if self.selected_user == 'Overall':  
                st.title('Overall Analysis')
            else:
                st.title("{}'s Analysis".format(self.selected_user))
            self.quick_metric()
    
    def quick_metric(self):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            num_message = self.analysis_obj.num_messages()
            st.metric(label='Total Messages',value=num_message)
            
        with col2:
            total_words = self.analysis_obj.total_words()
            st.metric(label='Total Words',value=total_words)
            
        with col3:
            media_shared = self.analysis_obj.media_shared()
            st.metric(label='Media Shared',value=media_shared)
            
        with col4:
            links_shared = self.analysis_obj.links_shared()
            st.metric(label='Links Shared',value=links_shared)
    

Main()