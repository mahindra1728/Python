# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:19:42 2021

@author: mahindra.choudhary
"""

""" 
File formats
csv format
xlsx format
txt format
"""

import os
import pandas as pd
import numpy as np
data = pd.read_csv('Desktop/Data.csv',index_col = 0)

# Blank cells are read as Nan. Also replacee  ???? by missing values

data1 = pd.read_csv('Desktop/Data.csv',index_col = 0,na_values = '???,###')
data1.isna().sum()


# Excwl spreadsheet 

data_excel = pd.read_excel('Desktop/Data.xlsx', index_col = 0, na_values=('!!','##','###','$$','%%','&&','???'))
data_excel.isna().sum()


# Text format 

data_txt1 = pd.read_table('filename.txt',sep = '\t', delimiter = '\t')
# read_csv can also be used to read the txt file




