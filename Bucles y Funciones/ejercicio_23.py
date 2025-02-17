def comun(els):
    contador = []
    #en "contador" almaceno cada clave y las veces que se repite
    for x in range(0, len(els)):
        exists = []
        for y in range(0, len(contador)):
            if(els[x] in contador[y]):
                exists.append(True)
                contador[y][els[x]] += 1
        
        if(len(exists) < 1):
            contador.append({els[x]: 1})
    
    #compruebo "contador" y voy accediendo a los valores para ver cual se repite más.
    number = 0
    element = ""
    for x in range(0, len(contador)):
        for clave, valor in contador[x].items():
            if(valor > number):
                number = valor
                element = clave
    
    return element

lista = ["hola", 1, "adios", 2, "hola", 2, "adios", 2, "hola", 1, "adios"]
print(comun(lista))