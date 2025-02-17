def ascendente(els):
    is_sorted = False
    #uso una variable para controlar que el array esté ordenado.
    while(not is_sorted):
        is_sorted = True
        #itero el array en cada iteración del while.
        for x in range(0, len(els)):
            #Este if evita que "els[x +1]" esté fuera de límites
            if(x < len(els) - 1):
                #Si el numero anterior es mayor al siguiente, no está ordenado
                if(els[x] > els[x + 1]):
                    #lo ordeno y cambio la variable del bucle "while" a false para que repita
                    temp = els[x]
                    els[x] = els[x + 1]
                    els[x + 1] = temp
                    is_sorted = False
    
    return els
        


print(ascendente([2,5,15,3,1,36,32,23,4,34,5,43,6,55,54,23,2,45,34]))