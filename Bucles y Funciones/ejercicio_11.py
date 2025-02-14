def palindromo(string):
    string = string.replace(" ", "")
    string = string.lower()
    
    end = len(string) - 1
    
    string_range = int(len(string) / 2)
    for start in range(0, string_range):
        if(string[start] != string[end]):
            return "No palíndromo"
        
        end -= 1
    
    return "Palíndromo"



        
        
        
        
        
print(palindromo("Arriba la birra"))
print(palindromo("Me llamo David"))
print(palindromo("Esto no es un palíndromo"))
print(palindromo("reconocer"))