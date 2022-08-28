def fact(num):
    count = 2
    n=1
    while count<=num:
        n *= count
        count +=1
    return n


while True:
    try:
        myNum = int(input("Give an integer: "))
        print("The factorial of",myNum,"is:",fact(myNum))
        break
    except:
        print("Invalid input,please try again!")
        continue
    


        
    
