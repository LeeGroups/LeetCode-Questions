def exclusiveTime(n, logs):
    output = [0 for i in range(n)]
    previous = 0
    current = []
    for i in range(len(logs)):
        x, y, z = logs[i].split(":")
        num = int(x)
        end = int(z)
        if y == "start":
            if current != []:
                output[current[-1]] += end - previous
            current.append(num)
            previous = end
        else:
            u = current.pop()
            output[u] += end - previous + 1
            previous = end + 1
    return output


# sample inputs:

#Expect [3,4]
print(exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))

#Expect [8]
print(exclusiveTime(1,["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))

#Expect [7,1]
print(exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))

#Expect [8,1]
print(exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]))

#Expect [1]
print(exclusiveTime(1,["0:start:0","0:end:0"]))