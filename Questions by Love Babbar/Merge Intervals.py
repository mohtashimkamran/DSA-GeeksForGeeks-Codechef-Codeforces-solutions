# Merge Intervals
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()
m1=a[0][0]
m2=a[0][1]
for i in range(1,n):
    if(a[i][0]<=m2 and a[i][1]>=m2):
        m1=min(a[i][0],m1)
        m2=max(a[i][1],m2)
    else:
        print(m1,m2)
        m1=a[i][0]
        m2=a[i][1]
print(m1,m2)