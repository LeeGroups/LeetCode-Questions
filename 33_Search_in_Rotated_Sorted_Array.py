def search(nums, target):
    left = 0
    right = len(nums)-1
    if target == nums[left]:
        return left
    elif target == nums[right]:
        return right
    while left != right:
        if nums[left] == target:
            return left
        middle = left + (right - left) // 2
        if target == nums[middle]:
            return middle
        if nums[left] < target < nums[middle]:
            right = middle
        elif nums[left] < target and nums[middle] < target:
            if nums[left] < nums[middle]:
                left = middle +1
            else:
                right = middle
        elif nums[left] > target and nums[middle] < target:
            left = middle +1
        elif nums[middle] > nums[left]:
            left = middle +1
        else: 
            right = middle
    if nums[left] == target:
        return left
    else:
        return -1

# beat 77%


# sample inputs:

# Expect 4
print(search([4,5,6,7,0,1,2],0))

# Expect -1
print(search([4,5,6,7,0,1,2],3))

# Expect -1
print(search([1],0))

# Expect 1
print(search([8,9,2,3,4],9))