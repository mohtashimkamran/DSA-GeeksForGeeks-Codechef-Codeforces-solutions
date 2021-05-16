import math
for _ in range(int(input())):
    n,m,x=map(int,input().split())
    a=math.ceil(x/n)
    b=x%n
    if b!=0:
        print((m*b)-(m-a))
    else:
        print((m*n)-(m-a))
