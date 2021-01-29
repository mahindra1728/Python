# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:26:47 2021

@author: mahindra.choudhary
"""

a = 14
b = a*10
a
b
print(np.array([a,b]))

#   Clearing console and environment
# %clear or ctrl + L , variable explorer will still be intact
# del, %reset

# numpy : import numpy 
# content = dir(numpy)
# print(content)
# help  > object > library and sublibrary name
# library.sublibrary (in search box)
#pandas
# matplotlib
# sklearn

physics,math,che = 80,90,95

# mahendra = "1"

# type(mahendra)

# int(mahendra)
# Cannot convert string to float

##########
# Operators and Operands
##########

# 2 + 3 # 2 is operand and + is operator

############
# Arithmetic Operators
############

# + Addition 
# - Subtraction
# * Multiplication
# / division
# % Remainder
# ** exponent
# (),**,/,*,+- hirerchy

############
# Assignment Operators
############
#  =.......ex:  a = b 
#  += .....ex: a = a+b is written as a+=b
#  -= .....ex: a = a-b is written as a-=b
#  *= .....ex: a = a*b is written as a*=b
#  /= .....ex: a = a/b is written as a/=b

####################
# Rational or comparisonal operators
####################

#  < strictly less than
#  <= less than equal to
#  > Greater than
#  >= Greater than equal to
#  == Equal to equal to
#  != Not equal to

#######################
# Logical Operators
#######################

# Used when operands are conditional statements
# and returns boolean value
# In python, logical operators are designed to 
#  work with scalar or boolean values.

#  or  print((x>y) or (x<y))
#  and print((x<y) and (x>y))
#  not print(not (x == y))

#############
# Bitwise operators
#############
# x = 5
#  y = 7
# | bitwise OR operator  x|y, output = 7
# & bitwise and operator
# 

if __name__ == '__main__':
    n = int(input(5))
    for i in range(1,n):
        print(i**2)

############
# list
############

#  Generic data strcture
#  enclosed between []
#  Create list of employee id and name 
num_emp = 4
id = [1,2,3,4]
name = ['Ram','preethi','satya','shyam']
employee_list = [id,name,num_emp]
employee_list[0][1]

# Negative indexing 
# -1 is the first index
employee_list[-3]

# Modify the components of list add and remove elements from the list
#  1. Based on the index positions 
#  2. Inbuilt functions

#  1. Based on the index positions 
employee_list[2] = 5
employee_list[1][2] = 'Karan'

#  2. Inbuilt functions : append(),insert(),del(),remove(),pop()

#  append() - adds an object at the end of the list
#  listname[index].append(object) , if the index is not specified the object is added to next level in the list.
#  There are 2 ways to add an object to a list
#       1. Adding an element to list
#       2. Adding a list to a list

employee_list[0]
employee_list[0].append(5)
employee_list.append(5)
employee_list.append([23,24,26,28,32])

#  insert() - add a element in a specified position

employee_list[0].insert(0,6)
employee_list[0].append(6)

# del()- removes the object at the specified index number
del employee_list[3]

# remove() - removes the first matching object from a list

employee_list[0].remove(5)  #will remove 6 from the list

#  pop() - displays object removed from specified list number
# syntax : list_name[index1].pop(index2)
employee_list[0].pop(1)
employee_list[0:2]

###############
# TUPLES
###############

#  Create tuple
#  Indexing
#  Access components
#  Slicing
#  Built in functions
#  Combine multile tuples
#  Modify the components of tuples


""" 
1. Considered as an ordered collection of objects
2. Some of the operations on tuples are similar to lists
3. Tuples are enclosed between () parantheses
4. Tuples are immutable, unable to modify later

"""

#  Create employee detail tuple

employee_detail = ('P001','John',35,40000)

#  Indexing 
#       Positive : starts from 0, left to right
#       Negative : starts from -1, right to left
#       Access elements: Use [] as an operator
employee_detail[1]


#  Slicing : To access a multiple set of elements
#  [x:y] :: [inclusive:exclusive]
employee_detail[1:3]

#  Length of tuple :Number of elements in the tuple
len(employee_detail)
#  Other : min(),max() etc

# Combine multiple tuples 
employee_education = ('Mtech','Accounts')
tuple2 = employee_education + employee_detail
tuple3 = employee_detail + employee_education

#  Tuples cannot be modified  
#       Elements cannot be added or modified
#       from tuples using index number or functions
employee_education[0] = 'Btech'


################
# DICTIONARY
################

#  What is dictionary
#  Creating a dictionary
#  Components of a dictionary
#  Modify the components.

#  It is an example of hash-table data structure
#  Enclosed in {}
#  Mutable

#  Creating a dictionary

fuel_type = {'Petrol':1,'Diesel':2,'CNG':3}
fuel_type['Petrol']
fuel_type['Diesel']
fuel_type['CNG']

#  Components
fuel_type.keys()
fuel_type.values()
fuel_type.items()

# Mutation
fuel_type['electric'] = 4

# Update 
fuel_type.update({'Hyrid': 5})

#  Modify value of existing Key
fuel_type['electric'] = 5

#  Remove components from dictionary
#  del - removes the key value pairs 

del fuel_type['electric']
len(fuel_type)

#  Clear() - removes all the key value pairs

fuel_type.clear()


###########
# SETS
###########

# We will learn to create and modify sets 















































