def second_max(nums):
    first_max = 0
    for x in range(0, len(nums)):
        if(nums[x] > first_max):
            first_max = nums[x]
    
    nums.remove(first_max)
    
    second_max = 0
    for x in range(0, len(nums)):
        if(nums[x] > second_max):
            second_max = nums[x]
            
    return second_max

print(second_max([1,2,3,4,5])) #4