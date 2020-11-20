#efficient approach for repeated elements
# a=[1,2,3,3,4,4]
# arr=[False]*len(a)
# for i in range(len(a)):
#     if arr[a[i]]==True:
#         print(a[i])
#     arr[a[i]]=True

def findRepeating(a,n):
    x=[]
    arr=[False]*len(a)
    for i in range(len(a)):
        if arr[a[i]]==True:
            x.append(a[i])
        arr[a[i]]=True
    return x

a=[1,2,3,3,4,4]
n=len(a)
ans =findRepeating(a,n)
print(ans[0],ans[1])