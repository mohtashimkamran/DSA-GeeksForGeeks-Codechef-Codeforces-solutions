# Max And Min Element
a=[1,3,4,5]
print(max(a))
print(min(a)).

a=[5,4,3,2,0,1]
a.sort()
mx=a[0]
mn=a[-1]
print(mx,mn)


def max(a,n):
    x=a[0]
    # for i in range(1,n):
    #     if(a[i]>x):
    #         x=a[i]
    # return x
    for i in range(1,n):
        x=min(a[i],x)
    return x

print(max([1,2,30],3))