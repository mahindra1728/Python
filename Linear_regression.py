# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:17:48 2021

@author: mahindra.choudhary
"""

#######################
# Simple Linear regression 
#######################

# Step 1 
"""
The first step is to import the package numpy and the class LinearRegression 
from sklearn.linear_model:
"""

import pandas as pd # Pandas Package 
import numpy as np # Numpy package 
from sklearn.linear_model import LinearRegression # Class 
import random
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler

# Step 2:  iImporting the required data 
x0 = np.random.rand(5) # 5 Random numbers between 0 and 1
x1 = np.random.randn(5) # Random float number
x2 = np.random.randint(1,10,5) # Random integer number
x3 = random.randrange(0,100,2) # Generate a random number between 0 and 100 divisibel by 2
x4 = random.randrange(0,100,5) # Generate a random number between 0 and 100 divisibel by 5

####################
# Other functionf to generate random numbers 
####################
""" 
seed()
Values produced will be deterministic, meaning, when the seed number is the same, the same sequence of values will be generated

ex: random.seed(n)

randrange()
Can return random values between the specified limit and interval

ex:  random.randrange(2,60,2)

randint()
Returns a random integer between the given limit

ex: import random
    random.randint(2,9)

choice()
Returns a random number from a sequence

ex:  random.choice([1,2,3,4,5,6,7,8,9])

shuffle()
Shuffles a given sequence

ex: mylist=[1,2,3,4,5,6,7,8,9]
    random.shuffle(mylist)

sample()
Returns randomly selected items from a sequence

ex: random.sample([1,2,3,4,5,6,7,8,9],4)

uniform()
Returns floating-point values between the given range

random()

ex : random.random()

"""

x = pd.DataFrame(np.random.rand(100))
y = pd.DataFrame(3.1*x -0.5)

sns.set(style= 'darkgrid')
sns.regplot(x = x, y = y,fit_reg=(True))
plt.scatter(x,y)

# Linear regression model
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
model.intercept_
model.coef_


sns.distplot(y)
sns.distplot(x)

# Both the x and y follows same distribution because it is linearly correlated
# Let us check if the error follows the same distribution

y_pred = model.intercept_ + model.coef_*x

error = y - y_pred
sns.distplot(error)
plt.scatter(x,error) # Error is very small, there is no meaning to plot this 

###############################
# Lets take some other dataset 
###############################
# Download link : https://www.kaggle.com/sohier/calcofi

raw_data = pd.read_csv('Summary of Weather.csv')

# Raw data info
info = raw_data.info()

# Extracting only numerical data
num_raw_data = raw_data.select_dtypes(exclude = object )

# Histogram of the dataset
sns.distplot(num_raw_data.iloc[:,1]) # Histogram of individual numerical column
num_raw_data.hist() # Histogram of whole dataset

# Scatter plot for whole dataset

g = sns.pairplot(num_raw_data.iloc[:,0:16], kind = 'scatter')
g.fig.set_size_inches(15,15)

x = pd.DataFrame(num_raw_data['MEA'])
y = pd.DataFrame(num_raw_data['MinTemp'])


dataset = pd.concat([x,y],axis=1).dropna(axis = 0)

x = pd.DataFrame(dataset['MEA'])
y = pd.DataFrame(dataset['MinTemp'])


# Linear regression model
model = LinearRegression()
model.fit(pd.DataFrame(dataset['MEA']), pd.DataFrame(dataset['MinTemp']))
r_sq = model.score(pd.DataFrame(dataset['MEA']), pd.DataFrame(dataset['MinTemp']))
model.intercept_
model.coef_

y_pred = model.intercept_ + model.coef_*x

error = np.subtract(y,y_pred)
sns.distplot(error,bins = 100)
plt.scatter(x,error) # Error is very small, there is no meaning to plot this 







