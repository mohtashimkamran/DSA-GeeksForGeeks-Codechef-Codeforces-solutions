# arr=[51,54,55,65]
# n=100
# low=0
# high=len(arr)-1
# while(low<high):
#     mid = (low+high)//2
#     if(n==arr[mid]):
#         print(mid)
#         break
#     elif(n>arr[mid]):
#         low = mid+1
#     elif(n<arr[mid]):
#         high=mid-1
# else:
#     print(-1)


# def binary(arr,n,low,high,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if (x==arr[mid]):
#         return mid
#     elif(x<arr[mid]):
#         return binary(arr,n,low,mid-1,x)
#     else:
#         return binary(arr,n,mid+1,high,x)
# arr=[1,2,3,4,5,6]
# n=6
# x=5
# print(binary(arr,n,0,n-1,x))


#indexof 1st occured no if multiple same no is present in list
# def first(arr,low,high,n,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if(x>arr[mid]):
#         return first(arr,mid+1,high,n,x)
#     elif(x<arr[mid]):
#         return first(arr,low,mid-1,n,x)
#     else:
#         if(mid==0 or arr[mid]!=arr[mid-1]):
#             return mid
#         else:
#             return first(arr,low,mid-1,n,x)
# arr=[1,2,2,4,5,6]
# n=6
# x=2
# print(first(arr,0,n-1,n,x))

#index of last occured elemenet in array
# def last(arr,low,high,n,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if(x>arr[mid]):
#         return last(arr,mid+1,high,n,x)
#     elif(x<arr[mid]):
#         return last(arr,low,mid-1,n,x)
#     else:
#         if(mid==n-1 or arr[mid]!=arr[mid+1]):
#             return mid
#         else:
#             return last(arr,mid+1,high,n,x)
# arr=[1,2,2,4,5,6,6,6,6]
# n=9
# x=6
# print(last(arr,0,n-1,n,x))


# def countones(arr,low,high,n,x):
#     return n-first(arr,0,n-1,n,x)

# def first(arr,low,high,n,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if(x>arr[mid]):
#         return first(arr,mid+1,high,n,x)
#     elif(x<arr[mid]):
#         return first(arr,low,mid-1,n,x)
#     else:
#         if(mid==0 or arr[mid]!=arr[mid-1]):
#             return mid
#         else:
#             return first(arr,low,mid-1,n,x)
# arr=[0,0,0,1,1,1]
# n=6
# x=1
# print(countones(arr,0,n-1,n,1))

# def count(arr,low,high,n,x):
#     if first(arr,0,n-1,n,x) ==-1:
#         return -1
#     return last(arr,0,n-1,n,x)-first(arr,0,n-1,n,x)+1

# def last(arr,low,high,n,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if(x>arr[mid]):
#         return last(arr,mid+1,high,n,x)
#     elif(x<arr[mid]):
#         return last(arr,low,mid-1,n,x)
#     else:
#         if(mid==n-1 or arr[mid]!=arr[mid+1]):
#             return mid
#         else:
#             return last(arr,mid+1,high,n,x)
# def first(arr,low,high,n,x):
#     if low>high:
#         return -1
#     mid = (low+high)//2
#     if(x>arr[mid]):
#         return first(arr,mid+1,high,n,x)
#     elif(x<arr[mid]):
#         return first(arr,low,mid-1,n,x)
#     else:
#         if(mid==0 or arr[mid]!=arr[mid-1]):
#             return mid
#         else:
#             return first(arr,low,mid-1,n,x)
# arr=[1,2,2,4,5,6,6,6,6]
# n=9
# x=3
# print(count(arr,0,n-1,n,x))


# n=input()
# for i in range(len(n)):
#     for j in range(i+1,len(n)+1):
#         print([n[i:j]],end=" ")

#http://www.geeksforgeeks.org/count-1s-sorted-binary-array

# def countones(arr,n):
#     low=0
#     high=n-1
#     while(low<=high):
#         mid=(low+high)//2
#         if ((mid==high) or arr[mid+1]==0) and (arr[mid]==1):
#             return mid+1
#         elif(arr[mid]<1):
#             high = mid-1
#         else:
#             low = mid+1
#     return 0    
# arr=[0,0,0]
# n=len(arr)
# print(countones(arr,n))

#two pointer approach
#given a sorted array and a sum find if there is any pair with given sum

# def pairSum(arr,n,x):
#     left=0
#     right=n-1
#     while(left<right):
#         if(arr[left]+arr[right]==x):
#             print(arr[left],arr[right])
#             return
#         elif(arr[left]+arr[right]>x):
#             right-=1
#         else:
#             left+=1
#     print(-1)
#     return

