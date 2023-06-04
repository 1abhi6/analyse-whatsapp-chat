# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:14:22 2023

@author: Abhishek
"""
import pandas as pd

class UserList:
    def __init__(self, df):
        self.df = df
    
    # Fetch user list from the dataframe
    def user_list(self):
        user_list = self.df['users'].unique().tolist()
        user_list.remove('Group Notification')
        user_list.insert(0,'Overall')
        
        return user_list

class Analyse(UserList):
    def __init__(self,df,selected_user):
        self.selected_user = selected_user
        super().__init__(df)
        if self.selected_user != 'Overall':
            self.df = self.df[self.df['users'] == self.selected_user]
        
    # Quick metrics
    def num_messages(self):
        return self.df.shape[0]
    
    def total_words(self):
        words = []
        for message in self.df['message']:
            words.extend(message.split())
        return len(words)
    
    
