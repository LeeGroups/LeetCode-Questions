import math

def minWindow(s,t):
    if not s or not t:
        return ""
    n = len(s)
    m = len(t)
    char = {}
    for elem in t:
        if elem not in char:
            char[elem] = 1
        else:
            char[elem] += 1
    left = 0
    right = 0
    correct = 0
    current = {}
    best = ""
    best_size = float('inf')
    while right < n:
        if s[right] not in current:
            current[s[right]] = 0
        current[s[right]] += 1
        if s[right] in char and current[s[right]] <= char[s[right]]:
            correct += 1
        while correct == len(t):
            if right + 1 - left < best_size:
                best = s[left:right+1]
                best_size = right - left + 1
            current[s[left]] -= 1
            if s[left] in char and current[s[left]] < char[s[left]]:
                correct -= 1
            left += 1
        right += 1 
    return best

                
""" beats 71.5%"""

# sample inputs:

# Expect BANC
print(minWindow("ADOBECODEBANC","ABC"))

# Expect ""
print(minWindow("a","aa"))

# Expect "a"
print(minWindow("a","a"))