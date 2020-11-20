# Next Permutation
def nextPermutation(n,arr):
    i = j = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:   # elemenets are in descending order
        arr.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while arr[j] <= arr[k]:
        j -= 1
    arr[k], arr[j] = arr[j], arr[k]  
    l, r = k+1, len(arr)-1  # reverse the second part
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l +=1 ; r -= 1
    return arr
n=3
arr=[1,2,3]
print(nextPermutation(n,arr))
