def vocales(string):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    
    for x in range(0, len(string)):
        if(string[x] in vocales):
            count += 1
            
    return str(count) + " vocales"


print(vocales("hola")) #2
print(vocales("hola me llamo David")) #7
print(vocales("Ahora voy")) #4