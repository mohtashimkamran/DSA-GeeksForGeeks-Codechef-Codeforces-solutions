import math
for _ in range(int(input())):
    n=int(input())
    x=n
    sumn=sum([int(i) for i in str(n)])
    y=math.gcd(x,sumn)
    while(y==1):
        n=n+1
        x=n
        sumn=sum([int(i) for i in str(n)])
        y=math.gcd(x,sumn)
    print(n)