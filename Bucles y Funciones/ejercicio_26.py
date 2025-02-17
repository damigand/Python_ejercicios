def diferencias(els, els_two):
    result = []
    for x in range(0, len(els)):
        if(els[x] not in els_two):
            result.append(els[x])
    
    for x in range(0, len(els_two)):
        if(els_two[x] not in els):
            result.append(els_two[x])
    
    return result


print(diferencias([1,2,3],[2,3,4])) #[1, 4]