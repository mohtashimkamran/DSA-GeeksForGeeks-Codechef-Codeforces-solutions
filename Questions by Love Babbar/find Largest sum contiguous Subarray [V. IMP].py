# find Largest sum contiguous Subarray [V. IMP]
def Largest_sum_contiguous_Subarray(arr,n):
    curm=arr[0]
    maxsf=arr[0]
    for i in range(1,n):
        curm=max(arr[i],curm+arr[i])
        maxsf=max(curm,maxsf)
    return maxsf
a=[-1,-2,-3,-4]
n=len(a)
print(Largest_sum_contiguous_Subarray(a,n))