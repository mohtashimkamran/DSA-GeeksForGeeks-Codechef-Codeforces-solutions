#print  nos 1 to n

# def luda(x):
#     if(x==-1):
#         return
#     luda(x-1)
#     print(x,end=" ")
# n=int(input())
# print(luda(n))

#sum of 1st n numbers

# def summ(x):
#     if(x<=0):
#         return 0
#     return (x + summ(x-1))
# n=int(input())
# print(summ(n))

#sum of digits
# def sod(x):
#     if x==0:
#         return 0
#     return (x%10)+sod(x//10)
# print(sod(int(input())))

#count digits
# def cd(x):
#     if x<10:
#         return 1
#     return (1 + cd(x//10))
# print(cd(int(input())))


# def nos(x):
#     if x==0:
#         return
#     nos(x-1)
#     print(x)

# print(nos(int(input())))

#You are given a number n. You need to find the digital root of n. 
# DigitalRoot of a number is the recursive sum of its digits until we get a single digit number

# def digitalroot(x):
#     if(x<10):
#         return x
#     else:
#         return (x%10) + digitalroot(x//10)
# def digitsum(x):
#     if(digitalroot(x)>9):
#         return digitsum(digitalroot(x))
#     else:
#         return digitalroot(x)
# n=99
# print(digitsum(n))

#NTH Fibonacci
# def fibonacci(x):
#     if x<=1:
#         return x
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)
# n=20
# print(fibonacci(n))