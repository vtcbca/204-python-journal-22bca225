#write a Numpy program to create a new shape to an array without changing its data.
import numpy as np

#original array
arr = np.array([[1, 2],[3, 4],[5, 6]])

#Reshped array to 2x3
reshaped_arr = np.reshape(arr, (2,3))

#printing original and reshaped arrays
print("Original array:\n", arr)
print("Reshaped array:\n", reshaped_arr)
