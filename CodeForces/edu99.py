# for _ in range(int(input())):
#     n=input()
#     print(len(n))

# n=int(input())
# s=1
# count=1
# for i in range(1,n+1):
#     s+=i
#     if (n-s)>=(i+1):
#         x=n-(i+1)
#         s=x
#         count+=(s-x)
#     else:
#         s+=i
#         count+=1
# print(count,s)

for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a==b):
        a=a-1
        print(a,b)
    else:
        a=a-1
        print(a,b)