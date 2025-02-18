def suma_cuadrados(num):
    suma = 0
    for x in range(0, num + 1):
        if(x % 2 == 0):
            suma += x**2
    
    return suma

print(suma_cuadrados(5)) #20
print(suma_cuadrados(6)) #56