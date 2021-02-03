# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:53:54 2021

@author: mahindra.choudhary
"""

###
# Introduction to pandas 
# Importing data to spyder
# Creating copy of original data
# Attributes of data
# Indexing and selecting data 

# Provides high perfoermance easy to use data structure 
# and analysis toosl for the python language

# Data manipulation and analysis tool using its powerful data structures

import os
import pandas as pd
import numpy as np

# Changing the working directory

os.chdir('Change directory name')

# Importing Data 

loan_data = pd.read_csv('Data.csv', index_col = 0,na_values=('???','###'))

# Creating the copy of original data 
# Shallow copy
# Deep copy 

# deep = False then the changes will be reflected in the original dataset
# deep = True, then the changes in the dataset will not be reflected in the original dataset
# data.index # To get the index(row labels) of the dataframe
# data.columns # to get the labels of columns in dataframe
# dataframe.size : to get the total number of elements in the data matrix
# dataframe.memory_usage() : memory usage of each column in bytes
# dataframe.ndim : to get number of axes/array dimension

# Indexing and Selecting data 
# [] and '.' is used for indexing 
# dataframe.head(n) : returns first n rows from the dataframe 
# dataframe.tail(n) : returns last n rows of an object 
# at and iat fastest method to access scalar values
#       at provides label-based scalar lookups
#       iat provides integer based lookups 

# To access group of rows and columns by label use .loc[] 

# Numeric types : 
    # Int(Numeric character) and float(Numeric character with decimals)
    # pandas datatype is int64 and float 64.. 64 = 8 byte, each byte is equal to 8 bit

# Category and Object:
    # Category : 
        # A string variable consisting of anly a few different values
        # Converting such string variable to a categorical variable will save some memory
    
    # Object : 
        # A column will be assigned as an object data type when it has mixed types(numbers and strings)
        # If a column contains 'nan' blank cells pandas will default to object datatype
        
# dataframe.dtypes : returns series with the data type of each column in the dataset
# dataframe.get_dtype_counts() : returns the counts of unique data types in the dataframe
# dataframe.select_dtypes(include = None, exclude = None) : returns a subset of the columns from dataframe based on the column dtypes
# dataframe.info() : returns concise summary of data 
# np.unique(array) : returns unique elements of a column array 
# dataframe.astype(dtype) : explicitly convert data types from one to another 
# dataframe.nbytes : is used to get total bytes consumed by the elements of the columns 
# dataframe.replace : used to replace a string,value with a desired value in a matrix or column
# dataframe.isnull.sum() : is used to check the missing values in the column
# 


















































































































