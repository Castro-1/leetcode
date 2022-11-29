import math


def solucion(array, s):
    minl = math.inf
    start = 0
    sum = 0
    for end in range(len(array)):
        sum += array[end]
        while sum >= s:
            minl = end - start + 1
            sum -= array[start]
            start += 1
    if minl == math.inf:
        return 0
    else:
        return minl


array = [2, 1, 5, 2, 3, 8]
s = 7
print(solucion(array, s))
