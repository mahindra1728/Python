# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:25:34 2021

@author: mahindra.choudhary
"""

import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# load input variables from a file
data = pd.read_csv('Desktop/Holdup_850_5.1rpm.csv',na_values=('nan'))
x_values = data.iloc[:,0]
y_values = data.iloc[:,1]
y_values[0] = 0
def objective(x, a):
	return np.exp(-1/(a*x))

df1 = pd.DataFrame(np.exp(-x_values))
df2 = pd.DataFrame(x_values)
df3 = pd.DataFrame(np.ones((4618,1),int))
A   = pd.concat([df1,df2,df3],axis = 1)

b = pd.DataFrame(y_values)
a_t_b  = np.dot(A.T,b)
Coeff = np.dot(np.linalg.inv(np.dot(A.T,A)),a_t_b)

y_pred = np.dot(A,Coeff)

LSE = (np.subtract(b,y_pred))**2
SST = np.sum((np.mean(b) - b)**2)

R_square_exp = 1-np.sum(LSE)/SST

# fit curve
popt, _ = curve_fit(objective, x_values, y_values)

y_1 = ()
a = popt
for i in x_values:
    y_1 = np.append(y_1,objective(i,a),axis = 0)
    