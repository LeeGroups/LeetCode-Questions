def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = max(prices[i] - min_price, profit)
    profit = max(prices[len(prices)-1]-min_price, profit)
    return profit