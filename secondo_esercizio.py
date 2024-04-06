def isprime(numero):
    temp = 0

    if numero == 1:
        return 1
    for i in range(2, numero//2+1): #checko se il numero è primo con questo ciclo for e salvo il primo divisore
        if numero%i == 0:
            temp = i
            break
    return temp

utente = []
numeri_primi = []
while True:
    nome = input("Per favore, inserisci il tuo nome: ")
    numero = int(input("\nScegli un numero per vedere se è primo: ")) #inizializzo nome e chiedo il numero da controllare


    check = isprime(numero) #salvo il flag della funzione

    if check == 0: #se non ha salvato niente, mi dà 0 e quindi il numero è primo e lo salvo
        print(numero, "è un numero primo!\n")
        utente.append(nome)
        numeri_primi.append(numero)

    else: #altrimenti, printo dal divisore più piccolo, fino al numero più 1 a passo di divisore più piccolo
        for i in range(check, numero+1, check):
            print(i)
    

    esco = int(input("Vuoi scegliere un altro numero? Premi 1 per continuare, 0 per uscire\n")) #condizione di uscita
    if esco == 0:
        break


for i in range(len(utente)):
    print("Il numero primo scelto da", utente[i], "è:", numeri_primi[i])