# Trapping Rain Water
def trappingWater(a,n):
    res = 0
    left_max = 0
    right_max = 0
    left = 0
    right = n - 1
    while left <= right:
        if a[left] <= a[right]:
            if left_max < a[left]:
                left_max = a[left]
            else:
                res += left_max - a[left]
            left += 1
        else:
            if right_max < a[right]:
                right_max = a[right]
            else:
                res += right_max - a[right]
            right -= 1
    return res

n=4
arr=[7,4,0,9]
print(trappingWater(arr,n))
