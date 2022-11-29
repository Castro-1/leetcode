def maxsum(array, k):
    start = 0
    sum = 0
    max = 0
    for end in range(len(array)):
        sum += array[end]
        if end >= k-1:
            if sum > max:
                max = sum
            sum -= array[start]
            start += 1
    return max


array = [2, 1, 5, 1, 3, 2]
k = 3
print(maxsum(array, k))
