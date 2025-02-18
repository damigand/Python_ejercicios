def promedio(nums):
    suma = 0
    range_nums = len(nums)
    
    for x in range(0, range_nums):
        suma += nums[x]
    
    return suma / range_nums

print(promedio([1,2,3,4,5])) #3
print(promedio([10,20,30])) #20