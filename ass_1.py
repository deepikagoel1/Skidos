# -*- coding: utf-8 -*-
"""ass_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/goeld9911/Skidos/blob/master/ass_1.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data_quality_sample_data.csv") #Load dataset
df.head()

df.info() #Getting information regarding each column from a dataframe

df.describe() #getting statistical information

df.isnull().sum() #checking null values in each column

df.shape

#Calculating the percentage of nll values for each column
percent = []
for i in df.columns:
    key_perc = (df[i].isnull().sum() * 100)/df.shape[0]
    percent.append(key_perc)
print(percent)

#Since all the columns have string values so we can't substitute with the mean values.
df.dropna(subset=["Keywords", "IdUser", "InorganicSource", "Campaign", "State", "Country"], axis=0, inplace = True)

df.isnull().sum()

#After removing the missing values, th
df.shape

#Checking the frequency of items in each column of a dataframe.
for i in df.columns:
    c = df[i].value_counts()
    print(f"\nColumn Name: {i}, counts: {c}\n")

