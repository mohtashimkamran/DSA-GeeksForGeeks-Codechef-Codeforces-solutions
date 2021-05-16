# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))
#     c = 0
#     for i in range(1,n):
#         mina = min(a[i],a[i-1])
#         maxa = max(a[i],a[i-1])
#         while mina*2<maxa:
#             mina*=2
#             c+=1
#     print(c)

# for _ in range(input()):
#     n=int(input())
#     arr=list(map(int,input().split))
# t=int(input())
# for _ in range(t):
#     n = int(input())//3
#     a = list(map(int,input().split()))
#     x=0;count=[0]*3
#     for b in a:
#         if b%3==0:
#             count[0]+=1
#         elif b%3==1:
#             count[1]+=1
#         else:
#             count[2]+=1
#     count=[_-n for _ in count]
#     i=k=0
#     while k<3:
#         if count[i]>0:
#             count[i%3]-=1
#             count[(i+1)%3]+=1
#             x+=1
#             k=0
#         else:
#             k+=1
#             i = (i+1)%3
#     print(x)

def cube(n):
    cuberoot=round(n**(1/3))
    if cuberoot*cuberoot*cuberoot==n:
        return True
    return False
for _ in range(int(input())):
    n=int(input())
    i=1
    flag=0
    while (i*i*i)<=n:
        a=n-(i*i*i)
        if cube(a)==True and a>0:
            flag=1
        i+=1
    if flag==1:
        print("YES")
    else:
        print("NO")      


# for _ in range(int(input())):
#     n=int(input())
#     i=1
#     flag=0
#     while(i*i*i<=n):
#         j=1
#         while(j*j*j<=n):
#             if (i*i*i + j*j*j == n):
#                 flag=1
#                 break
#             j+=1
#         i+=1
    # if flag==1:
    #     print("YES")
    # else:
    #     print("NO")        