
def productExceptSelf(nums):
    n = len(nums)        
    
    answer = [1 for i in range(n)]
    
    # product of the terms starting from the beginning
    start_total = 1
    first_few = [1 for i in range(n)]

    # product of the terms starting from the end
    end_total = 1
    last_few = [1 for i in range(n)]

    for i in range(n):
        start_total *= nums[i]
        end_total *= nums[n-1-i] 
        first_few[i] = start_total
        last_few[n-1-i] = end_total

    answer[0] = last_few[1]
    answer[n-1] = first_few[n-2]

    for i in range(1,n-1):
        answer[i] = first_few[i-1] * last_few[i+1]

    return answer


# sample inputs:

#Expect [24,12,8,6]
print( productExceptSelf([1,2,3,4]))

#Expect [0,0,9,0,0]
print( productExceptSelf([-1,1,0,-3,3]))
