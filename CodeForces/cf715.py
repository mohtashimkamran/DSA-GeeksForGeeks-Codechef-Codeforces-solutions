for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    x=[]
    for i in arr:
        if i%2!=0:
            x.append(i)
    for i in arr:
        if i%2==0:
            x.append(i)
    print(*x)