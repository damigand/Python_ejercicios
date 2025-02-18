def sin_duplicados(els):
    result = []
    for x in range(0, len(els)):
        if(els[x] not in result):
            result.append(els[x])
            
    return result


print(sin_duplicados([1,1,2,2,3,3,4,4,5,5])) #[1,2,3,4,5]