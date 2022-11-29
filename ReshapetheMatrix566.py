def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    rmat = len(mat)
    cmat = len(mat[0])
    t = c*r
    if rmat*cmat != t:
        return mat

    newmat = [[0 for _ in range(c)]for _ in range(r)]
    k = 0
    for i in range(rmat):
        for j in range(cmat):
            newmat[k//c][k % c] = mat[i][j]
            k += 1
    return newmat


mat = [[1, 2], [3, 4]]
r = 4
c = 1
print(matrixReshape(mat, r, c))
