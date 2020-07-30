def maxProfit(prices):
    if len(prices) == 0:
        return 0
    buy = prices[0]
    maxProfit = 0

    for i in range(1, len(prices)):
        sell = prices[i]
        buy = min(buy, prices[i-1])
        maxProfit = max(maxProfit, (sell-buy))
#             if buy > prices[i-1]:
#                 buy = prices[i-1]
#             if (sell-buy)>maxProfit:
#                 maxProfit = sell-buy

    return maxProfit
