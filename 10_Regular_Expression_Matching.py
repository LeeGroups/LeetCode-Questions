def isMatch(s, p):
    matches = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
    matches[0][0] = True

    for i in range(len(s)):
        for j in range(len(p)):



    return matches[-1][-1]


# Sample Inputs:

# Expect False
print(isMatch("aa","a"))

# Expect True
print(isMatch("aa","a*"))

# Expect True
print(isMatch("ab",".*"))

# Expect True
print(isMatch("aab","c*a*b"))

# Expect False
print(isMatch("mississippi","mis*is*p*."))