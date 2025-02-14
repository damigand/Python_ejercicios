def perfectNumber(num):
    number = int(num / 2)
    divisores = []
    
    for x in range (1, number + 1):
        if(num % x == 0):
            divisores.append(x)
    
    suma = 0
    for x in range(0, len(divisores)):
        suma += divisores[x]
    
    if(suma == num):
        return "Perfecto"
    
    return "No perfecto"


print(perfectNumber(6)) #Perfecto
print(perfectNumber(10)) #No perfecto
print(perfectNumber(25)) #No perfecto
print(perfectNumber(28)) #Perfecto