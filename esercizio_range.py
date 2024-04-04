numero = int(input("Inserisci il numero desiderato da cui vuoi far partire il countdown: ")) #chiedo il numero

selezione = 2 #inizializzo la selezione affinché mi entri nel secondo while

while True:
    for i in range(numero, -1, -1):
        print(i)
    while (selezione != 0 and selezione != 1): #check per controllare che il numero sia o 0 o 1
        selezione = int(input("Vuoi rifare il conto alla rovescia con un nuovo numero? Premi 1 per rifare l'esercizio, 0 per uscire dal programma\n"))
    if selezione == 0: #non voglio continuare
        print("Esco dal programma")
        break
    else: #rifaccio il ciclo
        numero = int(input("Inserisci il numero desiderato da cui vuoi far partire il countdown: "))
        selezione = 2 #inizializzo selezione ad un numero diverso da 0 e 1 per farlo rientrare nel secondo ciclo
    