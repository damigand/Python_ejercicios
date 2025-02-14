def binary(num):
    binary = bin(num)[2:]
    for x in range(1, 9 - len(binary)):
        binary = "0" + str(binary)
    
    return binary


print(binary(19))
