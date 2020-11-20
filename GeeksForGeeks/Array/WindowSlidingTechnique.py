#window sliding technique 
#naive sollution
n=[1,8,30,-5,20,7]
k=3
max_sum = -100000000
for i in range(0,len(n)-k):
    sum=0
    for j in range(0,k):
        sum+=n[i+j]
    max_sum=max(sum,max_sum)
print(max_sum)

# efficient
arr=[1,8,30,-5,20,7]
cur_sum=0
k=3
for i in range(k):
    cur_sum+=arr[i]
print(cur_sum)
max_sum = cur_sum
for i in range(k,len(arr)):
    cur_sum+=(arr[i]-arr[i-k])
    max_sum=max(max_sum,cur_sum)
print(max_sum)