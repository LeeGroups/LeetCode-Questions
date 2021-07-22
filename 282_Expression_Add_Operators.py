def addOperators(num, target):
    n = len(num)
    stop = True
    def increase(digits):
        carry = 1
        i = n-2
        nonlocal stop
        while carry == 1:
            if i < 0:
                stop = False
                break
            elif digits[i] == 3:
                digits[i] = 0
                i -= 1
            else: 
                digits[i] += 1
                carry = 0
    index = [0 for i in range(n-1)]
    increase(index)
    dictionary = {0: "", 1: "+", 2: "*", 3: "-"}
    output = []
    while stop:
        test = num[0]
        ignore = True
        leading = num[0]
        for i in range(n-1):
            if index[i] == 0:
                if leading == "0":
                    ignore = False
                    break
            else: 
                leading = num[i+1]
            test += dictionary[index[i]] + num[i+1]
        if ignore and eval(test) == target:
            output.append(test)
        increase(index)
    return output

# test cases

# Expect ["1*2*3","1+2+3"]
print(addOperators("123",6))

# Expect ["2*3+2","2+3*2"]
print(addOperators("232",8))

# Expect ["1*0+5","10-5"]
print(addOperators("105",5))

# Expect  ["0*0","0+0","0-0"]
print(addOperators("000",0))


# Expect  ["0*0","0+0","0-0"]
print(addOperators("10009",9))

# Expect []
print(addOperators("3456237490",9191))