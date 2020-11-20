# searching in a sorted matrix efficient way

def searchmatrix(arr,n,c,x):
    i=0;j=c-1
    while(i<n and j>=0):
        if arr[i][j]==x:
            print(i,j)
            break
        elif(arr[i][j]>x):
            j-=1
        else:
            i+=1


matr = [[ 10, 20, 30, 40 ], 
       [ 15, 25, 35, 45 ], 
       [ 27, 29, 37, 48 ], 
       [ 32, 33, 39, 50 ]] 

n=4
c=4
x=29
searchmatrix(matr,n,c,x)