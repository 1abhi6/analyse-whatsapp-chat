# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:12:13 2023

@author: Abhishek Santosh Gupta
@github: github.com/1abhi6
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class SubHeader:
    def __init__(self, subheader: str, tooltip: str) -> None:
        st.subheader(subheader, help=tooltip)


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
                  'rgba(255, 250, 165, 1)', 'rgba(128, 128, 128, 0.6)', 'rgba(128, 0, 128, 0.6)',
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


class PlotLineChart:
    """Class to plot a line chart."""

    def __init__(self, temp_df: pd.DataFrame(), x_axis: str, y_axis: str, layout_title: str) -> None:
        """
        Initialize the PlotLineChart class.

        Args:
            temp_df (str): The dataframe containing the chart data.
            x_axis (str): The column name for the x-axis.
            y_axis (str): The column name for the y-axis.
            layout_title (str): The title of the chart.
        """
        fig = px.line(
            temp_df,
            x=x_axis,
            y=y_axis,
            title=layout_title
        )

        st.plotly_chart(fig, use_container_width=True)
