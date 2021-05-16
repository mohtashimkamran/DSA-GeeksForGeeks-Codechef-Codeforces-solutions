# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     s=set(arr)
#     for i in s:
#         x=0
#         m=0
#         p=10**5
#         while x<n:
#             if arr[x]==i:
#                 x+=1
#                 # m+=1
#             else:
#                 x+=k
#                 m+=1
#         p=min(p,m)
#     print(p)

for _ in range(int(input())):
    n,k=map(int,input().split())
    houses = list(map(int, input().split()))
    colors = set(houses)
    days= n
    for c in colors:
        i = 0
        d = 0
        while True:
            if i >= n:
                break
            if houses[i] == c:
                i += 1
            else:
                i += k
                d += 1

        days= min(d, days)
    print(days)