# arr=[1,3,5,8,9]
# n=len(arr)
# x=17
# pairSum(arr,n,x)

#given an unsorted array and a sum find if there is any pair with given sum

# def unsortedPairSum(arr,x):
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if (arr[i]+arr[j]==x):
#                 print(arr[i],arr[j])
#                 return
#     return -1
# arr=[1,4,3,2,9,7]
# x=16
# unsortedPairSum(arr,x)


#two pointer approach
# given a sorted array and a sum count total pairs of given sum
# def pairSum(arr,n,x):
#     left=0
#     right=n-1
#     count=0
#     while(left<right):
#         if(arr[left]+arr[right]==x):
#             # return (arr[left],arr[right])
#             count+=1
#             right-=1
#             left+=1
#             # return count
#         elif(arr[left]+arr[right]>x):
#             right-=1
#         else:
#             left+=1
#     return count

# arr=[1,2,3,4,5,6,7]
# n=len(arr)
# x=5
# print(pairSum(arr,n,x))

# def pairSum(arr,x):
#     left=0
#     n=len(arr)
#     right=n-1
#     count=0
#     while(left<right):
#         if(arr[left]+arr[right]==x):
#             # return (arr[left],arr[right])
#             count+=1
#             right-=1
#             left+=1
#             # return count
#         elif(arr[left]+arr[right]>x):
#             right-=1
#         else:
#             left+=1
#     return count


# arr=[0,1,2,3,4,5,6,7,8,9,10]
# x=10
# n=len(arr)
# count=0
# for i in range(len(arr)-3):
#     count+=pairSum(arr[i+1:],x-arr[i])
# print(count)



# # # function to find median of array
# def findMedianSortedArrays(arr1, n1, arr2, n2):
#     c= arr1+arr2
#     c.sort()
#     med=(len(c)-1)//2
#     if(len(c)%2):
#         return c[med]
#     return (c[med]+c[med+1])//2

	
# # Driver code

# a=[1]*10000000
# b=[4]*10000000
# n = len(a)
# c=int(getMedian(a,b,n))
# e=time.time()
# print(c)
# print(e-s)
# # 0.31203579902648926
##  0.4773437976837158


# Majority Lement in an array
# def majority(arr,n):
#     res=0
#     count=1
#     for i in range(1,n):
#         if(arr[res]==arr[i]):
#             count+=1
#         else:
#             count-=1
#         if(count==0):
#             res=i
#             count=1
#     count=0
#     for i in range(n):
#         if(arr[res]==arr[i]):
#             count+=1
#     if(count<=(n//2)):
#         res=-1
#     return res
# arr=[8,8,1,2,8]
# n=len(arr)
# print(majority(arr,n))


#efficient approach for repeated elements
# a=[1,2,3,3,4,4]
# arr=[False]*len(a)
# for i in range(len(a)):
#     if arr[a[i]]==True:
#         print(a[i])
#     arr[a[i]]=True


#Allocate minimum number of pages 
#wrong sollution
# a=[12,34,67,90]
# a=[15,17,20]
# 250 : 74 + 159 : 181 : 23 : 45+129 : 174
# a=[10,5,30,1,2,5,10,10]
# m=int(input())
# for i in range(m-1):
#     # print(a[i])
#     c=max(a)
#     a.remove(c)
# print(sum(a))

#Allocate minimum number of pages 
#naive sollution
# def minpage(arr,n,k):
#     if (k==1):
#         return sum(arr[0:n])
#     if (n==1):
#         return arr[0]
#     res = 1000000000000
#     for i in range(1,n):
#         res = min(res,max(minpage(arr,i,k-1),sum(arr[i:n])))
#     return res
# a=[250,74,159,181,23,45,129,174]
# n=len(a)
# k=6
# print(minpage(a,n,k))

# def minpage(arr,n,k):
#     sm=sum(arr);mx=max(arr)
    
#     low = mx;high=sm;res=0
#     while(low<=high):
#         mid=(low+high)//2
#         if (ispheasible(arr,n,k,mid)):
#             res=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return res

# def ispheasible(arr,n,k,ans):
#     req=1;sum=0
#     for i in range(n):
#         if(sum+arr[i]>ans):
#             req+=1
#             sum=arr[i]
#         else:
#             sum+=arr[i]
#     return (req<=k)
# a=[250,74,159,181,23,45,129,174]
# n=len(a)
# k=6
# print(minpage(a,n,k))


#subarray with a given sum

