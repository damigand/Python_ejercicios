def suma(nums):
    suma = 0
    for x in range(len(nums)):
        suma += nums[x]
    
    return suma

print(suma([3,5,10,12,5]))