import collections

def findAnagrams(s, p):
    anagram = collections.defaultdict(int)    
    n = len(p)
    for i in range(n):
        anagram[p[i]] += 1
    i = 0
    reset = True
    temp = collections.defaultdict(int)
    output = []
    while i <= len(s)-n:
        if reset:            
            temp = collections.defaultdict(int)
            for j in range(n):
                if s[i+j] not in anagram:
                    i += j+1
                    reset = True
                    break
                else:
                    temp[s[i+j]] += 1
                    if j == n-1:
                        reset = False
        else:
            if s[i+n-1] not in anagram:
                i = i+n
                reset = True
            else:
                temp[s[i+n-1]] += 1
                temp[s[i-1]] -= 1            
        if not reset:
            is_anagram = True
            for char in anagram:
                if anagram[char] != temp[char]:
                    is_anagram = False
                    break
            if is_anagram:
                output.append(i)
            i += 1
    return output

        
# sample inputs:

#Expect [0,6]
print(findAnagrams("cbaebabacd", "abc"))

#Expect [0,1,2]
print(findAnagrams("abab", "ab"))

#Expect [1]
print(findAnagrams("baa", "aa"))