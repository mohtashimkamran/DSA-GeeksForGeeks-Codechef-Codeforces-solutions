
# print matrix in snake pattern
# def mat(arr,r,c):
#     for i in range(r):
#         if (i%2==0):
#             for j in range(c):
#                 print(arr[i][j],end=" ")
#         else:
#             for j in range(c-1,-1,-1):
#                 print(arr[i][j],end=" ")


# r=4
# c=4
# matr = [[ 10, 20, 30, 40 ], 
#        [ 15, 25, 35, 45 ], 
#        [ 27, 29, 37, 48 ], 
#        [ 32, 33, 39, 50 ]] 

# mat(matr,r,c)


# rotate a matrix by 90*
# import numpy as np
# def transpose(arr,n):
#     for i in range(n):
#         for j in range(i+1,n):
#             arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
#     for i in range(n):
#         low=0
#         high=n-1
#         while(low<high):
#             arr[low][i],arr[high][i]=arr[high][i],arr[low][i]
#             low+=1
#             high-=1
#     a=np.mat(arr)
#     return a

# matr = [[ 10, 20, 30, 40 ], 
#        [ 15, 25, 35, 45 ], 
#        [ 27, 29, 37, 48 ], 
#        [ 32, 33, 39, 50 ]] 

# n=4
# print(transpose(matr,n))


# searching in a sorted matrix efficient way

# def searchmatrix(arr,n,c,x):
#     i=0;j=c-1
#     while(i<n and j>=0):
#         if arr[i][j]==x:
#             print(i,j)
#             break
#         elif(arr[i][j]>x):
#             j-=1
#         else:
#             i+=1


# matr = [[ 10, 20, 30, 40 ], 
#        [ 15, 25, 35, 45 ], 
#        [ 27, 29, 37, 48 ], 
#        [ 32, 33, 39, 50 ]] 

# n=4
# c=4
# x=29
# searchmatrix(matr,n,c,x)

# reverse the columns of matrix

# row=int(input())
# column=int(input())
# mat=[]
# for i in range(row):
#     x=[]
#     for j in range(column):
#         x.append(int(input()))
#     mat.append(x)
# print(mat)

# for i in range(0,row):
#     start=0
#     end=row-1
#     while(start<end):
#         mat[i][start],mat[i][end]=mat[i][end],mat[i][start]

#         start+=1
#         end-=1

# print(mat)



#spiral traverse
def spirallyTraverse(m, n, a):
	k = 0
	l = 0
	while (k < m and l < n):
		for i in range(l, n):
			print(a[k][i], end=" ")

		k += 1
		for i in range(k, m):
			print(a[i][n - 1], end=" ")

		n -= 1
		if (k < m):

			for i in range(n - 1, (l - 1), -1):
				print(a[m - 1][i], end=" ")

			m -= 1
		if (l < n):
			for i in range(m - 1, k - 1, -1):
				print(a[i][l], end=" ")

			l += 1

