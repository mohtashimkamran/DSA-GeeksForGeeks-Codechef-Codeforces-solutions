# print matrix in snake pattern
def mat(arr,r,c):
    for i in range(r):
        if (i%2==0):
            for j in range(c):
                print(arr[i][j],end=" ")
        else:
            for j in range(c-1,-1,-1):
                print(arr[i][j],end=" ")


r=4
c=4
matr = [[ 10, 20, 30, 40 ], 
       [ 15, 25, 35, 45 ], 
       [ 27, 29, 37, 48 ], 
       [ 32, 33, 39, 50 ]] 

mat(matr,r,c)