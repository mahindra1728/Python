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
counts = pd.crosstab(data['borrower_genders'],columns = 'gender')
plt.bar(data['borrower_genders'].unique(),[counts.iloc[0,0],counts.iloc[1,0],counts.iloc[2,0]])


###############
# Seaborn Library 
###############

import seaborn as sns

sns.set(style= 'darkgrid')
sns.regplot(x = data['lender_count'],y = data['loan_amount'])
# Above is with regression fit line

# Without regression fit line 

sns.regplot(x = data['lender_count'], y = data['loan_amount'], fit_reg=(False),marker = 's')

# Markers : * ,o,s

# Scatter plot 
sns.lmplot(x = 'lender_count', y ='loan_amount',data = data) # With regression

sns.lmplot(x = 'lender_count', y ='loan_amount',data = data,fit_reg=(False),legend = True, hue = 'borrower_genders') # Without regression


#############
# Histogram 
#############

sns.distplot(data['loan_amount'],kde = False,bins = 1000)
# sns.plt.xlim(0,15000)

#############
# Bar Plot
#############

sns.countplot(x = 'borrower_genders',data = data)

##############
# Grouped bar plot
##############

sns.countplot(x = 'borrower_genders',data = data, hue = 'currency_policy')


##################
# Box and whiskers plot : Numerical Variable
##################

sns.boxplot(y = data['lender_count'])


##################
# Box and whiskers plot : Numerical vs categorical variable
##################

sns.boxplot(x = data['borrower_genders'],y = data['lender_count'])


##############
# Grouped box and whiskers plot 
##############

sns.boxplot(x = data['borrower_genders'],y = data['lender_count'], hue = 'currency_policy', data = data)


##################
# Box whiskers plot and histogram
##################

f,(ax_box, ax_hist) = plt.subplots(2,gridspec_kw = {'height_ratios':(0.20,0.80)})

sns.boxplot(data['rMPI'],ax = ax_box)

sns.distplot(data['rMPI'], ax = ax_hist, kde = False)


###################
# Pairwise Plots
##################

# It is used to plot pairwise relationships in a dataset
# Created scatterplots for joint relationships and histograms for univariate distributions

sns.pairplot(data, kind = 'scatter', hue = 'currency_policy')
plt.show





































