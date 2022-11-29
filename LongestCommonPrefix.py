def longestCommonPrefix(strs):
    answer = ""
    for i in strs:
        if strs.index(i) == 0:
            answer = i
        else:
            if not answer or not i or answer[0] != i[0]:
                return ""
            if len(answer) > len(i):
                answer = answer[:len(i)]
            for j in range(len(i)):
                if answer[:j] != i[:j]:
                    if j != 0:
                        answer = answer[:j-1]
                    else:
                        answer = answer[0]
    return answer


strs = ["ab", "a"]
print(longestCommonPrefix(strs))
