# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:38:27 2023

@author: Abhishek Santosh Gupta
@github: github.com/1abhi6
"""

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from .utils import (
    SubHeader,
    PlotBarChart,
    PlotLineChart
)
from analysis import (
    Analyse,
    GroupSpecificAnalysis
)


class Plot:
    def __init__(self, df, selected_user):
        self.df = df
        self.selected_user = selected_user
        self.group_specific_analysis = GroupSpecificAnalysis(
            self.df, self.selected_user)
        self.analyse = Analyse(self.df, self.selected_user)
    
    def plot_daily_timeline(self):
        daily_timeline = self.analyse.daily_timeline()

        SubHeader(
            subheader='Chat Timeline Datewise ',
            tooltip='Chat timeline over the date.'
        )

        PlotLineChart(
            temp_df=daily_timeline,
            x_axis='Time (Date)',
            y_axis='Number of Messages',
            layout_title='Conversation History'
        )

    def plot_timeline(self):
        timeline = self.analyse.timeline()

        SubHeader(
            subheader='Chat Timeline Month-Year Wise',
            tooltip='Chat timeline over the Month-Year.'
        )

        PlotLineChart(
            temp_df=timeline,
            x_axis='Time (Month-Year)',
            y_axis='Number of Messages',
            layout_title='Conversation History'
        )
        

    def plot_most_active_users(self):
        users = self.group_specific_analysis.most_active_users()

        PlotBarChart(
            x_axis=users['User Name'],
            y_axis=users['Number of Chats'],
            layout_title='Most Active Users',
            layout_x_axis='User Name',
            layout_yaxis='Number of Chats',
            orientation='v'
        )

    def plot_word_cloud(self):
        text = self.analyse.word_cloud()

        SubHeader(
            subheader='Frequently Used Words',
            tooltip='Wrod cloud of frequently used words.'
        )

        # Create a WordCloud object and generate the word cloud
        wordcloud = WordCloud(background_color='white', colormap='tab20c',
                              max_font_size=50, max_words=100).generate(text)

        # Set the height and width of the plot
        # Adjust the figure size as per your preference
        plt.figure(figsize=(10, 5))

        # Display the word cloud using matplotlib
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        st.pyplot(plt)

    def plot_most_common_words(self):
        common_words = self.analyse.most_common_words()

        SubHeader(
            subheader='Most Used Words during Chat',
            tooltip='Bar chart of frequently used words in chat.'
        )

        PlotBarChart(
            x_axis=common_words['Frequency'],
            y_axis=common_words['Words'],
            layout_title='Most Common Words',
            layout_x_axis='Frequency',
            layout_yaxis='Words',
            orientation='h'
        )

    def plot_most_used_emoji(self):
        most_used_emojis = self.analyse.most_used_emojis()

        SubHeader(
            subheader='Most Used Emojis during Chat',
            tooltip='Bar chart of frequently used emojis in chat.'
        )

        PlotBarChart(
            x_axis=most_used_emojis['Frequency'],
            y_axis=most_used_emojis['Emojis'],
            layout_title='Most Used Emojis',
            layout_x_axis='Frequency',
            layout_yaxis='Emojis',
            orientation='h'
        )
        
    def plot_most_active_day_of_week(self):
        most_active_day_of_week = self.analyse.most_active_day_of_week()
        
        SubHeader(
            subheader='Most Active Day',
            tooltip='Bar chart of most active day of the week.'
        )
        
        PlotBarChart(
            x_axis=most_active_day_of_week['Day of the Week'],
            y_axis=most_active_day_of_week['Number of Messages'],
            layout_title='Most Active Day Of The Week',
            layout_x_axis='Day of the Week',
            layout_yaxis='Number of Messages',
            orientation='v'
        )
        

    def plot_most_active_month(self):
        most_active_month = self.analyse.most_active_month()
        
        SubHeader(
            subheader='Most Active Month',
            tooltip='Bar chart of most active month of the year.'
        )
        
        PlotBarChart(
            x_axis=most_active_month['Month'],
            y_axis=most_active_month['Number of Messages'],
            layout_title='Most Active Month Of The Year',
            layout_x_axis='Month Name',
            layout_yaxis='Number of Messages',
            orientation='v'
        )
