# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:38:27 2023

@author: Abhishek Gupta
"""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from analysis import GroupSpecificAnalysis


class PlotBarChart:
    def __init__(self, df, x_axis, y_axis):
        fig = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)


class GroupPlot:
    def __init__(self, df, selected_user):
        self.df = df
        self.selected_user = selected_user
        self.group_specific_analysis = GroupSpecificAnalysis(
            self.df, self.selected_user)

    def plot_most_active_users(self):
        users = self.group_specific_analysis.most_active_users()
        PlotBarChart(df=users, x_axis='Users', y_axis='Number of Chats')