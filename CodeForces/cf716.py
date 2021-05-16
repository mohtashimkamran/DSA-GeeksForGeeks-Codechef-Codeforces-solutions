import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    flag="NO"
    for s in arr:
        if math.sqrt(s)!=int(math.sqrt(s)):
            flag="YES"
            break
    print(flag)       