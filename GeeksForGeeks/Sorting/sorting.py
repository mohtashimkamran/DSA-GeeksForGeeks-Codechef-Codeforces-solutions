# BUBBLE SORT

# # a=[1,4,5,9,2]
# a=list(map(int,input().split()))
# for i in range(0,len(a)):
#     for j in range(i,len(a)):
#         if (a[i]>a[j]):
#             a[i],a[j]=a[j],a[i]
# print(a)

# INSERTION SORT
# # a=[1,2,4,5,3,0,9,7]
# a=list(map(int,input().split()))
# for i in range(1,len(a)):
#     key=a[i]
#     j=i-1
#     while(j>=0 and key<a[j]):
#         a[j+1]=a[j]
#         j=j-1
#     a[j+1]=key
# print(a)

# UNION OF 2 SORTED ARRAYS
# a=[1,2,3,4,5]
# b=[1,2,3]
# print(set(a+b))

# a=set([1,2,3,4,5])
# b=set([1,2,3])
# print(a.intersection(b))


# LOMETO PARTITION
# # a=[10,80,30,90,40,50,70]
# n=int(input())
# a=list(map(int,input().split()))
# # partition=int(input())
# # a[partition],a[n-1]=a[n-1],a[partition]
# pivot=n-1
# high=n-1
# low=0
# i=low-1
# for j in range(low,high):
#     if(a[j]<a[pivot]):
#         i+=1
#         a[i],a[j]=a[j],a[i]
# a[i+1],a[high]=a[high],a[i+1]
# print(a)

# def lomato(a,l,h,n):
#     p=n-1
#     i=l-1
#     for j in range(l,h):
#         if(a[j]<a[p]):
#             i+=1
#             a[i],a[j]=a[j],a[i]
#     a[i+1],a[h]=a[h],a[i+1]
#     return a

# l=0
# a=[10,80,30,90,40,50,70]
# n=len(a)
# h=n-1
# print(lomato(a,l,h,n))

# Quick Sort
# def lomato(a,l,h):
#     p=h
#     i=l-1
#     for j in range(l,h):
#         if(a[j]<a[p]):
#             i+=1
#             a[i],a[j]=a[j],a[i]
#     a[i+1],a[h]=a[h],a[i+1]
#     return i+1
# def quicksort(a,l,h):
#     if(l<h):
#         p=lomato(a,l,h)
#         quicksort(a,l,p-1)
#         quicksort(a,p+1,h)
#     return a
# l=0
# a=[10,80,30,90,40,50,70]
# h=len(a)-1
# print(quicksort(a,l,h))

# KTH SMALLEST

# def lomato(a,l,h):
#     p=h
#     i=l-1
#     for j in range(l,h):
#         if(a[j]<a[p]):
#             i+=1
#             a[i],a[j]=a[j],a[i]
#     a[i+1],a[h]=a[h],a[i+1]
#     return i+1
# def KthSmallest(a,l,h,k):
#     while(l<=h):
#         p=lomato(a,l,h)
#         if(p==(k-1)):
#             return a[p]
#         elif(p>(k-1)):
#             h=p-1
#         else:
#             l=p+1
#     return -1
# a=[10,80,30,90,40,50,70]
# l=0
# h=len(a)-1
# k=2
# print(KthSmallest(a,l,h,k))

#segregate elements in array
#-ve +ve rearrange
# a=[-2,1,-3,5]
# a.sort()
# print(a)

# even first then odd
# a=[12,5,2,7]
# x=[]
# y=[]
# for i in range(len(a)):
#     if (a[i]%2==0):
#         x.append(a[i])
#     else:
#         y.append(a[i])
# print(x+y)

# print 0 first then 1 in binary array
# a=[0,1,0,1,0,1]
# a.sort()
# print(a)

