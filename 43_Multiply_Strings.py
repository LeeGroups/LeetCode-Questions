def multiply(num1, num2):
    total_product = "0"
    for i in range(len(num1)-1,-1,-1):    
        carry = 0
        product = ""
        for k in range(len(num1)-1-i):
            product += "0"
        for j in range(len(num2)-1,-1,-1):
            digit = str(int(num1[i])*int(num2[j]) + carry)
            if len(digit) == 1:
                product = digit + product
                carry = 0
            else:
                product = digit[1] + product
                carry = int(digit[0])
        if carry != 0:
            product = str(carry) + product
        total_product = str(eval(product + "+" + total_product))
        
    return total_product

# Sample inputs:

# Expect 6
print(multiply("2","3"))

# Expect 56088
print(multiply("123","456"))

# Expect 625
print(multiply("25","25"))