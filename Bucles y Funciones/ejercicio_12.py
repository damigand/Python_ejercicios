def fizz_buzz():
    for x in range(1, 51):
        string = ""
        if(x % 3 == 0):
            string += "Fizz"
        
        if( x % 5 == 0):
            string += "Buzz"
        
        if(len(string) < 1):
            string = x
        
        print(string)
        
    
fizz_buzz()