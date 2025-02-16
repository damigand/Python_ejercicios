def max_number(nums):
    num = 0
    for x in range(0, len(nums)):
        if(nums[x] > num):
            num = nums[x]
    
    return num

print(max_number([1,15,186,54,23,45])) #186