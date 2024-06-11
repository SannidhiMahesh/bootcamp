import numpy as np

# Define two multi-dimensional arrays (matrices)
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Perform element-wise multiplication

"""Element-wise multiplication multiplies corresponding elements of the arrays. This means each 
 element in the first array is multiplied by the corresponding element in the second array."""

element_wise_result = np.multiply(array1, array2)

# Perform matrix multiplication
"""Matrix multiplication (also known as the dot product) is different from element-wise multiplication. 
In matrix multiplication, the elements of the rows of the first matrix are multiplied with corresponding
 elements of the columns of the second matrix and then summed."""
matrix_result = np.dot(array1, array2)


# Print the results
print("Element-wise multiplication result:")
print(element_wise_result)

print("\nMatrix multiplication result:")
print(matrix_result)
