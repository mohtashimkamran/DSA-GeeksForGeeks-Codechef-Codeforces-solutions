c=""
def lcs(x, y, m, n): 
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]: 
        global c
        c+=x[m-1] 
        return 1 + lcs(x, y, m-1, n-1)
    else: 
        return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))
X = input()
Y = input()
print("Length",lcs(X , Y, len(X), len(Y)))
print(c[:lcs(X , Y, len(X), len(Y))])