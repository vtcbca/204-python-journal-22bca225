#write a numpy script to create 3x3 matrix with values ranging from 2 to 10.
#output will print dimension and size of each element and array in memory

import numpy as np

#create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arrange(2, 11).reshape(3, 3)

#print the matrix
print("matrix:")
print(matrix)


#print the dimenson and size of each element

print("Element dimension and size:")
for element in np.nditer(matrix):
    print(f"Dimension: {element.ndim},size: {element.size}")

#print the dimension and size of the array in memory

print("Array dimension and size in memory:")
print("Dimension: {matrix.ndim},size: {matrix.size}, Memory usage: {matrix.nbytes} bytes")
