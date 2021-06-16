
def findKthLargest(nums,k):
    return sorted(nums,reverse=True)[k-1]

# sample inputs:

#Expect 5
print( findKthLargest([3,2,1,5,6,4],2))

#Expect 4
print( findKthLargest([3,2,3,1,2,4,5,5,6], 4))

