def sumaDigitos(nums):
    suma = 0
    digits = str(nums)
    
    for x in range(0, len(str(nums))):
        digit = digits[x]
        suma += int(digit)
        
    return suma


print(sumaDigitos(53)) #8
print(sumaDigitos(194)) #14
print(sumaDigitos(432243)) #18