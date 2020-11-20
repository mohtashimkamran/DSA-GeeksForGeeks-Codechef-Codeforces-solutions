# Reverse the Array
# a=[1,4,3,2,1]
# a.reverse()
# print(a)

# a=[1,2,3,4,5]
# print(a[::-1])

# reverse a number
# a=123
# while a!=0:
#     n=a%10
#     a=a//10
#     print(n,end="")


# Max And Min Element
# a=[1,3,4,5]
# print(max(a))
# print(min(a)).

# a=[5,4,3,2,0,1]
# a.sort()
# mx=a[0]
# mn=a[-1]
# print(mx,mn)


# def max(a,n):
#     x=a[0]
#     # for i in range(1,n):
#     #     if(a[i]>x):
#     #         x=a[i]
#     # return x
#     for i in range(1,n):
#         x=min(a[i],x)
#     return x

# print(max([1,2,30],3))

# kth Max
# b=[1,1,2,5,6,7]
# a=list(set(b))
# print(a)
# k=2
# for i in range(k-1):
#     # print(min(a),max(a))
#     a.remove(min(a))
#     a.remove(max(a))
# print(min(a))
# print(max(a))


# def lomuto(a,n,h):
#     l=0
#     p=h
#     j=l-1
#     for i in range(l,h):
#         if(a[i]<a[p]):
#             j+=1
#             a[j],a[i]=a[i],a[j]
#     a[j+1],a[h]=a[h],a[j+1]
#     return j+1
# def kthSmallest(a,n,h,k):
#     l=0
#     while(l<=h):
#         p=lomuto(a,n,h)
#         if(p==(k-1)):
#             return a[p]
#         elif(p>(k-1)):
#             h=p-1
#         else:
#             l=p+1
# a=[1,2,4,9,3]
# n=len(a)
# h=n-1
# k=2
# print(kthSmallest(a,n,h,k))

# kth Max
# def lomuto(a,n,h):
#     l=0
#     p=h
#     j=l-1
#     for i in range(l,h):
#         if(a[i]>a[p]):
#             j+=1
#             a[j],a[i]=a[i],a[j]
#     a[j+1],a[h]=a[h],a[j+1]
#     return j+1
# def kthMax(a,n,h,k):
#     l=0
#     while(l<=h):
#         p=lomuto(a,n,h)
#         if(p==(k-1)):
#             return a[p]
#         elif(p>(k-1)):
#             h=p-1
#         else:
#             l=p+1
# a=[1,2,4,9,3]
# n=len(a)
# h=n-1
# k=2
# print(kthMax(a,n,h,k))

# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# def sortOs1s2s(arr,n):
#     l=0
#     mid=0
#     h=n-1
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
# arr=[1,0,2,0,1,2]
# n=len(arr)
# print(sortOs1s2s(arr,n))

# Move all the negative elements to one side of the array 

# def moveNegative(arr,n):
#     # h=n-1
#     l=0
#     k=l-1
#     for i in range(n):
#         if(arr[i]<0):
#             k+=1
#             arr[k],arr[i]=arr[i],arr[k]
#     return arr
# arr=[1,-3,9,8,-5,-6]
# n=len(arr)
# print(moveNegative(arr,n))

# Find the Union and Intersection of the two sorted arrays.

# a=[1,2,3,4,5]
# b=[1,2,3]
# print(set(a+b))

# a=set([1,2,3,4,5])
# b=set([1,2,3])
# print(a.intersection(b))

# Write a program to cyclically rotate an array by one.

# a=[1,2,3,4]
# n=len(a)
# #insert 0 at first index
# a.insert(0, 0)
# a[-1],a[0]=a[0],a[-1]
# print(a[:n])


#find Largest sum contiguous Subarray [V. IMP]
# def Largest_sum_contiguous_Subarray(arr,n):
#     curm=arr[0]
#     maxsf=arr[0]
#     for i in range(1,n):
#         curm=max(arr[i],curm+arr[i])
#         maxsf=max(curm,maxsf)
#     return maxsf
# a=[-1,-2,-3,-4]
# n=len(a)
# print(Largest_sum_contiguous_Subarray(a,n))

# #Minimise the maximum difference between heights [V.IMP]
# def Minimise_the_maximum_difference_between_heights(arr, k, size):
#     a=[]
#     maxarr=max(arr)
#     difference=maxarr-k
#     for i in range(n):
#         b=arr[i]+k
#         if(b<difference):
#             a.append(b)
#         else:
#             a.append(arr[i]-k)
#     return (max(a)-min(a))
# arr=[1,15,16]
# k=5
# n=3
# print(Minimise_the_maximum_difference_between_heights(arr,k,n))


