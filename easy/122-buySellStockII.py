def maxProfit(prices):
    profit = 0

    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
