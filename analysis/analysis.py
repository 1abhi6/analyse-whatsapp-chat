# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:14:22 2023

@author: Abhishek Santosh Gupta
"""
import pandas as pd

from urlextract import URLExtract

class UserList:
    def __init__(self, df):
        self.df = df

    # Fetch user list from the dataframe
    def user_list(self):
        user_list = self.df['users'].unique().tolist()
        user_list.remove('Group Notification')
        user_list.insert(0, 'Overall')

        return user_list


class Analyse(UserList):
    def __init__(self, df, selected_user):
        self.selected_user = selected_user
        super().__init__(df)
        if self.selected_user != 'Overall':
            self.df = self.df[self.df['users'] == self.selected_user]
        self.extract_url = URLExtract()

    # Quick metrics
    def num_messages(self):
        return self.df.shape[0]

    def total_words(self):
        words = []
        for message in self.df['message']:
            words.extend(message.split())
        return len(words)

    def media_shared(self):
        return (self.df[
            (self.df['message'] == '<Media omitted>') |
            (self.df['message'] == '<Media omitted\n>')
        ].shape[0])
    
    def links_shared(self):
        links = []
        for message in self.df['message']:
            links.extend(self.extract_url.find_urls(message))
        
        return len(links)