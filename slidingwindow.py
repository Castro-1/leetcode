def solucion(array, k):
    """sol = []
    i = 0
    while i + k < len(array):
        sol.append(sum(array[i:k+i])/k)
        i += 1
    return sol"""
    arraystart = 0
    arraysum = 0.0
    sol = []
    for arrayend in range(len(array)):
        arraysum += array[arrayend]
        if arrayend >= k-1:
            sol.append(arraysum/k)
            arraysum -= array[arraystart]
            arraystart += 1
    return sol


array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

print(solucion(array, k))
