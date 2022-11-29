def romanToInt(s):
    answer = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "I":
            answer = answer + 1
        elif s[i] == "V":
            answer = answer + 5
            if i != 0 and s[i-1] == "I":
                count = count + 2
        elif s[i] == "X":
            answer = answer + 10
            if i != 0 and s[i-1] == "I":
                count = count + 2
        elif s[i] == "L":
            answer = answer + 50
            if i != 0 and s[i-1] == "X":
                count = count + 20
        elif s[i] == "C":
            answer = answer + 100
            if i != 0 and s[i-1] == "X":
                count = count + 20
        elif s[i] == "D":
            if i != 0 and s[i-1] == "C":
                count = count + 200
            answer = answer + 500
        elif s[i] == "M":
            if i != 0 and s[i-1] == "C":
                count = count + 200
            answer = answer + 1000
    print(answer-count)
    print(answer)
    print(count)


s = "MMCMXC"
romanToInt(s)
