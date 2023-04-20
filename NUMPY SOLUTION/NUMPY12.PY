#Write a numpy program to convert a list of numeric value into a one-dimensional numpy array.print original list and array with its dimension,size and byte occupiesin memory.
#output will show as below:
import numpy as np

#create a list of numeric values
my_list=[12.23,13.32,100,36.32]

#convert the list into Numpy array
my_array= np.array(my_list)

#print the original list
print("original list:",my_list)

#print the one-dimensional Numpy array
print("one-dimensonal numpy array:",my_array)

#print the dimension of the array
print("Dimension of the array:",my_array.ndim)

#print the size of the array
print("Size of the array:",my_array.size)

#print the byte occupied in memory by the array
print("Byte occupied in memory by the array:",my_array.nbytes)
