
#EQUILIBIRUIM POINT
def quili(A,N):
    if N==1:
        return 1
    leftsum=0
    s=sum(A)
    for i in range(N):
        s-=A[i]
        if s == leftsum:
            return i+1
        leftsum+=A[i]
    return -1
n=int(input())
a=list(map(int,input().split()))
print(quili(a,n))
