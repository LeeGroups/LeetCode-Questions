def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m
    j = n
    while i > 0 or j > 0 :
        if j == 0: 
            nums1[i-1] = nums1[i-1]
            i -= 1
        elif i == 0:
            nums1[j-1] = nums2[j-1]                            
            j -= 1
        elif nums1[i-1] < nums2[j-1]:
            nums1[i+j-1] = nums2[j-1]
            j -= 1
        else: 
            nums1[i+j-1] = nums1[i-1]
            i -= 1
    return nums1

# sample inputs:

#Expect [2]
print(  merge([0],0, [2],1))

#Expect [1,2,2,3,5,6]
print(merge([1,2,3,0,0,0], 3, [2,5,6],3))

#Expect [1]
print(merge([1], 1, [],0))

