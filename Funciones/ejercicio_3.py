def primo(n):
    number = int(n / 2)
    
    for x in range(2, number + 1):
        if(n % x == 0):
            return str(n) + " no es primo"
    
    return str(n) + " es primo"

print(primo(12))