# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:14:22 2023

@author: Abhishek
"""
import pandas as pd

class Analyse:
    def __init__(self, df):
        self.df = df
    
    # Fetch user list from the dataframe
    def user_list(self):
        user_list = self.df['users'].unique().tolist()
        user_list.remove('Group Notification')
        user_list.insert(0,'Overall')
        
        return user_list