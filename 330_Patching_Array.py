def findSums(nums):
    if len(nums)==1:
        return set(nums)
    else:
        return set([nums[0]]+[nums[0]+s for s in findSums(nums[1:])] + [s for s in findSums(nums[1:])])

def minPatches(nums, n) -> int:
    # If we have [1,2,3,...,k] and we don't have k+1, then we simply add it and we get all numbers up
    # to 2k+1
    # So we have to update at each step which one is the first number that doesn't appear and add it
    sums = findSums(nums)
    checkpoints = sorted(list(sums))
    checkpoints.append(n+1)
    k=1
    patches = 0
    idx=0
    nextCheckpoint = checkpoints[idx]
    while k<n:
        while checkpoints[idx]<=k:
            idx+=1
            nextCheckpoint = checkpoints[idx]
        if k not in sums:
            k = 2*k-1
            if k+1>=nextCheckpoint:
                while k+1>=nextCheckpoint and nextCheckpoint<=n:
                    if checkpoints[idx+1]>k+1:
                        k = 2*nextCheckpoint-1
                    idx+=1
                    nextCheckpoint = checkpoints[idx]
            patches+=1
        k+=1
    return patches

print(minPatches([1,3],6))