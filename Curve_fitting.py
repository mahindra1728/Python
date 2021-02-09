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

################
# Using Approximation
################

df0 = pd.DataFrame(x_values**3)
df1 = pd.DataFrame(x_values**2)
df2 = pd.DataFrame(x_values)
df3 = pd.DataFrame(np.ones((4618,1),int))
A   = pd.concat([df0,df1,df2,df3],axis = 1)

y = pd.DataFrame(y_values)
a_t_b  = np.dot(A.T,y)
Coeff = np.dot(np.linalg.inv(np.dot(A.T,A)),a_t_b)

y_hat = pd.DataFrame(np.dot(A,Coeff))

LSE = (np.subtract(y,y_hat))**2
SST = np.sum((np.mean(y) - y)**2)

R_square = 1-np.sum(LSE)/SST

a,b,c,d = Coeff

y_pred = []
for i in np.linspace(461.8, 600,1382):
    y_pred = pd.DataFrame(np.append(y_pred,a*i**3 + b*i**2 + c*i + d))

true_range = pd.DataFrame(np.linspace(0,461.7,4618)) 
pred_range = pd.DataFrame(np.linspace(461.8, 600,1382))

Data = pd.concat([y,true_range,y_hat,true_range,y_pred,pred_range],axis = 1)

Data.plot(x =np.linspace(0,600,6000),y = [Data.iloc[:,0],Data.iloc[:,2],Data.iloc[:,4]] )
plt.show() # I am unable to plot using this command

# Above case led to overfitting : High variance and Low bias 

###############
# Fitting using 2nd order polynomial
###############

###############
# Fitting using Logarithmic function
###############

###############
# Fitting using exponential function
###############

#####################
# Fitting using Objective function 
#####################    
 
def objective(x, a):
	return np.exp(-1/(a*x))
# fit curve
popt, _ = curve_fit(objective, x_values, y_values)

y_1 = ()
a = popt
for i in x_values:
    y_1 = np.append(y_1,objective(i,a),axis = 0)
    