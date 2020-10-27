
def merge(a):
    if len(a) > 1:
        global c
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <=R[j]:
                a[k] = L[i]
                i += 1

            else:
                a[k] = R[j]
                j += 1
                
                c += len(L) - i

            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
for _ in range(int(input())):
    c = 0
    n=int(input())
    list = [int(x) for x in input().split()]
    b=int(((n*(n-1))/2)-1)
    merge(list)
    if(c<=b):
        print("YES")
    else:
        print("NO")