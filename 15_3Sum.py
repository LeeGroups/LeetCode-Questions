def threeSum(nums):
    output = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = len(nums)-1
        while j < k:
            n = - nums[j] - nums[k]
            if n == nums[i]:
                output.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
            elif n > nums[i]:
                j += 1
            else: 
                k -= 1
    return output

""" import json
def threeSum(nums):
    two_sums = {}
    i = 0 
    output = set()
    nums.sort()
    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            n = nums[i] + nums[j]
            if n not in two_sums:
                two_sums[n] = [(i,j)]
            else:
                two_sums[n].append((i,j))
    for k in range(len(nums)):
        if -nums[k] in two_sums:
            for elem in two_sums[-nums[k]]:
                i, j = elem
                if k != i and k != j:
                    list1 = [nums[i],nums[j],nums[k]]
                    list1.sort()
                    list2 = str(list1)
                    if list2 not in output:
                        output.add(list2)
    return [json.loads(list2) for list2 in output] """