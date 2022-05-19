#array arithemetic Operations
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 25, 4, 15, 4])

addarr = np.add(arr1, arr2)
subarr = np.subtract(arr1, arr2)
multarr = np.multiply(arr1, arr2)
modarr = np.mod(arr1, arr2)
divarr = np.divide(arr1, arr2)

print("The arrays after performing arithmetic operations")
print("Array Addition = ", addarr)
print("Array Subtraction = ", subarr)
print("Array Multiplication =  ", multarr)
print("Array Modulus = ", modarr)
print("Array division = ", divarr)
