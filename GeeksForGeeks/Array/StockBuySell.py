# Stock buy and sell max profit
def maxprofit(price ,n):
    profit=0
    for i in range(1,n):
        if price[i]>price[i-1]:
            profit+=(price[i]-price[i-1])
    return profit
n=7
a=[100,180,260,310,40,535,695]
print(maxprofit(a,n))
