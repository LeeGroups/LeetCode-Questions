def arrayNesting(nums):
    seen = set()
    longest = 0
    for i in range(len(nums)):
        current = 0
        a = i
        while a not in seen:
            seen.add(a)
            a = nums[a]
            current += 1
        longest = max(current,longest)
    return longest

# sample inputs:

#Expect 4
print( arrayNesting([5,4,0,3,1,6,2]))

#Expect 1
print( arrayNesting([0,1,2]))
