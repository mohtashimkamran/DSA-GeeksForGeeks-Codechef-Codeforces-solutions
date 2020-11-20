#given a fixed array and multiple queries of foloowng types on the array 
#how to efficiently erform opeartions
#0n time
# arr=[1,2,3,4,5]
# prefix_sum = [1]
# for i in range(1,len(arr)):
#     prefix_sum.append(prefix_sum[i-1]+arr[i])
# print(prefix_sum)

# def equilibrium(arr,n):
#     sum=0
#     for i in range(n):
#         sum+=arr[i]
#     left_sum=0
#     for i in range(n):
#         if left_sum==sum-arr[i]:
#             return True
#         left_sum+=arr[i]
#         sum-=arr[i]
#     return False

