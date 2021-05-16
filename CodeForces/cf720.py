for _ in range(int(input())):
    a,b=map(int,input().split())
    x=y=z=0
    if b==1:
        print("NO")
    else:
        s=a*b*2
        y=s-a
        print("YES")
        print(a,y,s)