# def sort0s1s2s(arr,n):
#     l=0
#     h=n-1
#     mid=0
#     while(mid<=h):
#         if(arr[mid]==0):
#             arr[mid],arr[l]=arr[l],arr[mid]
#             l+=1
#             mid+=1
#         elif(arr[mid]==1):
#             mid+=1
#         else:
#             arr[mid],arr[h]=arr[h],arr[mid]
#             h-=1
#     return arr
# arr=[0,1,0,1,2,0,1,2,0]
# n=len(arr)
# print(sort0s1s2s(arr,n))

# merge overlapping intervals


# 1 4 , 3 6 , 6 10 , 11 18 , 18 1000
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# a.sort()
# m1=a[0][0]
# m2=a[0][1]
# for i in range(1,n):
#     if (a[i][0]<=m2  and a[i][1]>=m2):
#         m1 = min(a[i][0],m1)
#         m2 = max(a[i][1],m2)
#     else:
#         print(m1,m2)
#         m1=a[i][0]
#         m2=a[i][1]
# print(m1,m2)


# meeting maximum guests
# def maxguest(arr,n,dep):
#     i=1;j=0;count=1;res=1
#     arr.sort()
#     dep.sort()
#     while(i<n and j<n):
#         if(arr[i]<=dep[j]):
#             count+=1
#             i+=1
#         else:
#             j+=1
#             count-=1
#         res=max(res,count)
#     return res
# arr=[10,12,20]
# dep=[20,25,30]
# n=3
# print(maxguest(arr,n,dep))


# counting sort
# def countingSort(arr,n,k):
#     c=[0]*k
#     for i in range(n):
#         c[arr[i]]+=1
#     index=0
#     for i in range(k):
#         for _ in range(c[i]):
#             arr[index]=i
#             index+=1
#     return arr
# a=[5,4,3,2,1]
# k=6
# n=len(a)
# print(countingSort(a,n,k))


# Radix Sort
# def countingSort(arr,n,exp):
#     c=[0]*10
#     op=[0]*n
#     for j in range(n):
#         index = arr[j]//exp
#         c[int(index)%10]+=1
#     for k in range(1,10):
#         c[k]+=c[k-1]
#     i=n-1
#     while(i>=0):
#         index=arr[i]//exp
#         op[c[int(index%10)]-1]=arr[i]
#         c[int(index%10)]-=1
#         i-=1
#     i=0
#     for i in range(n):
#         arr[i]=op[i]

# def RadixSort(arr,n):
#     mx = max(arr)
#     exp=1
#     while (mx//exp)>0:
#         countingSort(arr,n,exp)
#         exp*=10
#     return arr
# a=[312,212,5,90,787]
# n=len(a)
# print(RadixSort(a,n))


# merge 2 sorted arrays

# def mergeSorted(a,b,n,m):
#     i=0
#     j=0
#     x=[]
#     while(i<n and j<m):
#         if(a[i]<b[j]):
#             x.append(a[i])
#             i+=1
#         else:
#             x.append(b[j])
#             j+=1

#     while(i<n):
#         x.append(a[i])
#         i+=1
#     while(j<m):
#         x.append(b[j])
#         j+=1
#     print(x)
# a=[1,3,4]
# b=[1,2,3]
# mergeSorted(a,b,len(a),len(b))

# def mergeSort(a,l,h):
#     if(h>l):
#         m=(l+h)//2
#         mergeSort(a,l,m)
#         mergeSort(a,m+1,h)
#         mergefun(a,l,h,m)

# def mergefun(a,l,h,m):
#     n1=m-l+1
#     n2=h-m
#     x=a[l:m+1]
#     y=a[m+1:h+1]
#     i=0
#     j=0
#     k=l
#     while(i<n1 and j<n2):
#         if(x[i]<=y[j]):
#             a[k]=x[i]
#             k+=1
#             i+=1
#         else:
#             a[k]=y[j]
#             k+=1
#             j+=1
#     while(i<n1):
#         a[k]=x[i]
#         k+=1
#         i+=1
#     while(j<n2):
#         a[k]=y[j]
#         k+=1
#         j+=1

# arr=[1,5,7,9,3,2]
# l=0
# h=5
# mergeSort(arr,l,h)
# print(arr)
