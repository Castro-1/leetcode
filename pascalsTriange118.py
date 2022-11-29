def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1], [1, 1]]
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return ans
    for i in range(2, numRows):
        ans += [[1]]
        for j in range(1, i+1):
            if j >= (i+1)/2:
                ans[i] += [ans[i][i-j]]
            else:
                ans[i] += [ans[i-1][j-1]+ans[i-1][j]]

    return ans


num = 5
print(generate(num))
