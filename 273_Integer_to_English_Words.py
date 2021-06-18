
def numberToWords(num):
    digit = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen", "20": "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty", "60": "Sixty", "70": "Seventy", "80": "Eighty", "90": "Ninety"}
    
    number = str(num)
    n = len(number)
    English = ""
    i = 0
    while i < n:
        if (n-i) % 3 == 0:
            if number[i] == "0":
                i += 1
                continue
            English += digit[number[i]] + " Hundred "
            i += 1
        elif (n-i) % 3 == 2:
            if number[i] == "0":
                i += 1
                continue
            if int(number[i]) < 2: 
                English += digit[number[i:i+2]] + " "
                i += 1
                if (n-i) // 3 == 1:
                    English += "Thousand "
                elif (n-i) // 3 == 2: 
                    English += "Million "
                elif (n-i) // 3 == 3:
                    English += "Billion "
                elif (n-i) // 3 == 4: 
                    English += "Trillion "
                i += 1
            else:
                English += digit[str(int(number[i])*10)] + " "
                i += 2
        else: 
            if number[i] != "0":
                English += digit[number[i]] + " " 
            if (n-i) // 3 == 0:
                pass
            elif (n-i) // 3 == 1:
                English += "Thousand "
            elif (n-i) // 3 == 2: 
                English += "Million "
            elif (n-i) // 3 == 3:
                English += "Billion "
            elif (n-i) // 3 == 4: 
                English += "Trillion "
            i += 1
    m = len(English)
    if English[m-1] == " ":
        English = English[:m-1]
    return English
            


# sample inputs:

#Expect "One Hundred Twenty Three"
print( numberToWords(123))

#Expect "Twelve Thousand Three Hundred Forty Five"
print( numberToWords(12345))

#Expect "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print( numberToWords(1234567))

#Expect "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
print( numberToWords(1234567891))

#Expect "Twelve Thousand Three Hundred Forty Five"
print( numberToWords(12345))

#Expect "One Hundred Fifteen"
print( numberToWords(115))

#Expect "Twenty"
print( numberToWords(20))

print( numberToWords(100000000))

print( numberToWords(123116519))