# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:43:38 2021

@author: mahindra.choudhary
"""
import numpy as np
#  Linear algebra operators using python 
#  Find rank of a matrix
#  Find determinant of a matrix
#  Find inverse of a matrix
#  Solving system of equations 
#  


# Determinant of a matrix 

# np.linalg.det() - returns the determinant of matrix
#  syntax:  np.linalg.det(matrix)

x = np.matrix("4,5,16,7;2,-3,2,3;4,3,6,7;1,4,12,9")
det_value = np.linalg.det(x)


#  Rank of a Matrix 
#  numpy.linalg.matrix_rank(matrix)

rank_x = np.linalg.matrix_rank(x)

#  Inverse of a matrix 
#  numpy.linalg.inv()
#  numpy.linalg.inv(matrix)

inv_matrix = np.linalg.inv(x)

B = np.matrix("2,1,2;1,0,1;3,1,3")
inv_B = np.linalg.inv(B) # Singlar Matrix(Determinant is zero for singular matrix)


#  System of Linear equations 

#  3x + y + 2z = 2
#  3x + 2y+ 5z = -1
#  6x + 7y + 8z = 3

#  numpy.linalg.solve(matrix_A,matrix_b)

A = np.matrix('3,1,2;3,2,5;6,7,8')
B = np.matrix('2,-1,3')
sol_linear = np.linalg.solve(A,np.transpose(B))  # Can also use B.T for B transpose 



