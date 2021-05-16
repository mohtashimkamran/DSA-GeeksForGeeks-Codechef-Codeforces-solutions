# a=[]
# while True:
#     s="Is it rated?"
#     x=input()
#     a.append(s)
# for i in range(len(a)):
#     if a[i]==s:
#         print("NO")

# # import math
# # n=int(input())
# # print(math.floor(math.sqrt(n)))

def apr(arg1=15,*arg2):
    for num in arg2:
        if arg1>num:
            return num
    return 0

print(apr(9,12,45,0))