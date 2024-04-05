def fibonacci(numero):
    #il numero deve essere maggiore di 0
    if numero == 0:
        print("Errore, il numero deve essere maggiore di zero") 
    
    #caso il numero sia solo il primo
    elif range == 1:
        print(1)
    #caso il numero siano i primi due
    elif numero == 2:
        for i in range(2):
            print(1)
    #tutti gli altri casi
    else:
        totale_temp = 1
        temp = 1  
        for i in range(2):
            print(1)
        for i in range(2,numero):
            totale = totale_temp + temp
            print(totale)
            temp = totale_temp
            totale_temp = totale




#fibonacci(2)
#fibonacci(5)
fibonacci(10)
