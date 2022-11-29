def maximumWealth(accounts):
    maxw = 0
    for i in range(len(accounts)):
        cw = sum(accounts[i])
        if cw > maxw:
            maxw = cw

    return maxw

    """maxw = 0
    for i in range(len(accounts)):
        currentw = sum(accounts[i])
        maxw = max(maxw, currentw)
    
    return maxw"""


accounts = [[1, 2, 3], [3, 2, 1]]
print(maximumWealth(accounts))
