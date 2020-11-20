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