def elementos(els, n):
    result = []
    
    for x in range(0, n):
        result.append(els[x])
        
    return result

print(elementos([1,2,3,4,5], 3)) #[1,2,3]
print(elementos(["hola","me","llamo","David"], 2)) #["hola","me"]
print(elementos(["hola",1,"me",2,"llamo",3,"David",4], 5)) #["hola", 1, "me", 2, "llamo"]