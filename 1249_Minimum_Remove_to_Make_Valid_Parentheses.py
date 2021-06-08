def minRemoveToMakeValid(s: str) -> str:
    
    bracket = ["(",")"]

    # an array to keep track of the indices of the positions of open "("
    stack = []

    # an array to keep track of indices of unpaired ")"
    bad = []

    # a loop that adds the indices of "(" to stack, and delete them if they are paired; at the same time as adding the indices of unpaired ")" to bad
    for i in range(len(s)):
        if s[i] not in bracket:
            continue
        elif s[i] == "(":
            stack.append(i)
        elif s[i] == ")" and stack != []:
            stack.pop()
        else: 
            bad.append(i)

    y = ""

    # a loop that creates a new string y, which is just s with the indices in stack and bad deleted
    for i in range(len(s)):
        if i not in (stack + bad):
            y += s[i]
        else: 
            continue    
    return y


# Test

print(minRemoveToMakeValid("lee(t(c)o)de)"))

print(minRemoveToMakeValid("a)b(c)d"))

print(minRemoveToMakeValid("))(("))

print(minRemoveToMakeValid("(a(b(c)d)"))
