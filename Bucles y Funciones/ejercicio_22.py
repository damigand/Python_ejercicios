def suma_nums(nums):
    suma = 0
    for x in range(0, len(nums)):
        suma += nums[x]
    
    return suma


print(suma_nums([1,2,43,34,21,53])) #154