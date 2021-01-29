# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:19:25 2021

@author: mahindra.choudhary
"""
import numpy as np

#  Matrix
#  Create Matrices
#  Modifying Matrices
#  Accessing elements of a matrix
#  Matrix Operations 

#  MATRICES 
#  Rectangular arrangement consisting of numbers in rows and columns 
#  Create a matrix

# matrix() - returns a matric from an array type object or a string of data
#  Syntax :- numpy.matrix(data)

x = np.matrix("1,2,3,4,5,6,7,8,9,10")
x1 = np.matrix("1,2,3,4;4,5,6,7;7,8,9,10")


#############
# Matrix Properties 
#############

#  1. Shape command : shape() returns number of rows and columns in a matrix

x.shape
x1.shape
x.shape[0] # Number of rows
x.shape[1] # Number of columns 

#  2. size, returns the number of elements from a matrix

x.size
x1.size


#  3. Modify
#       1. Insert 
#           insert - adds values at a given positoon and axis in a matrix 
#           syntax : numpy.insert(matrix,obj,values,axis)

col_new = np.matrix('2,3,4')
x2 = np.insert(x1,0,col_new,axis = 1) # will insert at 0th position

row_new = np.matrix("2,3,4,5")
x3 = np.insert(x1,1,row_new,0)



#  Matrix addition
#  np.add(MatrixA,MatrixB)

#  Matrix Multiplication 
#  np.dot(A,B) , np.multiply does element wise multiplication

#  Matrix division 
#  np.divide() : does element wise division

