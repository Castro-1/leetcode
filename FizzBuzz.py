def fizzBuzz(n):
    answer = []
    i = 1
    while i < n+1:
        tmp = ''
        if i % 3 == 0 and i % 5 == 0:
            tmp = "FizzBuzz"
        elif i % 3 == 0 and i % 5 != 0:
            tmp = "Fizz"
        elif i % 3 != 0 and i % 5 == 0:
            tmp = "Fizz"
        else:
            tmp = str(i)
        answer.append(tmp)
        i += 1
    return answer


print(fizzBuzz(3))
