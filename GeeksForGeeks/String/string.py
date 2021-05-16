# a=input()
# # print(ord(a))
# for i in a:
#     print(ord(i))


#print frequencies of characters in sorted manner of a string


# n=input()
# arr=[]
# for i in n:
#     arr.append(i)
# a = set(arr)
# a=sorted(a)
# b={}
# for i in a:
#     b[i]=0
# for i in arr:
#     b[i]+=1
# print(b)

#leftmost repeating character in string
# a=input()
# arr=[False]*256
# res=-1
# for i in range(len(a)-1,-1,-1):
#     if arr[a.index(a[i])]==False:
#         arr[a.index(a[i])]=True
#     else:
#         res=i
# print(a[res])

#leftmost non repeating character

# n=input()
# for i in range(len(n)):
#     flag=0
#     for j in range(len(n)):
#         if (i!=j and n[i]==n[j]):
#             flag=1
#             break
#     if flag==0:
#         print(n[i])
#         break

#efficient

# a=input()
# arr=[0]*256
# for i in a:
#     arr[ord(i)]+=1
# for i in a:
#     if arr[ord(i)]==1:
#         print(i)
#         break


#reverse the words in string 
#naive
# a='i love coding'
# arr=a.split(" ")
# arr.reverse()
# print(arr)


# def pattersearch(s,p):
#     n=len(s)
#     m=len(p)
#     i=0
#     while i<=(n-m):
#         for j in range(0,m):
#             if (s[i+j]!=p[j]):
#                 break
#             j+=1
#         if j==m:
#             print(i)
#             i+=m
#         elif(j==0):
#             i+=1
#         else:
#             i+=j
# n=input()
# p=input()
# pattersearch(n,p)

# n=input()
# p=input()
# ps=0
# x=len(p)
# for i in p:
#     ps+=ord(i)
# l=0
# for j in range(len(n)-x+1):
#     z=[]
#     ns=0
#     for k in range(l,x):
#         ns+=ord(n[k])
#         z.append(n[k])
#     if(ns==ps and z==list(p)):
#         print(j)
#         l+=1
#         x+=1
#     else:
#         l+=1
#         x+=1

# def fillps(s):
#     n=len(s)
#     arr=[0]*n
#     i=1
#     l=0
#     while (i<n):
#         if s[i]==s[l]:
#             l+=1
#             arr[i]=l
#             i+=1
#         else:
#             if l==0:
#                 arr[i]=0
#                 i+=1
#             else:
#                 l=arr[l-1]
#     return arr
# s=input()
# print(fillps(s))

# def pattersearch(s,p):
#     n=len(s)
#     m=len(p)
#     i=0
#     while i<=(n-m):
#         for j in range(0,m):
#             if (s[i+j]!=p[j]):
#                 break
#             j+=1
#         if j==m:
#             print(i)
#             print("YES")
#             i+=m
#         elif(j==0):
#             i+=1
#         else:
#             i+=j
# n=input()
# n=n+n
# p=input()
# pattersearch(n,p)


#search an anagram


# n=input()
# p=input()
# arr=[0]*256
# lrr=[0]*256


# for i in range(len(p)):
#     arr[ord(n[i])]+=1
#     lrr[ord(p[i])]+=1

# if lrr==arr:
#     print("yes")
# for i in range(len(p),len(n)):
#     if arr==lrr:
#         print("True")
#         break
#     else:
#         arr[ord(n[i])]+=1
#         arr[ord(n[i-len(p)])]-=1


#find the longest substring having distinct characters
#On2 solutiuon

# def longestSubstring(s):
#     n=len(s)
#     res=0
#     for i in range(n):
#         arr=[0]*256
#         for j in range(i,n):
#             if(arr[ord(s[j])]==True):
#                 break
#             else:
#                 res=max(res,j-i+1)
#                 arr[ord(s[j])]=True
#         arr[ord(s[i])]=False
#     return res
# s=input()
# print(longestSubstring(s))

#efficient On solution

# def longestSubstring(s):
#     n=len(s)
#     arr=[-1]*256
#     r=0
#     i=0
#     for j in range(n):
#         i=max(i,arr[ord(s[j])]+1) #if any repeating element found we move to next index
#         maxIn = j-i+1    #we store the max no of disctinct characters everytime we encounter any same value 
#         r=max(r,maxIn)   #update r as we find any other count of disctinct characters greater than previous
#         arr[ord(s[j])]=j
#     return r
# s=input()
# print(longestSubstring(s))


#Lexicographical rank of a string

# import math
# n=input()
# arr=[0]*256
# x=len(n)
# f=math.factorial(x)
# res=1
# for i in range(len(n)):
#     arr[ord(n[i])]+=1
# # print(arr)

# for i in range(len(arr)):
#     arr[i]+=arr[i-1]
# # print(arr)

# for i in range(x-1):
#     f=f//(x-i)
#     res=res + (arr[ord(n[i])-1]*f)
#     for j in range(ord(n[i]),len(arr)):
#         arr[j]-=1
# print(res)


#leftmost repeating no

# s=input()
# arr=[0]*256
# res=0
# for i in range(len(s)-1,0,-1):
#     if arr[ord(s[i])]==1:
#         res=i
#     else:
#         arr[ord(s[i])]==1
# print(s[res])

#Sort charaacters on the basis of their frequency
# from collections import Counter
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # arr=list(s.split())
#         # return arr
#         arr=[]
#         for i in s :
#             arr.append(i)
#         arr.sort(reverse=True)
#         c=Counter(arr)
#         a=sorted(arr,key=c.get,reverse=True)
#         return a