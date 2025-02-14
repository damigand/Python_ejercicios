def fibonacci(n):
    current = 1
    nextNumber = 2
    for x in range(1, n + 1):
        print (current)
        
        suma = current + nextNumber
        current = nextNumber
        nextNumber = suma
        
        
    return "done"
        


print(fibonacci(10))