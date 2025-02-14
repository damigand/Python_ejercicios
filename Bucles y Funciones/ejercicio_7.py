def mayus_minus(string):
    mayus = 0
    minus = 0
    
    for x in range(0, len(string)):
        letter = string[x]
        if(letter.isalpha()):
            if(letter.isupper()):
                mayus += 1
            else:
                minus += 1
            
    return "mayúsculas: " + str(mayus) + "," + " minúsculas: " + str(minus)

print(mayus_minus("Hola")) #1, 3
print(mayus_minus("Hola, me llamo David")) #2, 14