def primo(num):
    divisores = []
    for x in range(1, num + 1):
        if(num % x == 0):
            divisores.append(x)
        
        if(len(divisores) > 2):
            return False
    
    return True

print(primo(7)) # True
print(primo(6)) # False
print(primo(21)) # False
print(primo(23)) # True