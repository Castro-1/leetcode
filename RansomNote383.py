def canConstruct(ransomNote, magazine):
    magazine = sorted(magazine)
    for i in range(len(ransomNote)):
        if ransomNote[i] not in magazine:
            return False
        magazine.pop(magazine.index(ransomNote[i]))
    return True


print(canConstruct("aa", "aab"))