# Minimum no. of Jumps to reach end of an array
# a=[1,3,5,8,9,2,6,7,6,8,9]
# a=[2,9,1,1,1,1,1]
# s=0
# i=0
# c=0
# while(i<=len(a)-1):
#     s+=a[i]
#     i+=s
#     c+=1
# print(c)


# find duplicate in an array of N+1 Integers
# a=[1,2,3,3,4,4]
# arr=[False]*len(a)
# for i in range(len(a)):
#     if arr[a[i]]==True:
#         print(a[i])
#     arr[a[i]]=True

# Merge 2 sorted arrays without using Extra space.
# a=[1,2,3,4]
# b=[0,1,2,3]
# a[:]=sorted(a+b)
# print(a)

# kedane's  algorithm
# def kedane(arr,n):
#     curm=arr[0]
#     maxm=arr[0]
#     for i in range(1,n):
#         curm=max(arr[i],curm+arr[i])
#         maxm=max(maxm,curm)
#     return maxm
# arr=[-1,-2,-3,-4]
# n=len(arr)
# print(kedane(arr,n))

# Count Inversion

# arr=[1,20,6,4,5]
# count=0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if((i<j and arr[i]>arr[j]) or (i>j) and (arr[i]<arr[j])):
#             count+=1
# print(count)
#Merge Intervals
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# a.sort()
# m1=a[0][0]
# m2=a[0][1]
# for i in range(1,n):
#     if(a[i][0]<=m2 and a[i][1]>=m2):
#         m1=min(a[i][0],m1)
#         m2=max(a[i][1],m2)
#     else:
#         print(m1,m2)
#         m1=a[i][0]
#         m2=a[i][1]
# print(m1,m2)

#Next Permutation
# def nextPermutation(n,arr):
#     i = j = len(arr)-1
#     while i > 0 and arr[i-1] >= arr[i]:
#         i -= 1
#     if i == 0:   # elemenets are in descending order
#         arr.reverse()
#         return 
#     k = i - 1    # find the last "ascending" position
#     while arr[j] <= arr[k]:
#         j -= 1
#     arr[k], arr[j] = arr[j], arr[k]  
#     l, r = k+1, len(arr)-1  # reverse the second part
#     while l < r:
#         arr[l], arr[r] = arr[r], arr[l]
#         l +=1 ; r -= 1
#     return arr
# n=3
# arr=[1,2,3]
# print(nextPermutation(n,arr))


#find all pairs on integer array whose sum is equal to given number
# l=0
# r=0
# def pairSum(arr,n,x):
#     left=0
#     n=len(arr)
#     right=n-1
#     count=0
#     global l
#     global r
#     while(left<right):
#         if(arr[left]+arr[right]==x):
#             # return (arr[left],arr[right])
#             count+=1
#             right-=1
#             left+=1
#             l=arr[left]
#             r=arr[right]
#             # return count
#         elif(arr[left]+arr[right]>x):
#             right-=1
#         else:
#             left+=1
#     return count
# arr=[1,2,3,4,5,6,7]
# n=len(arr)
# x=9
# print(pairSum(arr,n,x),l,r)




# Stock Buy and Sell
# def stockbuysell(arr):
#     lowestPrice=arr[0]
#     maxProfit=0

#     for i in arr:
#         if i<lowestPrice:
#             lowestPrice=arr[i]
        
#         if i>lowestPrice:
#             localMaxProfit=i-lowestPrice

#             if localMaxProfit>maxProfit:
#                 maxProfit=localMaxProfit
#     return maxProfit

# a=[7,1,5,3,6,4]
# print(stockbuysell(a))


# https://practice.geeksforgeeks.org/problems/common-elements1132/1
# find common in 3 sorted lists

# from itertools import groupby
# def common(a,b,c,n1,n2,n3):
#     i=j=k=0
#     x=[]
#     while(i<n1 and j<n2 and k<n3):
#         if(a[i]==b[j] and b[j]==c[k]):
#             # print(a[i])
#             x.append(a[i])
#             i+=1
#             j+=1
#             k+=1
#         elif(a[i]<b[j]):
#             i+=1
#         elif(b[j]<c[k]):
#             j+=1
#         else:
#             k+=1
#     c= (" ".join(str(x[0])for x in list(groupby(x))))
#     p=list(c.split())
#     return p
# ar1 = [1, 5, 10, 20, 40, 80] 
# ar2 = [6, 7, 20, 80, 100] 
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# n1=len(ar1)
# n2=len(ar2)
# n3=len(ar3)
# print(common(ar1,ar2,ar3,n1,n2,n3))


