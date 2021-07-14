import heapq

def topKFrequent(nums, k):
    dictionary = {}
    for i in range(len(nums)):
        if nums[i] not in dictionary:
            dictionary[nums[i]] = 1
        else:
            dictionary[nums[i]] += 1
    flipped = {}
    for elem in dictionary:
        if dictionary[elem] not in flipped:
            flipped[dictionary[elem]] = [elem]
        else:
            flipped[dictionary[elem]].append(elem)
    size = len(nums)
    n = 0 
    output = []
    while n < k:
        if size in flipped:
            output.extend(flipped[size])
            n += len(flipped[size])
        size -= 1
    return output


""" def topKFrequent(nums, k):
    dictionary = {}
    for i in range(len(nums)):
        if nums[i] not in dictionary:
            dictionary[nums[i]] = 1
        else:
            dictionary[nums[i]] += 1
    list1 = [[dictionary[elem],elem] for elem in dictionary]
    heapq.heapify(list1)
    top = heapq.nlargest(k,list1)
    return [i[1] for i in top]
        
 """
# sample inputs:

# Expect [1,2]
print(topKFrequent([1,1,1,2,2,3], 2))

# Expect [1]
print(topKFrequent([1],1))

