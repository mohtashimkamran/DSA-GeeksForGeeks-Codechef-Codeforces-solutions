# rotate a matrix by 90*
import numpy as np
def transpose(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n):
        low=0
        high=n-1
        while(low<high):
            arr[low][i],arr[high][i]=arr[high][i],arr[low][i]
            low+=1
            high-=1
    a=np.mat(arr)
    return a

matr = [[ 10, 20, 30, 40 ], 
       [ 15, 25, 35, 45 ], 
       [ 27, 29, 37, 48 ], 
       [ 32, 33, 39, 50 ]] 

n=4
print(transpose(matr,n))