
def subarraySum(nums, k) -> int:
    
    # A hash storing all the cumulative sums
    csums = {0: 1}

    # a variable storing the current cumulative sum
    sum = 0

    # stores the number of times k appears as a difference of the cumulative sums
    x = 0

    for i in range(len(nums)):
        sum += nums[i]

        if sum - k in csums:
            x += csums[sum-k]
        
        if sum not in csums:
            csums[sum] = 1
        else: 
            csums[sum] += 1

    return x


# sample inputs:

#Expect 2
print( subarraySum([1,1,1],2))

#Expect 2
print( subarraySum([1,2,3], 3))

#Expect 4
print( subarraySum([1,1,2,5,7,1,1,2], 2))

#Expect 0
print( subarraySum([1], 0))