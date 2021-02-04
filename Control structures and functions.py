# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:40:31 2021

@author: mahindra.choudhary
"""
import os
import pandas as pd
import numpy as np
data = pd.read_csv('Desktop/Data.csv',index_col = 0)
# Control structure and functions

# For loop 
for i in range(1,1oo):
    if a<b:
        a = a+1
    elif a>=b:
        a = a-1
    else:
        a = a*a
            
# While loop 

# Used whenever i need to execute statements until a
# specific condition is violated

i = 0

while i<len(a):
    if b >d:
        b = b+1
    elif b<d:
        b = b-1
    else:
        b = b*b


# Series.value_counts()
# dataframe['colname'].value_counts()


# Functions in Python 

# A function accepts input arguments and produces an output by executing
# valid commands present in the function

# Function name and file names need not be the same

# A file can have one or more function definitions 

# Funcions are created using the command def and a colon with the statements to be executed indented as a block

# Since statements are not demarcated explicitly, it is essential to follow cottect indentation practises 

###########################
# Exploratory data analysis
###########################

# Frequency table
# Two way tables
# Two way table - Joint Probability
# Two way table - marginal probability 
# Two way table - conditional probability
# Correlation 
# Importing necessary libraries

import os 
import pandas as pd
import numpy as np

data = pd.read_csv('Desktop/Data.csv', index_col = 0,
                   na_values=('!!','##','###','$$','%%','&&','???','??'))

data2 = data.copy(deep = True)

#################
# Frequency table
#################

# pandas.crosstab()
# To compute a simple cross-tabulation of one, two or more factors 
# Or it means to compute the frequency table of the factors

cross_table = pd.crosstab(data2['activity'], columns = 'count',dropna = True) 

###################
# Two way table
###################
# To look at the frequency distribution of gearbox types with respect to different variable

cross_table2 = pd.crosstab(data2['activity'], data2['borrower_genders'],dropna = False)
cross_table3 = pd.crosstab(data2['activity'], data2['borrower_genders'],dropna = True)


###################
# Two way joint probability
###################

# Joint probability is the likelihood of two independent evevts hapenning at the same time 

cross_table4 = pd.crosstab(data2['activity'], data2['borrower_genders'],normalize= True,dropna = True)

##############
# Two way table marginal probability 
##############

# Probability of occurence of single event

cross_table5 = pd.crosstab(data2['activity'], data2['borrower_genders'],normalize = True, margins = True,dropna = True)

#################
# Two way rable conditional probability 
#################
# Given that certain activity is performed and gender is male, female or both

cross_table6 = pd.crosstab(data2['activity'], data2['borrower_genders'],normalize = 'index', margins = True,dropna = True)

cross_table7 = pd.crosstab(data2['activity'], data2['borrower_genders'],normalize = 'columns', margins = True,dropna = True)

##############
# Correlation 
##############

correlation_table = data.corr()






































