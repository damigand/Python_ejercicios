def reverse_list(els):
    reverseIndex = len(els) - 1
    reverseList = []
    
    for x in range(0, len(els)):
        reverseList.append(els[reverseIndex])
        reverseIndex -= 1
    
    return reverseList

print(reverse_list(["start",1,2,3,4,5, "end"]))