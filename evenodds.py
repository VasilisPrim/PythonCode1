def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False



countEven = 0
countOdd = 0
count = 0

while True:
    
    try:
        myNum = int(input("Give a num: "))
        if myNum==0:
            break
        
        if isEven(myNum)== True:
            count+=1
            countEven += 1
        else:
            count+=1
            countOdd += 1

        percOfOdd = (countOdd/count)*100
        percOfEven = (countEven/count)*100
        
    except:
        print("You gave an invalid input!")
        continue
        




print("The percentage of odds is: %.2f%% and the percentage of even is: %.2f%%"%(percOfOdd,percOfEven))