# subarray whose sum is 0
# def subArrayExists(arr,n):
#     s = set()

#     sum = 0
#     for i in range(n): 
#         sum += arr[i]

#         if sum == 0 or sum in s: 
#             return True
#         s.add(sum)

#     return False

# def subArraySum(arr, n, sum):
#     i = 1
#     start = 0
#     total = arr[0]
#     while i <= n:
#         while total > sum and start < i-1:
#             total = total - arr[start]
#             start += 1
#         if total == sum:
#             print (start+1, i,end ="")
#             return
#         if i < n:
#              total = total + arr[i]
#         i += 1
#     print(-1,end="")

# # a=[15, 2, 4, 8, 9, 5, 10, 23]
# # subArraySum(a,len(a),23)
# arr=[4,2,-3,1,6]
# n=len(arr)
# subArraySum(arr,n,0)
# n=len(a)

# max product subarray
# def maxproduct(arr,n):
#     if n==0:
#         return -1
#     if n==1:
#         return a[0]
#     ans=a[0]
#     max_p=a[0]
#     max_n=a[0]

#     for i in range(1,n):
#         c1=max_n*a[i]
#         c2=max_p*a[i]

#         max_n=min(a[i],c1,c2)
#         max_p=max(a[i],c1,c2)
#         ans=max(max_n,max_p)
#     return ans

# a=[6,-3,-10,0,2]
# n=5
# print(maxproduct(a,n))

# #Find longest coinsecutive subsequence
# a=[2,6,1,9,4,5,3]
# n=7
# x=a
# c=0
# for i in range(n):
#     if (a[i]-1 not in x):
#         j=a[i]
#         while j in x:
#             j+=1
#         c=max(c,j-a[i])
# print(c)
    


# given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/

# from collections import Counter 
# def majorityElement(self, a: List[int]) -> List[int]:
#     # a=[1,2,3,5,2]
#     # b=list(set(a))
#     # print(b)
#     k=(len(a)/3)
#     x=Counter(a)
#     # print(x)
#     y=[]
#     for i in range(len(a)):
#         if x[a[i]]>k:
#             y.append(a[i])
#     c=list(set(y))
#     return c


#Maximum profit by buying and selling a share atmost twice

# def maxProfit(price, n):
# 	profit = [0]*n
# 	max_price = price[n-1]

# 	for i in range(n-2, 0, -1):

# 		if price[i] > max_price:
# 			max_price = price[i]
# 		profit[i] = max(profit[i+1], max_price - price[i])
# 	min_price = price[0]

# 	for i in range(1, n):

# 		if price[i] < min_price:
# 			min_price = price[i]
# 		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))

# 	result = profit[n-1]

# 	return result

# a=[1,3,5,8,16]
# n=5
# print(maxProfit(a,n))


# Array Subset of another array

# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     c=0
#     for i in range(len(b)):
#         if b[i] in a:
#             c+=1
#     if(c==len(b)):
#         print("Yes")
#     else:
#         print("No")

#Triplet Array
# def twopint(arr,n,x):
#     # l=0
#     arr.sort()
#     c=0
#     # h=n-1
#     for i in range(0,n):
#         l=i+1
#         h=n-1
#         while(l<h):
#             if(arr[l]+arr[h]+arr[i]==x):
#                 c+=1
#                 l+=1
#                 h-=1
#             elif(arr[l]+arr[h]<x):
#                 l+=1
#             else:
#                 h-=1
#     if c>=1:
#         return 1
#     else:
#         return 0
# for _ in range(int(input())):
#     # a=[1,2,3,4,5]
#     n,x=map(int,input().split())
#     a=list(map(int,input().split()))
#     print(twopint(a,len(a),x))

t=int(input())
while(t>0):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    flag=0
    for i in range(0,n-2):
        l=i+1
        r=n-1
        while(l<r):
            x=arr[i]+arr[l]+arr[r]
            if(x==s):
                flag=1
                break
            elif(x<s):
                l+=1
            else:
                r-=1
        if(flag):
            break
    print(flag)
    t-=1