def maximumSwap(num):
    n = [i for i in str(num)]
    length = len(n)
    largest_index = length - 1
    smallest_index = length -1
    temp = length -1
    for i in range(len(n)-1,-1,-1):
        if n[temp] < n[i]:
            temp = i
        elif n[temp] > n[i]:
            largest_index = temp
            smallest_index = i
    a = n[largest_index]
    n[largest_index] = n[smallest_index]
    n[smallest_index] = a
    return "".join(n)

