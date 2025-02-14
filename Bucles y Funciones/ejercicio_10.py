def interseccion(els_one, els_two):
    result = []
    
    for x in range(0, len(els_one)):
        if(els_one[x] in els_two):
            result.append(els_one[x])
            
    return result



print(interseccion([1,2,3],[1,3])) #[1, 3]
print(interseccion([1,2,3,4,5],[2,5])) #[2, 5]
print(interseccion([1,2,3, 7, 10],[1,2, 5, 10])) #[1, 2, 10]