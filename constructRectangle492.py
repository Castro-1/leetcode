def constructRectangle(area):
    i = 1
    ans = area
    sol = [1, 1]
    tmp = 0.0
    while i < ans:
        if area % i == 0:
            ans = area/i
            sol = [int(ans), i]
        i += 1

    return sol


print(constructRectangle(37))
