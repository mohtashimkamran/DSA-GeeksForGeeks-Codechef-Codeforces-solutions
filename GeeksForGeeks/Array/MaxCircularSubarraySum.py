# Max Circular subarray sum
def kedane(arr,n):
    max_so_far=arr[0]
    current_max=arr[0]
    for i in range(1,n):
        current_max=max(arr[i],current_max+arr[i])
        max_so_far=max(max_so_far,current_max)
    return max_so_far
n=int(input())
arr=list(map(int,input().split()))
normal_sum_max_subarray=kedane(arr,n)
sum_of_array=sum(arr)
# print(normal_sum_max_subarray,sum_of_array)
invertedarry=[-x for x in arr]
# print(invertedarry)
invertedarray_kedane=kedane(invertedarry,n)
max_circular_subarray_sum = sum_of_array+invertedarray_kedane
# print(sum_of_array,max_circular_subarray_sum,normal_sum_max_subarray)
if (max_circular_subarray_sum>0):
    print(max(normal_sum_max_subarray,max_circular_subarray_sum))
else:
    print(normal_sum_max_subarray)
