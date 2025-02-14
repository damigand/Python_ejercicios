def reverse(string):
    reverseString = ""
    
    for x in range(0, len(string))[::-1]:
        reverseString += string[x]
        
    return reverseString

print(reverse("hola"))