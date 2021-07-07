def calculate(s):
    digits = {"0":0, "1": 1, "2":2, "3": 3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9}
    n = len(s)

    def find_num(string, start):
        for j in range(start,n):
            if s[j] == " ":
                continue
            elif s[j] not in digits:
                return [int(string[start:j]),j]
        return [int(string[start:]),len(string)]
    
    def find_next(string,start):        
        next_num , j = find_num(string,start)
        while j < n:
            if s[j] == "+" or s[j] == "-":
                return [next_num,j]
            elif s[j] == "*":
                number, j = find_num(s,j+1)
                next_num *= number
            elif s[j] == "/":
                number, j = find_num(s,j+1)
                next_num //= number
        return [next_num,j]

    output, i = find_next(s,0)
    while i < len(s):
        if s[i] in digits:
            number, i = find_num(s,i)
            if output == True:
                output = number
        elif s[i] == "+":
            next_num, i = find_next(s,i+1)
            output += next_num
        elif s[i] == "-":
            next_num, i = find_next(s,i+1)
            output -= next_num
        else:
            i+= 1
    return output
        
# sample inputs:

#Expect 7
print(calculate("3+2*2"))

#Expect 1
print(calculate(" 3/2 "))

#Expect 5
print(calculate(" 3+5 / 2 "))

#Expect 1
print(calculate("1-1+1"))