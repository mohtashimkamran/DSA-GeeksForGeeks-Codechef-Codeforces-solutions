# smallest positive missing no
def missingNumber(arr,n):
    poss = [x for x in arr if x > 0]
    if poss:
        if poss == list(range(1,n+1)):
            return max(poss)+1
        else:
            max_poss = max(poss)
            total_range = list(range(1,max_poss+1))
            missingNumbers = set(total_range) - set(poss)
            return min(missingNumbers)
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
print(missingNumber(a,n))
# arr=list(map(int,input().split()))
# x=[]
# for i in range(len(arr)):
#     arr.reverse()
#     x.append(arr[0])
#     arr.remove(arr[0])
# arr=x
# print(arr)
# def arry(a,n):
#     global arr
#     x=[]
#     j=0
#     for i in range(len(a)):
#         a.reverse()
#         x.append(a[0])
#         a.remove(a[0])
#         j+=i
#     arr=x
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# arry(arr,n)
# print(arr)