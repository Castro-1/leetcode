def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    ans = -1
    chars = {}
    for i in range(len(s)):
        if s[i] in chars:
            del chars[s[i]]
        else:
            chars[s[i]] = i
    if chars == {}:
        return ans
    return list(chars.values())[0]


print(firstUniqChar("leetcode"))
