# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:38:27 2023

@author: Abhishek Santosh Gupta
@github: github.com/1abhi6
"""

import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from analysis import Analyse, GroupSpecificAnalysis


class PlotBarChart:
    """Class to plot a bar chart."""

    def __init__(
            self,
            x_axis: pd.Series,
            y_axis: pd.Series,
            layout_title,
            layout_x_axis: str,
            layout_yaxis: str,
            orientation: str) -> None:
        """
        Initialize the PlotHorizontalBarChart class.

        Args:
            x_axis (pd.Series): The x-axis data.
            y_axis (pd.Series): The y-axis data.
            layout_title: The title of the chart.
            layout_x_axis: The label for the x-axis.
            layout_yaxis: The label for the y-axis.
        """

        # Define a color palette for the bars
        colors = ['rgba(0, 255, 255, 0.6)', 'rgba(0, 0, 255, 0.6)',
                  'rgba(255, 165, 0, 0.6)', 'rgba(128, 0, 128, 0.6)', 'rgba(0, 128, 0, 0.6)',
                  'rgba(255, 255, 0, 0.6)', 'rgba(255, 0, 255, 0.6)', 'rgba(0, 128, 128, 0.6)',
                  'rgba(128, 128, 0, 0.6)', 'rgba(0, 0, 128, 0.6)', 'rgba(128, 0, 0, 0.6)',
                  'rgba(0, 255, 0, 0.6)', 'rgba(0, 0, 128, 0.6)', 'rgba(255, 0, 0, 0.6)',
                  'rgba(255, 255, 255, 0.6)', 'rgba(128, 128, 128, 0.6)', 'rgba(128, 0, 128, 0.6)',
                  'rgba(255, 255, 0, 0.6)', 'rgba(0, 255, 255, 0.6)', 'rgba(255, 0, 255, 0.6)',
                  'rgba(0, 255, 255, 0.9)', 'rgba(0, 0, 255, 0.9)', 'rgba(255, 0, 0, 0.9)',
                  'rgba(255, 165, 0, 0.6)', 'rgba(128, 0, 128, 0.6)', 'rgba(0, 128, 0, 0.8)',
                  'rgba(255, 255, 0, 0.9)', 'rgba(255, 0, 255, 0.9)', 'rgba(0, 128, 128, 0.9)',]

        fig = go.Figure(data=go.Bar(
            x=x_axis,
            y=y_axis,
            orientation=orientation,
            marker=dict(color=colors)
        ))

        fig.update_layout(
            title=layout_title,
            xaxis=dict(title=layout_x_axis),
            yaxis=dict(title=layout_yaxis)
        )

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
        PlotBarChart(
            x_axis=most_used_emojis['Frequency'],
            y_axis=most_used_emojis['Emojis'],
            layout_title='Most Used Emojis',
            layout_x_axis='Frequency',
            layout_yaxis='Emojis',
            orientation='h'
        )
