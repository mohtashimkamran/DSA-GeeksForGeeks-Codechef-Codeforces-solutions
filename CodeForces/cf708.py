# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     arr.sort()
#     x=set(arr)
#     arr=arr[::-1]
#     # print(arr)
#     a=list(x)
#     for i in x:
#         c=arr.count(i)
#         if c>1:
#             b=i
#             for i in range(c-1):
#                 a.append(b)
#     print(*a)
