#Find longest coinsecutive subsequence
a=[2,6,1,9,4,5,3]
n=7
x=a
c=0
for i in range(n):
    if (a[i]-1 not in x):
        j=a[i]
        while j in x:
            j+=1
        c=max(c,j-a[i])
print(c)
    