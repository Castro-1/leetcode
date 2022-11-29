def kWeakestRows(mat, k):
    """hashmap = {}
    answer = []
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                count += 1
            else:
                break
        hashmap[i] = count
    sorthash = sorted(hashmap.items(), key=lambda x: x[1])

    values = sorthash

    for i in range(k):
        answer.append(values[i][0])
    return answer"""
    answer = []
    for i in range(len(mat)):
        answer += [[sum(mat[i]), i]]

    y = answer.sort(key=lambda x: x[0])

    return [i[1] for i in answer[:k]]


mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

k = 2
print(kWeakestRows(mat, k))
