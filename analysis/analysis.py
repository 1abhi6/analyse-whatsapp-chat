# -*- coding: utf-8 -*-
"""
WhatsApp Chat Analyzer - Analysis Functions

This module contains classes and functions for analyzing WhatsApp chat data in a Streamlit app.

Author: Abhishek Santosh Gupta
GitHub: github.com/1abhi6
"""

import emoji
import pandas as pd
from collections import Counter
from urlextract import URLExtract
import streamlit as st
from functools import wraps


def filter_selected_user(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.selected_user != 'Overall':
            self.df = self.df[self.df['users'] == self.selected_user]
        return func(self, *args, **kwargs)
    return wrapper


class UserList:
    """
    Class for generating the list of users in the chat data.
    """

    def __init__(self, df):
        """
        Initialize the UserList class.

        Args:
            df (pandas.DataFrame): The chat data as a DataFrame.
        """
        self.df = df

    def user_list(self):
        """
        Fetch the list of users from the dataframe.

        Returns:
            list: List of users.
        """
        user_list = self.df['users'].unique().tolist()
        user_list.remove('Group Notification')
        user_list.insert(0, 'Overall')

        return user_list


class Analyse(UserList):
    """
    Class for performing various analyses on the WhatsApp chat data.
    """

    def __init__(self, df, selected_user):
        """
        Initialize the Analyse class.

        Args:
            df (pandas.DataFrame): The chat data as a DataFrame.
            selected_user (str): The selected user for analysis.
        """
        self.selected_user = selected_user
        super().__init__(df)
        if self.selected_user != 'Overall':
            self.df = self.df[self.df['users'] == self.selected_user]
        self.extract_url = URLExtract()

    def num_messages(self):
        """
        Calculate the total number of messages.

        Returns:
            int: Total number of messages.
        """
        return self.df.shape[0]

    def total_words(self):
        """
        Calculate the total number of words.

        Returns:
            int: Total number of words.
        """
        words = []
        for message in self.df['message']:
            words.extend(message.split())
        return len(words)

    def media_shared(self):
        """
        Count the number of media shared.

        Returns:
            int: Number of media shared.
        """
        return (self.df[
            (self.df['message'] == '<Media omitted>') |
            (self.df['message'] == '<Media omitted\n>')
        ].shape[0])

    def links_shared(self):
        """
        Count the number of links shared.

        Returns:
            int: Number of links shared.
        """
        links = []
        for message in self.df['message']:
            links.extend(self.extract_url.find_urls(message))

        return len(links)

    def word_cloud(self):
        """
        Generate the word cloud of frequently used words.

        Returns:
            str: Text containing all the words.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = pd.DataFrame(self.df['message'])

        # Combine all the messages into a single string
        text = ' '.join(df['message'].tolist())

        # Remove '<Media omitted>' from the text
        text = text.replace('<Media omitted>', '')

        return text

    def most_common_words(self):
        """
        Find the most common words in the chat.

        Returns:
            pandas.DataFrame: DataFrame containing the most common words and their frequencies.
        """
        try:
            f = open('./dependencies/stop_hinglish.txt', 'r')
            stop_words = f.read()
        except FileNotFoundError:
            st.error(
                'The server is unable to fetch the required file. Please try again later.')

        try:
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

        except Exception:
            st.write(
                'The data you provided has fewer metrics to show more about the selected user.')

        common_words.rename(columns={
            0: 'Words',
            1: 'Frequency'
        }, inplace=True)

        return common_words

    def most_used_emojis(self):
        """
        Find the most used emojis in the chat.

        Returns:
            pandas.DataFrame: DataFrame containing the most used emojis and their frequencies.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        emojis = []
        for message in df['message']:
            emojis.extend(
                [c for c in message if c in emoji.UNICODE_EMOJI['en']])

        most_used_emojis = pd.DataFrame(
            Counter(emojis).most_common(len(Counter(emojis))))

        most_used_emojis.rename(columns={
            0: 'Emojis',
            1: 'Frequency'
        }, inplace=True)

        return most_used_emojis.head(20)

    def timeline(self):
        """
        Generate the timeline of message counts.

        Returns:
            pandas.DataFrame: DataFrame containing the timeline of message counts.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        timeline = df.groupby(['year', 'month']).count()[
            'message'].reset_index()

        time = []
        for i in range(timeline.shape[0]):
            time.append(timeline['month'][i] + '-' + str(timeline['year'][i]))
        timeline['time'] = time

        timeline.rename(columns={
            'time': 'Time (Month-Year)',
            'message': 'Number of Messages'
        }, inplace=True)

        return timeline

    def daily_timeline(self):
        """
        Generate the daily timeline of message counts.

        Returns:
            pandas.DataFrame: DataFrame containing the daily timeline of message counts.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        daily_timeline = df.groupby('date').count()['message'].reset_index()

        daily_timeline.rename(columns={
            'date': 'Time (Date)',
            'message': 'Number of Messages'
        }, inplace=True)

        return daily_timeline

    def most_active_day_of_week(self):
        """
        Find the most active day of the week.

        Returns:
            pandas.DataFrame: DataFrame containing the most active day of the week and the number of messages on that day.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        most_active_day_of_week = df['day_name'].value_counts()

        weekdays = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        sorted_series = most_active_day_of_week.reindex(weekdays)

        index_lst = []
        values_lst = []

        for day, value in sorted_series.items():
            index_lst.append(day)
            values_lst.append(value)

        most_active_day_of_week = pd.Series(
            values_lst, index=index_lst).reset_index()

        most_active_day_of_week.rename(columns={
            'index': 'Day of the Week',
            0: 'Number of Messages'
        }, inplace=True)

        return most_active_day_of_week

    def most_active_month(self):
        """
        Find the most active month.

        Returns:
            pandas.DataFrame: DataFrame containing the most active month and the number of messages in that month.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        most_active_month = df['month'].value_counts()

        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

        sorted_series = most_active_month.reindex(months)

        index_lst = []
        values_lst = []

        for day, value in sorted_series.items():
            index_lst.append(day)
            values_lst.append(value)

        most_active_month = pd.Series(
            values_lst, index=index_lst).reset_index()
        most_active_month.rename(columns={
            'index': 'Month',
            0: 'Number of Messages'
        }, inplace=True)

        return most_active_month

    def activity_heatmap(self):
        """
        Generate the activity heatmap.

        Returns:
            pandas.DataFrame: DataFrame containing the activity heatmap.
        """
        if self.selected_user != 'Overall':
            df = self.df[self.df['users'] == self.selected_user]

        df = self.df

        pivot_table = df.pivot_table(
            index='day_name', columns='Period', values='message', aggfunc='count').fillna(0)

        return pivot_table


class GroupSpecificAnalysis(Analyse):
    """
    Class for performing group-specific analyses on the WhatsApp chat data.
    """

    def most_active_users(self):
        """
        Find the most active users in the group.

        Returns:
            pandas.DataFrame: DataFrame containing the most active users and the number of chats sent by them.
        """
        users = self.df['users'].value_counts().sort_values(
            ascending=False
        ).reset_index().head()

        users.rename(columns={
            'index': 'User Name',
            'users': 'Number of Chats'
        }, inplace=True)

        return users

    def most_active_users_percentage(self):
        """
        Find the percentage of chats sent by each user in the group.

        Returns:
            pandas.DataFrame: DataFrame containing the user names and their chat percentages.
        """
        users = round((self.df['users'].value_counts(
        ) / self.df.shape[0]) * 100, 2).reset_index().rename(
            columns={'index': 'User Name', 'users': 'Chat Percentage'})

        return users
