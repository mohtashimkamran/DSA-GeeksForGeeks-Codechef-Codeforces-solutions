#minimum group flips to make same
n=[1,0,1,0,0,0,0,1]
count=0
for i in range(1,len(n)):
    if(n[i]!=n[i-1]):
        if(n[i]!=n[0]):
            print(i)
            count+=1
        else:
            print(i-1)
if(n[i]!=n[0]):
    print(len(n)-1)    
print(count)
