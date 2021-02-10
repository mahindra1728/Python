# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:16:05 2021

@author: mahindra.choudhary
"""

# Case study 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Logistic_Regression
from sklearn.metrics import accuracy_score,confusion_matrix

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

###############
# Importing Data
###############

data_income = pd.read_csv('income1.csv')


# Creating a copy of original data

data = data_income.copy()

"""
# Exploratory Data Analysis 

# Getting to know the Data
# Data preprocessing (Missing Values)
# Cross table and Data visualisation

"""

########################
# Getting to know the data
#######################

# To check the variable typs
data.info()

# Checking for missing values
data.isnull().sum() # There are no missing values 


# Summary of numerical variables 
summary_num = data.describe()

# Summary of categorical variables
summary_cat = data.describe(include = "O")

# Frequency of each category 
summary_cat.iloc[2:4,:] # Frequency of Top category 

data['Job type'].value_counts()
data['Occupation'].value_counts()

# Checking for unique classes

np.unique(data['Job type'])
np.unique(data['Occupation'])

# Cleaning the ? values and replacing by na
data_income1 = pd.read_csv('income1.csv', na_values = [" ?"])
data1 =data_income1.copy() 
#######################
# Data preprocessing
#######################

data1.isnull().sum()

data1.isna().sum()

missing_data = data1[data1.isnull().any(axis = 1)]

# Missing values in Job type = 1843
# Missing values in occupation = 1836 
# Missing values in native country = 583

# Total missing should b3  = 1843 + 1836 + 583 = 4262, bu the missing data matrix is of length 2399. Thus tells there are some common missning values in those  columns

data2 = data1.dropna(axis = 0) # This will delete those rows where there is atlaeast 1 nan
data3 = data1.dropna(axis = 1) # This will delete those columns where there is atleast 1 nan

# Relationship between variables 

np.linalg.matrix_rank(data2)
num_data = data2.select_dtypes(exclude = 'object')

np.linalg.matrix_rank(num_data) # Check ranl of a matrix
num_data.corr() # Correlation matrix


#################################################
# Cross tables and Data Visualisation 
#################################################

data2.columns

# Gender proportion table
gender  = pd.crosstab( data2['Gender'], columns = 'count', normalize = True)

# Gender v/s Salary status 
gender_salarystat = pd.crosstab(data2['Gender'], [data2['Salary stat'],data2['Race']])


####################################
# Frequency Distribution of a column
####################################

sns.countplot(data2['Salary stat'])

####################################
# Histogram Plot 
####################################

sns.distplot(data2['Age'],bins = 100, kde =False)


###############################
# Box plot of Age v/s Salary 
###############################

sns.boxplot('Salary stat','Age', data = data2)
data2.groupby('Salary stat')['Age'].median()

####################### 
# Bar Plot 
######################

sns.countplot(y = 'Ed type', data  = data2,hue = 'Salary stat')

sns.countplot(y = 'Occupation', data  = data2,hue = 'Salary stat')



































