# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:10:30 2021

@author: mahindra.choudhary
"""

#######################
# Dealing with missing values
#######################

# Identifying the missing values
# Approaches to fill the missing values


# Importing the necessary libraries

import os
import pandas as pd

# Importing data 
data = pd.read_csv('Desktop/Data.csv',index_col= 0,na_values=('!!','##','###','$$','%%','&&','???','??')
                   )
# data1 = data.dropna(axis = 0, inplace = True)

data2 = data.copy(deep = True)
data3 = data2.copy(deep = True)

# Identifying the missing values 

""" 
In pandas dataframe the missing data is represented as NaN (an acronym for Not a number)
To check the null values, in pandas dataframe, isnull and isna is used
These functions returns a dataframe of boolean values which are True for NaN

"""
data.isna().sum()
data.isnull().sum()

missing = data[data.isnull().any(axis = 1)]


####################
# Approach to fill missing values 
####################

# 1. Mean ,Median and other methods for numerical variable
# 2. Maximum xount in case of categorical variable

# Imputing the missing values 

description = data.describe() # Describe the data 


# Calculate the mean value 
data['lender_count'].mean()
data['lender_count'].fillna(data['lender_count'].mean(),inplace = True)


data['borrower_genders'].value_counts().index[0]

data['borrower_genders'].fillna(data['borrower_genders'].value_counts().index[0],inplace = True)






















