
def addBinary(a,b):
    n = len(a)
    m = len(b)
    c = 0
    s = ""
    for i in range(1,max(m,n)+1):     
        if i <= n and i <= m:
            u = int(a[n-i]) + int(b[m-i]) + c
            if u >= 2: 
                s = str(u-2) + s
                c = 1
            else:
                c = 0
                s = str(u) + s
        elif i <= n:
            u = int(a[n-i]) + c
            if u == 2: 
                s = str(u-2) + s
                c = 1
            else:
                c = 0
                s = str(u) + s
        else:
            u = int(b[m-i]) + c
            if u == 2:
                s = str(u-2) + s
                c = 1
            else:
                c = 0 
                s = str(u) + s
    if c == 1:
        s = "1" + s
    return s

## def addBinary(self, a: str, b: str) -> str:
##      return bin(int(a,2)+int(b,2))[2:]


# sample inputs:

#Expect 100
print( addBinary("11","1"))

#Expect 10101
print( addBinary("1010","1011"))

