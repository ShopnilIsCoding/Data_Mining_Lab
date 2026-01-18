import numpy as np

arr = np.array([1, 2, 3, 4,5,6]) 

print("Array dimension ",arr.ndim)
#array indexing
print("indexing sum ",arr[2] + arr[3])

# array slicing

print("sliced array1 ",arr[1:3])
print("sliced array2 ",arr[:4])

# array data types
newarr = arr.astype('S')
print("Array data type ",newarr.dtype)

#array copy
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#array shape
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array2 shape ",arr2.shape)

#reshaping array
arr3 = arr2.reshape(3, 2)
print("Reshaped array3 ",arr3)

#iterating array
for x in arr:
    print("iterating ",x)

#joining arrays
print("Joining arrays ",np.concatenate((arr, arr2.flatten())))

arr4 = np.array([[1, 2], [3, 4]])

arr5 = np.array([[5, 6], [7, 8]])

arrCon = np.concatenate((arr4, arr5), axis=1)

print("axis-wise concatenate",arrCon)

#array splitting
print("Splitting array ",np.array_split(arr, 3))

#searching array
print("Searching array ",np.where(arr > 2))

#sorting array
unsorted_arr = np.array([3, 1, 4, 2])
sorted_arr = np.sort(unsorted_arr)
print("Sorted array ",sorted_arr)

#filtering array
filter_arr = arr[arr > 2]
print("Filtered array ",filter_arr)

#mathematical operations
print("Sum of array elements ",np.sum(arr))
print("Mean of array elements ",np.mean(arr))
print("Standard deviation of array elements ",np.std(arr))
print("Variance of array elements ",np.var(arr))
print("Minimum of array elements ",np.min(arr))
print("Maximum of array elements ",np.max(arr))
print("Square root of array elements ",np.sqrt(arr))
print("Exponential of array elements ",np.exp(arr))
print("Natural logarithm of array elements ",np.log(arr))
print("Sine of array elements ",np.sin(arr))
print("Cosine of array elements ",np.cos(arr))
print("Tangent of array elements ",np.tan(arr))
print("Dot product of two arrays ",np.dot(arr4, arr5))
print("Matrix multiplication of two arrays ",np.matmul(arr4, arr5))
print("Cross product of two arrays ",np.cross([1, 2, 3], [4, 5, 6]))

#random number generation
rand_arr = np.random.rand(3, 2)
print("Random array ",rand_arr)
rand_int_arr = np.random.randint(1, 10, size=(3, 2))
print("Random integer array ",rand_int_arr)
rand_norm_arr = np.random.normal(0, 1, size=(3, 2))
print("Random normal array ",rand_norm_arr)
rand_choice_arr = np.random.choice([10, 20, 30, 40, 50], size=(3, 2))
print("Random choice array ",rand_choice_arr)

#statistical functions
print("Median of array elements ",np.median(arr))
print("Percentile of array elements (50th) ",np.percentile(arr, 50))
print("Correlation coefficient between two arrays ",np.corrcoef([1, 2, 3], [4, 5, 6]))
print("Covariance matrix of two arrays ",np.cov([1, 2, 3], [4, 5, 6]))
#linear algebra
matrix = np.array([[1, 2], [3, 4]])
inv_matrix = np.linalg.inv(matrix)
print("Inverse of matrix ",inv_matrix)
det_matrix = np.linalg.det(matrix)
print("Determinant of matrix ",det_matrix)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues of matrix ",eigenvalues)
print("Eigenvectors of matrix ",eigenvectors)
#Fourier Transform
fourier_arr = np.fft.fft(arr)
print("Fourier Transform of array ",fourier_arr)
inv_fourier_arr = np.fft.ifft(fourier_arr)
print("Inverse Fourier Transform of array ",inv_fourier_arr)