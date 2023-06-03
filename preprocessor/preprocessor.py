# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 00:39:53 2023

@author: Abhishek
"""
import re
import pandas as pd


class Preprocess:
    def __init__(self,data):
        self.data = data
    
    def text_to_df(self):
        pattern = r'\n?\d{2}/\d{2}/\d{2,4},\s\d{1,2}:\d{2}\u202f?(?:am|pm|\d{1,2}:\d{2})\s-\s'
        
        # Split the data based on the pattern
        messages = re.split(pattern,self.data)[1:]
        
        dates = re.findall(pattern,self.data)
        
        # Clean the dates list
        cleaned_date_strings = [date_string.strip('\u202f- \n') for date_string in dates]
        
        # Create dataframe of user_messages and date
        df = pd.DataFrame({
            'user_message' : messages,
            'date' : cleaned_date_strings
        })
        
        # Convert message datatype
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M\u202f%p')
        
        # Separate users and message
        users = []
        messages = []
        
        for message in df['user_message']:
            entry = re.split('([\w\W]+?):\s',message)
            if entry[1:]:
                users.append(entry[1])
                messages.append(entry[2])
            else:
                users.append('Group Notification')
                messages.append(entry[0])
        
        df['users'] = users
        df['message'] = messages
        df.drop(columns=['user_message'],inplace=True)
        
        # Extraxt year, month, day, hour and minutes
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month_name()
        df['day'] = df['date'].dt.day
        df['hour'] = df['date'].dt.hour
        df['minute'] = df['date'].dt.minute
        
        # Drop the date column since it is not required
        df.drop(columns='date',inplace=True)
        
        return df
        