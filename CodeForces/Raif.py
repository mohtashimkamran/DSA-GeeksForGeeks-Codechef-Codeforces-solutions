for i in range(int(input())):
#     n=input()
#     while("BB" in n or "AB" in n):
#         if("AB" in n):
#             n=n.replace("AB","")
#         elif("BB" in n):
#             n=n.replace("BB","")
#     print(len(n))
    x1,y1,x2,y2=map(int,input().split())
    c=abs(y2-y1)
    d=abs(x2-x1)
    if(c==0 or d==0):
        print(d+c)
    else:
        print(c+d+2)
    
