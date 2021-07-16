import math
import copy

def wordBreak(s, wordDict):
    if s == "":
        return True
    n = len(s)
    dummy = [None for i in range(n+1)]
    dummy[0] = True
    for i in range(1,n+1):
        for j in range(len(wordDict)):
            m = len(wordDict[j]) 
            if i>= m and dummy[i-m] and s[i-m:i] == wordDict[j]:
                if dummy[i-m] == True:
                    list1 = [[j]]
                else:
                    list1 = [copy.deepcopy(dummy[i-m][u]) for u in range(len(dummy[i-m]))]
                    for u in range(len(dummy[i-m])):
                        list1[u].append(j)
                if not dummy[i]:
                    dummy[i] = list1
                else:
                    dummy[i].extend(list1)
    print(dummy)
    output = []
    if not dummy[-1]:
        return None
    else:
        for i in range(len(dummy[-1])):
            word = wordDict[dummy[-1][i][0]]
            for j in range(1,len(dummy[-1][i])):
                word += " " + wordDict[dummy[-1][i][j]]
            output.append(word)
    return output    

                
""" beats 71.5%"""

# sample inputs:

# Expect ["cats and dog","cat sand dog"]
print(wordBreak("catsanddog",["cat","cats","and","sand","dog"]))

# Expect ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))

# Expect []
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

