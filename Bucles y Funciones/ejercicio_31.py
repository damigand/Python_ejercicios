def primos(n):
    nums = []

    index = 1

    while(len(nums) < n):
        divisores = []
        for x in range(1, index + 1):
            if(index % x == 0):
                divisores.append(x)
            
            if(len(divisores) > 2):
                break
        
        if(len(divisores) == 2):
            nums.append(index)
            
        index += 1
        
    return nums

print(primos(5)) #[2,3,5,7,11]
print(primos(10)) #[2,3,4,7,11,13,17,19,23,29]
        