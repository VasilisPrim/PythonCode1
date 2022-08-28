def checkinput():
    try:
        myRoute = int(input("Give an integer: "))

    except:                        #Υποθέτω οτι ο χρήστης ξέρει πόσες διαδρομές
        print("Incorrect input!")  #μπορεί να ακολουθήσει σε κάθε στάδιο ,πχ
        return None                #οτι αρχικά μπορεί να επιλέξει αριθμούς απο 
                                   #το 1 μέχρι το 3 ,μετά απο το 1 έως το 2 και
                                   #τέλος απο το 1 μέχρι το 4.
    return myRoute


route1=0
route2=0
route3=0
route = checkinput()

if route == 1:
    route1=route
    route = checkinput()
    if route==1:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
            
    else:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
        
    print(route1,"---->",route2,"---->",route3)            


elif route:
    route1=route
    route = checkinput()
    if route==1:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
            
    else:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
        
    print(route1,"---->",route2,"---->",route3)
    
    
    
else:
    route1=route
    route = checkinput()
    if route==1:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
            
    else:
        route2=route
        route = checkinput()
        if route == 1:
            route3=route
        elif route==2:
            route3=route
        elif route==3:
            route3=route
        else:
            route3=route
        
    print(route1,"---->",route2,"---->",route3)
        
        














    
