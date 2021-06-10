
def productExceptSelf(nums):
    n = len(nums)        
    
    answer = [1 for i in range(n)]
    
    # product of the terms starting from the beginning
    start_total = 1

    # product of the terms starting from the end
    end_total = 1

    for i in range(n):
        answer[i] *= start_total
        answer[n-i-1] *= end_total
        start_total *= nums[i]
        end_total *= nums[n-1-i] 

    return answer


# sample inputs:

#Expect [24,12,8,6]
print( productExceptSelf([1,2,3,4]))

#Expect [0,0,9,0,0]
print( productExceptSelf([-1,1,0,-3,3]))
