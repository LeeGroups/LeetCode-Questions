def lengthOfLongestSubstring(s):        
    longest = 0
    start = 0
    letters = {}
    for j in range(len(s)):
        if s[j] not in letters:
            letters[s[j]] = j
        else:
            if letters[s[j]] >= start:
                longest = max(longest, j - start)
                start = letters[s[j]] + 1
                letters[s[j]] = j
            else:
                letters[s[j]] = j 
    longest = max(longest, len(s)-start)
    return longest