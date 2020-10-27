#Frequencies of Limited Range Array Elements
# import collections
# arr=list(map(int,input().split()))
# a=collections.Counter(arr)
# print(a)
# a=list(map(int,input().split()))
# x=[]
# c=0
# for i in range(1,len(a)-1):
#     if i == a[i]:
#         c+=1
#         x.append(c)
#     else:
#         x.append(0)
# print(x)

import collections
def printfrequency(a,N):
    x=[]
    counter=collections.Counter(a)
    for i in range(1,N+1):
        if i not in counter:
            # print(0,end=' ')
            x.append(0)
        else:
            # print(counter[i],end=' ')
            x.append(counter[i])
    global A
    A=x
    return " ".join(str(x)for x in A)
n=int(input())
A=list(map(int,input().split()))
printfrequency(A,n)
print(A)
