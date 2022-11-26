import numpy as np;

#Task 1: Binary operation on an array and a scalar
arr = np.arange(1,11)
print(arr+1)

# Task 2: create a 10x10 matrix where A[i][j]=i+j
new_arr= np.arange(100).reshape(10,10)
for idx,x in np.ndenumerate(new_arr):
    new_arr[idx]= idx[0]+1 +idx[1]+1
print(new_arr)

#Task 3: Create a fake dataset of 50x5
import numpy.random as npr
data = np.exp ( npr.randn(50, 5) )
print(data)

#Task 4: Calculating the mean and standard deviation of each column(axis=0)
mean = np.mean(data,axis=0)
std = np.std(data,axis=0)
print("Mean: ",mean)
print("Standard Deviation: ",std)

#Task 5: Standardizing the data matrix
normalized = (data -mean)/std
norm_mean = np.mean(normalized,axis=0)
norm_std = np.std(normalized,axis=0)
print("Normalized Matrix Mean: ",norm_mean)
print("Normalized Matrix Standard Deviation: ",norm_std)


