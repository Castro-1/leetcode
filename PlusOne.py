def plusOne(digits):
    for i in range(len(digits)):
        if digits[-i-1] == 9:
            if i+1 == len(digits):
                digits[-i-1] = 1
                digits.append(0)
                return digits
            else:
                digits[-i-1] = 0
        else:
            digits[-i-1] += 1
            return digits


digits = [9]
plusOne(digits)
