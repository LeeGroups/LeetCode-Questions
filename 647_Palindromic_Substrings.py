def countSubstrings(s):
    # A 2x2 chart where the (i,j)-th entry indicates whether or not s[i:j+1] is a palindrome or not 
    isPalindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
    # since s[i:i+1] = s[i], it is always a palindrome
    for i in range(len(s)):
        isPalindrome[i][i] = True    
    NumberPalin = len(s)
    palindrome = []
    for n in range(2,len(s)+1):
        for i in range(len(s)-n+1):
            if n == 2:
                isPalindrome[i][i+1] = s[i] == s[i+1]
            else:
                isPalindrome[i][i+n-1] = s[i] == s[i+n-1] and isPalindrome[i+1][i+n-2]
            if isPalindrome[i][i+n-1]:
                NumberPalin += 1
                palindrome.append(s[i:i+n])
    return NumberPalin


# Sample Inputs:

# Expect 3
print(countSubstrings("abc"))

# Expect 6
print(countSubstrings("aaa"))

# Expect 8
print(countSubstrings("ubaaa"))

