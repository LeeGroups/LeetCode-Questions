
def firstBadVersion(n,secret = 4):
    """
    :type n: int
    :rtype: int
    """
    first = 1
    last = n
    while first != last:
        middle = (last - first) // 2 + first
        bad = isBadVersion(middle, secret)
        if bad:
            last = middle
        else:
            first = middle + 1
    return first

def isBadVersion(m, secret = 4):
    return m >= secret


# sample inputs:

#Expect 4
print( firstBadVersion(5))