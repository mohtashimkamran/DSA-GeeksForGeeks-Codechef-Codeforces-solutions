# even first then odd
a=[12,5,2,7]
x=[]
y=[]
for i in range(len(a)):
    if (a[i]%2==0):
        x.append(a[i])
    else:
        y.append(a[i])
print(x+y)