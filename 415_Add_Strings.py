
def addStrings(num1,num2):
    n = len(num1)
    m = len(num2)
    c = 0
    s = ""
    for i in range(1,max(m,n)+1):     
        if i <= n and i <= m:
            u = int(num1[n-i]) + int(num2[m-i]) + c
            if u >= 10: 
                s = str(u-10) + s
                c = 1
            else:
                c = 0
                s = str(u) + s
        elif i <= n:
            u = int(num1[n-i]) + c
            if u == 10: 
                s = str(u-10) + s
                c = 1
            else:
                c = 0
                s = str(u) + s
        else:
            u = int(num2[m-i]) + c
            if u == 10:
                s = str(u-10) + s
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

