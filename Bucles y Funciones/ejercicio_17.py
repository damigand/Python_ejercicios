def sum_cubos(num):
    digits = []
    num_str = str(num)
    
    for x in range(0, len(num_str)):
        digits.append(num_str[x])
    
    suma = 0
    for x in range(0, len(digits)):
        suma += int(digits[x])**2
        
    return suma
    
    
print(sum_cubos(25)) #29
print(sum_cubos(352)) #38