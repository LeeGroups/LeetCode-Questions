def searchRange(nums, target):
    n = len(nums)
    if not nums:
        return [-1,-1]
    first1 = first2 = 0
    last1 = last2 = n 
    while first1 != last1 or first2 != last2:
        if first1 != last1:
            middle1 = (last1-first1) // 2 + first1
            if nums[middle1] > target:
                if middle1 == 0 or nums[middle1-1] < target:
                    first1 = last1 = -1
                else:
                    last1 = middle1
                    last2 = middle1
            elif nums[middle1] < target:
                if middle1 == n-1:
                    first1 = last1 = -1
                else:
                    first1 = middle1 + 1
                    first2 = middle1 + 1
            else: 
                if middle1 == 0 or nums[middle1-1] < target:
                    first1 = last1 = middle1
                else:
                    last1 = middle1

        if first2 != last2:
            middle2 = (last2-first2) // 2 + first2
            if nums[middle2] > target:
                if middle2 == 0 or nums[middle2-1] < target:
                    first2 = last2 = -1
                else:
                    last2 = middle2
            elif nums[middle2] < target:
                if middle2 == n-1:
                    first2 = last2 = -1
                else:
                    first2 = middle2 + 1
            else: 
                if middle2 == n-1 or nums[middle2+1] > target:
                    first2 = last2 = middle2
                else:
                    first2 = middle2 + 1
    return [first1,first2]




        
# sample inputs:

#Expect [3,4]
print(searchRange([5,7,7,8,8,10],8))

#Expect [-1,-1]
print(searchRange([5,7,7,8,8,10],6))

#Expect [-1,-1]
print(searchRange([],0))

#Expect [6,6]
print(searchRange([1,1,3,3,5,5,6],6))

#Expect [0,1]
print(searchRange([1,1,3,3,5,5,6],1))

#Expect [0,0]
print(searchRange([1,3,3,5,5,6],1))