for _ in range(int(input())):
    n=int(input())
    if n<2050:
        print(-1)
    elif(n%2050!=0):
        print(-1)
    else:
        x=n//2050
        c=0
        while(x!=0):
            a=x%10
            c+=a
            x=x//10
        print(c)