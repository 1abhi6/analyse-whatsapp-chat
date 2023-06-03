# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:35:25 2023

@author: Aryan
"""

import pandas as pd
import numpy as np
import re

f = open('Untitled Folder/dataset/group_chat.txt','r',encoding='utf-8')
data = f.read()
print(data)

pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\u202f?(?:AM|PM|\d{2}:\d{2})\s-\s'

message = re.split(pattern,data)
print(message)