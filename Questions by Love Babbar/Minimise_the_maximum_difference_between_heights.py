#Minimise the maximum difference between heights [V.IMP]
# def Minimise_the_maximum_difference_between_heights(arr, k, size):
#     a=[]
#     maxarr=max(arr)
#     difference=maxarr-k
#     for i in range(n):
#         b=arr[i]+k
#         if(b<difference):
#             a.append(b)
#         else:
#             a.append(arr[i]-k)
#     return (max(a)-min(a))
# arr=[3, 9, 12, 16, 20]
# k=3
# n=5
# print(Minimise_the_maximum_difference_between_heights(arr,k,n))


def getMinDiff(self,a,n,k):
        mini=min(a)
        maxi=max(a)
        if ((maxi-mini)<=k):
            return (maxi-mini)
        else:
            for i in range(n):
                if a[i]-mini>maxi-a[i]:
                    a[i]-=k
                else:
                    a[i]+=k
            return (maxi-mini)


arr=[1,5,8,10]
k=2
n=4
ans = (getMinDiff(arr,n,k))
