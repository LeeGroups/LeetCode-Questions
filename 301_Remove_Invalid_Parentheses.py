import itertools
import copy

def remove_indices_from_string(s,list1):
    output = ""
    for i in range(len(s)):
        if i not in list1:
            output += s[i]
    return output

def removeInvalidParentheses(s):
    removed = [[]]
    bra = []
    ket = []
    parity_index = -1
    for i in range(len(s)):
        if s[i] == "(":
            if ket:
                n = len(bra)
                m = len(ket)
                if n < m:                    
                    combo = list(itertools.combinations(ket,m-n))
                    t = len(combo)
                    extension = [0 for i in range(t*len(removed))]
                    for u in range(t):
                        for v in range(len(removed)):
                            extension[u+v] = copy.deepcopy(removed[v])
                            extension[u+v].extend(list(combo[u]))
                    removed = extension                   
                    bra, ket = [i] , []
                elif n>m:
                    bra = [k for k in bra if k > parity_index]
                    combo = list(itertools.combinations(bra,n-m))
                    t = len(combo)
                    extension = [0 for i in range(t*len(removed))]
                    for u in range(t):
                        for v in range(len(removed)):
                            extension[u+v] = copy.deepcopy(removed[v])
                            extension[u+v].extend(list(combo[u]))
                    removed = extension
                    bra, ket = [i] , []
                else:
                    bra.append(i)
            else:
                bra.append(i)
        elif s[i] == ")":
            if bra:
                ket.append(i)
                if len(bra) == len(ket):
                    parity_index = i
            else: 
                for j in range(len(removed)):
                    removed[j].append(i)
    for i in range(len(removed)):
        removed[i].extend(bra[len(ket):])
    initial = [remove_indices_from_string(s,j) for j in removed]
    dummy = []
    for i in range(len(initial)):
        if initial[i] not in dummy:
            dummy.append(initial[i])
    return dummy

# Sample Inputs

# Expect ["(())()","()()()"]
print(removeInvalidParentheses("()())()"))

# Expect ["(a())()","(a)()()"]
print(removeInvalidParentheses("(a)())()"))

# Expect [""]
print(removeInvalidParentheses(")("))

# Expect ["()"]
print(removeInvalidParentheses("(()("))

# Expect ["()"]
print(removeInvalidParentheses("))()(("))

# Expect ["r()()","r(())","(r)()","(r())"]
print(removeInvalidParentheses("(r(()()("))

['r()()', '(r)()']

r(()) removed 0, 
