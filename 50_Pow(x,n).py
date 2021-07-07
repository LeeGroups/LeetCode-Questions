def myPow(x, n):
    m = abs(n)
    product = 1
    power = x
    while m != 0:
        if m % 2 == 1:
            product *= power
            m -= 1
        else:
            m /= 2
            power *= power
    if n < 0:
        return 1/product
    else:
        return product
        
# sample inputs:

#Expect 1024.00000
print(myPow(2.00000, 10))

#Expect 9.26100
print(myPow(2.10000,3))

#Expect 0.25000
print(myPow(2.00000,-2))

""" def myPow(x, n):
    m = abs(n)
    powers = {1: x}
    k = 2
    while k <= m: 
        powers[k] = powers[k/2] * powers[k/2]
        k *= 2
    product = 1
    print(powers)
    while m > 0:        
        if m < k:
            k /= 2
        else: 
            product *= powers[k]
            m -= k
    if n < 0:
        return 1/product
    else:
        return product
 """