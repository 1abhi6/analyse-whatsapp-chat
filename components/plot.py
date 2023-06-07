# -*- coding: utf-8 -*-
"""
WhatsApp Chat Analyzer - Plotting Functions

This module contains classes and functions for plotting various analyses of WhatsApp chat data in a Streamlit app.

Author: Abhishek Santosh Gupta
GitHub: github.com/1abhi6
"""

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

from .utils import SubHeader, PlotBarChart, PlotLineChart
from analysis import Analyse, GroupSpecificAnalysis


class Plot:
    """
    Class for generating plots of WhatsApp chat analysis results.
    """

    def __init__(self, df, selected_user):
        """
        Initialize the Plot class.

        Args:
            df (pandas.DataFrame): The chat data as a DataFrame.
            selected_user (str): The selected user for analysis.
        """
        self.df = df
        self.selected_user = selected_user
        self.group_specific_analysis = GroupSpecificAnalysis(self.df, self.selected_user)
        self.analyse = Analyse(self.df, self.selected_user)

    def plot_daily_timeline(self):
        """
        Plot the chat timeline on a daily basis.
        """
        daily_timeline = self.analyse.daily_timeline()

        SubHeader(
            subheader='Chat Timeline Datewise',
            tooltip='Chat timeline over the date.'
        )

        PlotLineChart(
            temp_df=daily_timeline,
            x_axis='Time (Date)',
            y_axis='Number of Messages',
            layout_title='Conversation History'
        )

    def plot_timeline(self):
        """
        Plot the chat timeline on a monthly basis.
        """
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
        """
        Plot the bar chart of the most active users.
        """
        users = self.group_specific_analysis.most_active_users()

        PlotBarChart(
            x_axis=users['User Name'],
            y_axis=users['Number of Chats'],
            layout_title='Most Active Users',
            layout_x_axis='User Name',
            layout_y_axis='Number of Chats',
            orientation='v'
        )

    def plot_word_cloud(self):
        """
        Generate and plot the word cloud of frequently used words.
        """
        text = self.analyse.word_cloud()

        SubHeader(
            subheader='Frequently Used Words',
            tooltip='Word cloud of frequently used words.'
        )

        wordcloud = WordCloud(background_color='white', colormap='tab20c',
                              max_font_size=50, max_words=100).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        st.pyplot(plt)

    def plot_most_common_words(self):
        """
        Plot the bar chart of the most common words in the chat.
        """
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
            layout_y_axis='Words',
            orientation='h'
        )

    def plot_most_used_emoji(self):
        """
        Plot the bar chart of the most used emojis in the chat.
        """
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
            layout_y_axis='Emojis',
            orientation='h'
        )

    def plot_most_active_day_of_week(self):
        """
        Plot the bar chart of the most active day of the week.
        """
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
            layout_y_axis='Number of Messages',
            orientation='v'
        )

    def plot_most_active_month(self):
        """
        Plot the bar chart of the most active month of the year.
        """
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
            layout_y_axis='Number of Messages',
            orientation='v'
        )

    def plot_activity_heatmap(self):
        """
        Plot the heatmap of activity hours of users on different days of the week.
        """
        pivot_table = self.analyse.activity_heatmap()

        SubHeader(
            subheader='Most Active Hour wrt Day',
            tooltip='This heatmap shows at which hour of which day users are active.'
        )

        fig, ax = plt.subplots(figsize=(20, 10))
        sns.heatmap(pivot_table, ax=ax)
        ax.set_xlabel('Hour')
        ax.set_ylabel('Day of the Week')

        st.pyplot(fig)
