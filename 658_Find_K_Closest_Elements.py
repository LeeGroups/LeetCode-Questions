import heapq

def findClosestElements(arr, k, x):
    i, j = 0, len(arr) - 1
    while i < j - k +1:
        if j == len(arr):
            i += 1
        elif i == -1:
            j -= 1
        elif x - arr[i] > arr[j] - x:
            i += 1
        else:
            j -= 1
    return arr[i:j+1]


# Sample Inputs:

# Expect [7,8]
print(findClosestElements([0,1,2,4,7,8],2,10))

# Expect [0,2]
print(findClosestElements([0,2,3,4,7],2,-1))

# Expect [1,2,3,4]
print(findClosestElements([1,2,3,4,5],4,3))


# Heap solution
""" def findClosestElements(arr, k, x):
    list1 = [(abs(elem - x),elem) for elem in arr]
    heapq.heapify(list1)
    output = []
    for i in range(k):
        output.append(heapq.heappop(list1)[1])
    return sorted(output) """

# Binary search into two pointer
""" def findClosestElements(arr, k, x):
    i, j = 0, len(arr)
    while i < j:
        mid = (j-i) // 2 + i
        if arr[mid] > x:
            j = mid
        elif arr[mid] < x:
            i = mid
            if mid == len(arr)-1 or arr[mid+1] > x:
                j = mid
        else: 
            i, j = mid, mid
    j += 1
    output = []
    while k > 0:
        if j == len(arr):
            output = [arr[i]] + output
            i -= 1
        elif i == -1:
            output.append(arr[j])
            j += 1
        elif x - arr[i] > arr[j] - x:
            output.append(arr[j])
            j += 1
        else:
            output = [arr[i]] + output
            i -= 1
        k -= 1
    return output """