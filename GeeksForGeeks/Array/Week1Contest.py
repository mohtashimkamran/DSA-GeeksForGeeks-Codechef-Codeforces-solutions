#contest 1
#nearest perfect square
# import math
# for _ in range(int(input())):
#     n=int(input())
#     a=int(math.sqrt(n))
#     # print(a**2)
#     x=(a+1)**2
#     y=(a-1)**2
#     # print(x,y)
#     if(math.floor(math.sqrt(n))!=math.sqrt(n)):
#         print(a**2)
#     else:
#         if((abs(x-a))==(abs(y-a))):
#             print(x)
#         else:
#             print(y)
# import math
# for _ in range(int(input())):
#     n=int(input())
#     above=math.ceil(math.sqrt(n+1))*math.ceil(math.sqrt(n+1))
#     below=math.floor(math.sqrt(n-1))*math.floor(math.sqrt(n-1))

#     d1=n-above
#     d2=below-n

#     if(d1==d2):
#         print(below)
#     elif(d1>d2):
#         print(above)
#     else:
#         print(below)

#Get The Shadow

# import collections
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().strip().split()))
#     rep=[]
#     freq=collections.Counter(arr)
#     print(freq)
    # for k,v in freq.items():
    #     if v==2:
    #         rep.append(k)
    # for i in range(n):
    #     if arr[abs(arr[i])-1]>0:
    #         arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]

    # missnumber=[]
    # for i in range(n):
    #     if(arr[i]>0):
    #         missnumber.append(i+1)
    # print(" ".join([str(rep[0]),str(missnumber[0])]))
