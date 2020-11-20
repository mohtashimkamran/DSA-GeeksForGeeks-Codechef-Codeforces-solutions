
def ins(a,i,m):
    c=i%m
    if a[c]==0:    
        z=[i]
        a[c]=z
    else:
        a[c].append(i)
        # print(a[c])


def dele(a,k,m):
    c=k%m
    if k in a[c]:
        a[c].remove(k)
    else:
        print("NOT hai")


ele=[70,71,29,28,35,34]
m=7
arr=[0]*m
for i in ele:
    ins(arr,i,m)
print(arr)

# k=29

# dele(arr,k,m)
# print(arr)
