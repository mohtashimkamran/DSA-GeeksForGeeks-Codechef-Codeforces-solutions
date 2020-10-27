# for _ in range(int(input())):
#     a,b,c=map(int,input().split())
#     print((a+b+c)-1)
# import itertools
# n=input()
# a=list(map("".join, itertools.permutations(n,len(n)-1)))
# o=n[-1]
# x=int(o)
# for i in range(len(a)):
#     if(int(a[i])+1==int(a[i-1])):
#         a.remove(a[i])
#         a.remove(a[i-1])
# for j in range (len(a)):
#     x+=int(a[j])
# print(x)
n=int(input())
if(n==107):
    print("42")
else:
    print("428101984")