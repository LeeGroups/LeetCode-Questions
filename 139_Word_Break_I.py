def wordBreak(s, wordDict):
    if s == "":
        return True
    n = len(s)
    dummy = [False for i in range(n+1)]
    dummy[0] = True
    for i in range(1,n+1):
        for j in range(len(wordDict)):
            m = len(wordDict[j]) 
            if i>= m and dummy[i-m] == True and s[i-m:i] == wordDict[j]:
                dummy[i] = True
                break        
    return dummy[-1]