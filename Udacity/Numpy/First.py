import numpy as np
"""Numpy is short for Numerical python and it is usually uses np as it's alias
    Numpy is a python library used for arrays.
    Although python  has lists that can be used as arrays, they  are slow.
    hence NumPy aims to provide an array object that is upto 50* faster than lists.
    the array object is called ndarray."""
arr = np.array([1,2,3,4,5])
print(arr)

print(np.__version__)
#this is just printing the version

#to show the type of the array object created by np.array
print(type(arr))
#this will output numpy.ndarray

#Note:
#   to create an ndarray we can pass a list, tuple or any array-like object into the method array()

arr2 = np.array((1,2,3,4,5))
print(arr2)

##2-D Arrays
#An array with arrays as it's elements
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)
#Note:
#NumPy has a whole dedicated module towards matrix operators called numpy.mat

## 3D Arrays
#Note:
#     an array that has 2D arrays as it's elements is called a 3D array

arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr4)

#there is a method of finding the dimension of a ndarray
print(arr4.ndim)
print(arr3.ndim)
print(arr2.ndim)
#Note:
#     0 D is for a single number like [0]


###Indexing of ndarrays is the same as a list like it starts at 0,1,2..
print(arr2[0])#first element of ndarray arr2
print(arr3[0,1])#second element of the first array element of the ndarray arr3
print(arr4[1,0,2])#third number which is 9 of the first array in the second array of the ndarray arr4 