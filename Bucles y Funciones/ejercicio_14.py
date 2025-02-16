def isLonger(els, n):
    result = []
    for x in range(0, len(els)):
        if(len(els[x]) > n):
            result.append(els[x])
    
    return result


print(isLonger(["hola","David","ordenador", "dos", "armario"], 4)) #["David", "ordenador", "armario"]