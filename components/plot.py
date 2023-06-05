# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:38:27 2023

@author: Abhishek Gupta
"""

import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

from analysis import Analyse,GroupSpecificAnalysis


class PlotBarChart:
    def __init__(self, df, x_axis, y_axis):
        fig = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)


class Plot:
    def __init__(self, df, selected_user):
        self.df = df
        self.selected_user = selected_user
        self.group_specific_analysis = GroupSpecificAnalysis(
            self.df, self.selected_user)
        self.analyse = Analyse(self.df, self.selected_user)

    def plot_most_active_users(self):
        users = self.group_specific_analysis.most_active_users()
        PlotBarChart(df=users, x_axis='User Name', y_axis='Number of Chats')
    
    def plot_word_cloud(self):
        text = self.analyse.word_cloud()
        # Create a WordCloud object and generate the word cloud
        wordcloud = WordCloud(background_color='white', colormap='tab20c').generate(text)
        
        # Set the height and width of the plot
        plt.figure(figsize=(40, 20))
        
        # Display the word cloud using matplotlib
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        
        st.pyplot(plt)
        
    

