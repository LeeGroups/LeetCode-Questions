def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True          


# sample inputs:

#Expect True
print( isPalindrome("A man, a plan, a canal: Panama"))

#Expect False
print( isPalindrome("race a car"))
