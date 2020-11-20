# Array Subset of another array

for _ in range(int(input())):
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for i in range(len(b)):
        if b[i] in a:
            c+=1
    if(c==len(b)):
        print("Yes")
    else:
        print("No")
