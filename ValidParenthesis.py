def isValid(self, s):
    par = {}
    for i in range(len(s)):
        if s[i] in par:
            par[s[i]] += 1
        else:
            par[s[i]] = 1

    pare = par["("] - par[")"]
    cor = par["["] - par["]"]
    llav = par["{"] - par["}"]

    if llav != 0 or pare != 0 or cor != 0:
        return False
    return True
