# for _ in range(int(input())):
#     r,b,d=map(int,input().split())
#     if r==b and abs(r-b)<=d:
#         print("YES")
#     elif (abs(r-b)<=min(r,b)*d):
#         print('YES')
#     else:
#         print("NO")

for _ in range(int(input())):
    x,y,k=map(int,input().split())
    i=j=1
    c=0
    while(i<x):
        i+=1
        c+=j
    while(j<y):
        j+=1
        c+=i
    # print(c)
    if c==k:
        print("YES")
    else:
        print("NO")