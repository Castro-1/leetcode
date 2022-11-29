def numberOfSteps(num):
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num/2
            count += 1
        else:
            num -= 1
            count += 1

    return count
    # return len(bin(num)[2:])+bin(num).count("1") -1


print(numberOfSteps(3))
