# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:32:52 2021

@author: mahindra.choudhary
"""

# Numpy
#  Creating an array
#  Generating arrays using built in functions
#  Fundamental package for numerical computations in Python
#  Supports N-dimensional array objects that can be used for prpcessing
#       multidimensional data
#  Using numpy i can learn and perform
#       Mathematical and logical operations on arrays
#       Fourier transforms
#       Linear Algebra operations and
#       Random number generation


# 1. Creating an Array 

#  An array is ordered collection of elements of basic data types of given length
#  SAYNTAX TO CREATE AN ARRAY :  numpy.array(object)


import numpy as np
x = np.array([1,2,3,4,5])
type(x)
len(x)
x.shape

#  Numpy can handle different categorical entries

x1 = np.array([1,2,3,'a',4,5])

#  All elements in an array are coerced as same data type

# ############
# LINSPACE
##############
# numpy.linspace() - returns equally spaced numbers within given range based on the sample number
#  Syntax : numpy.linspace(start, stop, num, dtype, retstep)

x2 = np.linspace(1,20,20,True,False,int,axis = 0)
x3 = np.linspace(1,20,20,True,True,int,axis = 0)

#############
# arange()
#############
#  Generate array based on the step value.
#  numpy.arange() : returns equally spaced array
#  Syntax : numpy.arange(start, stop, step)

x4 = np.arange(1,20,0.01)
len(x4)

############
# ones()
############

# creates an array of ones in numpy array
# Syntax : np.ones(shape,dtype) , shape (integer or sequence of integer)
#                  dtype : default is float 

x5  = np.ones((3,3),int)

############
# zeros()
############

# creates an array of ones in numpy array
# Syntax : np.zeros(shape,dtype) , shape (integer or sequence of integer)
#                  dtype : default is float 

x6  = np.zeros((3,4),int)


############
# random.rand()
############


x7 = np.random.rand(5)
x8 = np.random.rand(5,5)


############
# logspace()
############

#  numpy.logspace() - returns equally spaced numbers based on log scale
#  numpy.logspace(start, stop, num, endpoint, base, dtype)
#  num : default is 50 , 


x9 = np.logspace(1,20,30,True,10,int,0)

############
# timeit
############

#  timeit is a module can be used to measure the execution time for the snippets of code
#  Comparing the processing speed of a list and an array using an addition operation 

x10 = range(1000000)

timeit sum(x10)


################
# ADVANTAGES OF NUMPY ARRAY 
################


#  getsizeof() - returns the size of object in bytes
#  Syntax : sys.getsizeof(object)

#  itemsize - returns the size of one element of a numpy array
#  numpy.ndarray.itemsize

#  Storage size 
import sys
sys.getsizeof(x10)


#  Reshaping an array 
#  reshape() - recasts an array to a new shape without changing its data 
np.arange(0,20).reshape(4,5)

#  Array dimensions 
x11 = np.array([[1,2,3],[4,5,6],[7,8,9]])
x11.shape

# Numpy addition
# numpy.add() : performs element wise addition of two arrays
# syntax : numpy.add(array_1,array_2)

a = np.arange(1,10).reshape(3,3)
b = np.arange(11,20).reshape(3,3)
np.add(a,b)

#  Numpy multiply
#  np.multiply(array_1,array_2)
np.multiply(a,b)

#  Numpy subtract
np.subtract(a,b)

#  Numpy divide 
np.divide(a,b)

# Numpy remainder
np.remainder(a,b)

###############
# Accessing components of an numpy array
###############
a[0,1]
a[1:3]
a[1:3,0:1]
a[1:3,1:3]


a[:,0] # extract elements of 1st col all rows
a[0,:] # all col first row

a[1:3,0]
a[0:2,0:2]
a[:2,:2]

a_sub = a[:2,:2]
a_sub[0,0] = 13


#  Transpose()
#  numpy.transpose()
#  numpy.transpose(array)
np.transpose(a_sub)
np.transpose(a)

#########
#  Append 
##########

#  numpy.append(array,axis)

np.append(a,[[14,15,17]],axis = 0)

np.append(a,np.array([14,15,17]).reshape(3,1),axis = 1)

#########
#  Insert 
#########

#  insert() - adds values at a given position and axis in an array
#  Syntax : numpy.insert(inp_array, obj, array_value_to_be_inserted, axis)


a
a_ins = np.array([45,32,12])
a_new = np.insert(a,1,a_ins,axis = 0)
a_new1 = np.insert(a,1,a_ins,axis = 1)
a_new2 = np.insert(a,1,np.transpose(a_ins),axis = 1)

#  Note : In insert there is no need to reshape the axis as we do in append 


#########
# Delete()
#########
#  delete()  - removes values ar a given position in an array
#  Syntax : numpy.delete(array,obj,axis)

a_del = np.delete(a_ins,1,axis = 0)
a_del1 = np.delete(a_new,1,axis = 0)
a_del2 = np.delete(a_new,1,axis = 1)













