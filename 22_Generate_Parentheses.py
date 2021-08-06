def generateParenthesis(n):
    if n == 0:
        return [""]
    output = []
    for k in range(n):
        s = generateParenthesis(k)
        t = generateParenthesis(n-1-k)
        for inside in s:
            for outside in t:
                output.append("(" + inside + ")" + outside)
    return output

# Sample inputs

# Expect ["()"]
print(generateParenthesis(1))

# Expect ["(()),()()"]
print(generateParenthesis(2))

# Expect ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(3))

