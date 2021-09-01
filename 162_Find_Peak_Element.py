def findPeakElement(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        mid = (j-i) // 2 + i
        mid_right = mid + 1        
        if nums[mid_right] > nums[mid]:            
            i = mid_right
        else:
            j = mid
    return i

# Sample Inputs:

# Expect 2
print(findPeakElement([1,2,3,1]))

# Expect 5
print(findPeakElement([1,2,1,3,5,6,4]))