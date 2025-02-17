def letras_nums(string):
    letras = 0
    nums = 0
    string = string.replace(" ", "")
    
    num_chars = ["1","2","3","4","5","6","7","8","9","0"]
    
    for x in range(0, len(string)):
        if(string[x] in num_chars):
            nums += 1
        else:
            letras += 1
    
    return "letras: " + str(letras) + " | números: " + str(nums)


print(letras_nums("Me llamo David y tengo 21 años."))