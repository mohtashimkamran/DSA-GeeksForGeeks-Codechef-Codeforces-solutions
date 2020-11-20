#rotate an array by d elements
# def rotate(arr,n,d):
#     reverse(arr,0,d-1)
#     reverse(arr,d,n-1)
#     reverse(arr,0,n-1)
#     return arr
# def reverse(arr,low,high):
#     while(low<high):
#         temp=arr[low]
#         arr[low]=arr[high]
#         arr[high]=temp
#         low+=1
#         high-=1

# arr=[1,2,3,4,5]
# n=5
# d=2
# print(rotate(arr,n,d))

# a=[1,2,3,4]
# n=len(a)
# d=2
# for i in range(d):
#     a.insert(0, 0)
# j = -1
# for i in range(d-1,-1,-1):
#     a[j],a[i]=a[i],a[j]
#     j-=1
# print(a[:n])

