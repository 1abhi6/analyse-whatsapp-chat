# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:14:22 2023

@author: Abhishek Santosh Gupta
"""

import emoji
import pandas as pd
from collections import Counter
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

    def word_cloud(self):
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = pd.DataFrame(self.df['message'])

        # Combine all the messages into a single string
        text = ' '.join(df['message'].tolist())

        # Remove '<Media omitted>' from the text
        text = text.replace('<Media omitted>', '')

        return text

    def most_common_words(self):
        f = open('./dependencies/stop_hinglish.txt', 'r')
        stop_words = f.read()

        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        temp = df[df['users'] != 'group_notification']
        temp = temp[temp['message'] != '<Media omitted>\n']
        temp = temp[temp['message'] != '<Media omitted>']

        words = []

        for message in temp['message']:
            for word in message.lower().split():
                if word not in stop_words:
                    words.append(word)

        common_words = pd.DataFrame(Counter(words).most_common(20))
        common_words.rename(columns={
            0: 'Words',
            1: 'Frequency'
        }, inplace=True)

        return common_words

    def most_used_emoji(self):
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]
        
        df = self.df
        

        emojis = []
        for message in df['message']:
            emojis.extend(
                [c for c in message if c in emoji.UNICODE_EMOJI['en']])

        emoji_df = pd.DataFrame(
            Counter(emojis).most_common(len(Counter(emojis))))

        return emoji_df


class GroupSpecificAnalysis(Analyse):
    def most_active_users(self):
        users = self.df['users'].value_counts().sort_values(
            ascending=False
        ).reset_index().head()

        users.rename(columns={
            'index': 'User Name',
            'users': 'Number of Chats'
        }, inplace=True)

        return users

    def most_active_users_percentage(self):
        users = round((self.df['users'].value_counts(
        ) / self.df.shape[0]) * 100, 2).reset_index().rename(
            columns={'index': 'User Name', 'users': 'Chat Percentage'})

        return users
