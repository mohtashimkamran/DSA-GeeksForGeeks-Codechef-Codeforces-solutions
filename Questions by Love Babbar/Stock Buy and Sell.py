# Stock Buy and Sell
def stockbuysell(arr):
    lowestPrice=arr[0]
    maxProfit=0

    for i in arr:
        if i<lowestPrice:
            lowestPrice=arr[i]
        
        if i>lowestPrice:
            localMaxProfit=i-lowestPrice

            if localMaxProfit>maxProfit:
                maxProfit=localMaxProfit
    return maxProfit

a=[7,1,5,3,6,4]
print(stockbuysell(a))