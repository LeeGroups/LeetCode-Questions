def isMonotonic(nums):
    direction = nums[0] < nums[-1]
    for i in range(1,len(nums)):
        if nums[i-1] < nums[i]:
            if not direction:
                return False
        elif nums[i-1] > nums[i]:
            if direction:
                return False
    return True