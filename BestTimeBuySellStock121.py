def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    profit = 0
    for sell in range(1, len(prices)):
        while prices[sell] < prices[buy]:
            buy += 1
        tmp = prices[sell]-prices[buy]
        if tmp > profit:
            profit = tmp

    return profit


prices = [3, 2, 6, 5, 0, 3]
print(maxProfit(prices))
