def caracteres(string):
    result = []
    for x in range(0, len(string)):
        exists = []
        for y in range(0, len(result)):
            if(string[x] in result[y]):
                exists.append(True)
                result[y][string[x]] += 1
        
        if(len(exists) < 1):
            result.append({string[x]: 1})
            
    
    return result


print(caracteres("Hola, me llamo David."))
print(caracteres("Esto es una frase con caracteres"))