def leastInterval(tasks, n):
    length = len(tasks)
    dictionary = {}
    for i in range(0,len(tasks)):
        if tasks[i] not in dictionary:
            dictionary[tasks[i]] = 1
        else:
            dictionary[tasks[i]] +=1
    max_freq = 0   
    occurrence = 0
    for elem in dictionary:
        if dictionary[elem] > max_freq:
            max_freq = dictionary[elem]
            occurrence  = 1
        elif dictionary[elem] == max_freq:
            occurrence += 1
    max_blank = (n - occurrence + 1) * (max_freq - 1) 
    deletion = length - occurrence * (max_freq)  
    return length + max(0, max_blank - deletion)
                
""" let the maximum number of occurrence of some letter be max_freq. then the maximum number of blanks is (max_freq - 1) * n
but then i have to deal with cases where multiple letters appear the same amount of time, that's why max_blank is ugly
after that, you subtract this by however many letters you haven't filled in, and this should be the number of blanks one needs
 """

# sample inputs:

# Expect 8
print(leastInterval(["A","A","A","B","B","B"], 2))

# Expect 6
print(leastInterval(["A","A","A","B","B","B"],0))

# Expect 16
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
