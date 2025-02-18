def cadena_larga(els):
    cadena = ""
    for x in range(0, len(els)):
        if(len(els[x]) > len(cadena)):
            cadena = els[x]
    
    return cadena

print(cadena_larga(["ordenador","oftalmólogo","coche","fotografía"])) #oftalmólogo
print(cadena_larga(["hola","adiós", "buenos días", "buenas tardes"])) #buenas tardes