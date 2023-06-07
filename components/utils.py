# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:12:13 2023

@author: Abhishek Santosh Gupta
@github: github.com/1abhi6
"""

import streamlit as st


class SubHeader:
    def __init__(self, subheader: str, tooltip: str) -> None:
        st.subheader(subheader, help=tooltip)
