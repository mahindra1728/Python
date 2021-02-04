# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:24:56 2021

@author: mahindra.choudhary
"""
"""
# Data visualizations
# Allows to quickly interpret the data and adjust different variable t see their effect
# Pyhton provides multiple graphic libraries that offers diverse features 

# matplotlin : 2D graphs and plots 

# pandas visualization : easy to use the interface, buile on Matplotlib

# seaborn : Provides high level interface for drawing attractive 
#               and informative statistical graphics

# ggplot: based on R's ggplot2 and uses grammar on graphics

# plotly : can create interactive plots


# matplotlib  :  It has origins in emulating the matlab graphics commands, 
                    # it is independent of matlab 
                
# Uses numpy and other extension code to provide good performance even for large arrays.

# 1. Scatter plot
#   Convey relationship between two numerical variables
#   Also called as Correlation plots
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Desktop/Data.csv',index_col= 0,na_values=('!!','##','###','$$','%%','&&','???','??')
                   )
data.dropna(axis = 0, inplace = True) # Removing the missing values (na values from the dataframe)


###########
# Scatter plot
###########

plt.scatter(data['loan_amount'],data['lender_count'])
plt.title('Scatterplot of Loan_amount vs lender_count')
plt.xlabel('Loan amount')
plt.ylabel('Lender_count')
plt.show()


###########
# Histogram 
###########

# It is a graphical representation using bars of different heights
# Histogram groups numbers into ranges and height of each bar depict the frequency of each range or bin 
# Used to represent frequency distribution of each value 

plt.hist(data['loan_amount'],bins = 1000,color='red',edgecolor = 'black')
plt.xlim([0,15000])

plt.hist(data['lender_count'],bins = 1000)
plt.xlim([0,200])


#########
# Bar plot 
#########

# Represents the categorical data with rectangular bars with lengths proportional to the counts they represent
#  Used to represent the frequency distribution of categorical data
# A bar diagram makes it easy to compare sets of data between different groups 

plt.bar(data['borrower_genders'])
























