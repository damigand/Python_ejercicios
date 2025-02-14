def divisores(n):
    numbers = []
    
    for x in range(1, n + 1):
        if(n % x == 0):
            numbers.append(x)
            
    return numbers


print(divisores(10))