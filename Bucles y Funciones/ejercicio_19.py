def miembro_comun(els, els_two):
    for x in range(0, len(els)):
        for y in range(0, len(els_two)):
            if(els[x] == els_two[y]):
                return True
        
    return False


print(miembro_comun([1,2,3],[4,5,6])) #False
print(miembro_comun([1, "a", 2, "b"], [3, 4, "a", 5])) #True