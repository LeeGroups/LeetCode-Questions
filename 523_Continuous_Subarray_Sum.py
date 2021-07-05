def checkSubarraySum(nums, k):    
    if k ==0:
        for i in range(1,len(nums)):
            if nums[i] == 0 and nums[i-1] == 0:
                return True
        return False
    sums = 0
    dicts = {0:-1}
    for i in range(len(nums)):
        sums = (sums + nums[i]) % k
        if sums in dicts and i - dicts[sums] >= 2:
            return True
        else: 
            dicts[sums] = i  
    return False


# sample inputs:

#Expect True
print(checkSubarraySum([23,2,4,6,7], 6))

#Expect True
print(checkSubarraySum([23,2,6,4,7],6))

#Expect False
print(checkSubarraySum([23,2,6,4,7],13))

#Expect True
print(checkSubarraySum([5,0,0,0],3))