# -*- coding: utf-8 -*-
"""
This module provides a Preprocess class for converting chat data into a 
structured pandas DataFrame.

The Preprocess class defines a method, `text_to_df()`, which takes a 
string of chat data and performs the following preprocessing steps:

1. Splits the data into individual messages based on a specific pattern.
2. Extracts the dates from the messages and cleans the date strings.
3. Creates a DataFrame with columns for user, message, and date.
4. Converts the date column to datetime format.
5. Separates the user and message components from each message.
6. Appends the user and message data to the DataFrame.
7. Extracts year, month, day, hour, and minute information from the date.
8. Drops the unnecessary date column from the DataFrame.

Created on Sun Jun  4 00:39:53 2023

@author: Abhishek Santosh Gupta
@github: github.com/1abhi6
"""

import re
import pandas as pd


class Preprocess:
    def __init__(self, data):
        """
        Initialize the Preprocess class.

        Parameters:
        - data (str): The input data containing chat messages.
        """
        self.data = data

    def text_to_df(self):
        """
        Convert the chat data into a pandas DataFrame.

        Returns:
        - df (pandas.DataFrame): DataFrame containing processed chat data.
        """

        # Define the pattern to split the data into messages
        pattern = r'\n?\d{2}/\d{2}/\d{2,4},\s\d{1,2}:\d{2}\u202f?(?:am|pm|\d{1,2}:\d{2})\s-\s'

        # Split the data based on the pattern
        messages = re.split(pattern, self.data)[1:]

        # Extract the dates using the pattern
        dates = re.findall(pattern, self.data)

        # Clean the dates list
        cleaned_date_strings = [date_string.strip(
            '\u202f- \n') for date_string in dates]

        # Create a DataFrame with user messages and date
        df = pd.DataFrame({
            'user_message': messages,
            'date': cleaned_date_strings
        })

        # Convert the date column to datetime format
        df['datetime'] = pd.to_datetime(
            df['date'], format='%d/%m/%y, %I:%M\u202f%p')

        # Separate users and messages
        users = []
        messages = []

        for message in df['user_message']:
            entry = re.split('([\w\W]+?):\s', message)
            if entry[1:]:
                users.append(entry[1])
                messages.append(entry[2])
            else:
                users.append('Group Notification')
                messages.append(entry[0])

        df['users'] = users
        df['message'] = messages
        df.drop(columns=['user_message'], inplace=True)

        # Drop the date column since it is not required
        df.drop(columns='date', inplace=True)

        # Extract year, month, day, hour, and date from the datetime column
        df['year'] = df['datetime'].dt.year
        df['month'] = df['datetime'].dt.month_name()
        df['day'] = df['datetime'].dt.day
        df['day_name'] = df['datetime'].dt.day_name()
        df['hour'] = df['datetime'].dt.hour
        df['date'] = df['datetime'].dt.date
        
        # Add period of an hour as Period column in the df
        period = []
        for hour in df[['day_name', 'hour']]['hour']:
            if hour == 23:
                period.append(str(hour) + "-" + str('00'))
            elif hour == 0:
                period.append(str('00') + "-" + str(hour + 1))
            else:
                period.append(str(hour) + "-" + str(hour + 1))
                
        df['Period'] = period
        
        return df
    