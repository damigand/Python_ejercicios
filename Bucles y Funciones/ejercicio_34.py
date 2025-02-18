def vocales(string):
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    contador = 0
    for x in range(0, len(string)):
        if(string[x] in vocales):
            contador += 1
    
    return str(contador) + " vocales."

print(vocales("Hola, me llamo David")) #7 vocales.