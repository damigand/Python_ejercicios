def unicos(nums):
    result = []
    for x in range(0, len(nums)):
        if nums[x] not in result:
            result.append(nums[x])
            
    return result
            

print(unicos([1,2,3,4,5,5,1,2,3]))