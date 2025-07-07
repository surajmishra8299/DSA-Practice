def buysell(price):

    n = len(price)
    maxp = 0

    for i in range(1,n):
        if price[i] > price[i-1]:
            maxp = maxp + (price[i] - price[i-1])
    
    return maxp

num = [7, 1, 5, 3, 6, 4]
print(buysell(num))