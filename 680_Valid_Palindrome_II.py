
def validPalindrome(s):
    def check_palindrome(s,skipped):
        n = len(s)
        if n <= 1:
            return True
        elif s[0] == s[n-1]:
            return check_palindrome(s[1:n-1],skipped)
        elif skipped:
            return False
        else:
            return check_palindrome(s[0:n-1],True) or check_palindrome(s[1:n],True)
    return check_palindrome(s,False)


# sample inputs:

#Expect True
print( validPalindrome("aba"))

#Expect True
print( validPalindrome("abca"))

#Expect False
print( validPalindrome("abc"))

#Expect True
print( validPalindrome("acbca"))
