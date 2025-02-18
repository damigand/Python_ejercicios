def palabras(string):
    result = []
    array = string.split(" ")
    
    for x in range(0, len(array))[::-1]:
        result.append(array[x])
    
    return result

print(palabras("hola me llamo David")) #["David", "llamo", "me", "hola"]