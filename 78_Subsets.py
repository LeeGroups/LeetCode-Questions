import json

def subsets(nums):
    stack = [nums]
    output = set()
    while stack:
        temp = stack.pop()
        output.add(str(temp))
        for i in range(len(temp)):
            x = temp[:i] + temp[i+1:]
            if str(x) not in output:
                stack.append(x)
    return [json.loads(elem) for elem in output]

print(subsets([1,2,3]))