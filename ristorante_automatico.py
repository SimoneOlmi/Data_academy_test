num_tavoli = 2 #numero massimo di tavoli

conteggio = 0

#inizializzo i clienti
clienti_ristorante = []
clienti_asporto = []
tavoli = [*range(1,num_tavoli+1)]
torte_ristorante = []
torte_asporto = []
prezzo_torte_ristorante = []
prezzo_torte_asporto = []


base = ["pan di spagna ", "Frolla ", "Soffice al Cioccolato "] #inizializzo le tre componenti della torta.
farcitura = ["Crema pasticcera ", "Marmellata di frutta ", "Crema al burro "]
topping = ["panna montata", "frutta fresca", "scaglie di cioccolato"]

prezzo_base = [2,4,6] #i prezzi delle tre componenti
prezzo_farcitura = [4,5,6]
prezzo_topping = [6,9,12]



#inizializzo il ciclo per il mio massimo di tavoli (5)
#while conteggio < num_tavoli:
while True:
    base_temp = 3 #inizializzo le variabili temporanee per assicurarmi che nel secondo ciclo while entri
    farcitura_temp = 3
    topping_temp=3

    asporto = False #inizializzo il falso qui, per switchare tra le due possibilità


    #inizializzo il nome dell'utente
    nome_cliente = input("Benvenuto nel ristorante! Per favore, inserisci il tuo nome: ")
    
    #asporto o ristorante?
    if conteggio >= num_tavoli:
        print("Tutti i tavoli sono pieni, ordinerai da asporto e mangerai a casa\n")
        clienti_asporto.append(nome_cliente) #aggiungo ai clienti il nuovo cliente
        asporto = True
    else:
        clienti_ristorante.append(nome_cliente) #aggiungo ai clienti il nuovo cliente
        print("Benvenut* " + clienti_ristorante[conteggio]+" il tuo tavolo è il numero ", tavoli[conteggio], "\n") #giusto un print di benvenuto
          
    print("Per favore, scegli tre ingredienti per la base della tua torta\n")

    #faccio un ciclo while per essere sicuro che il numero sia giusto (non deve essere un numero al di fuori dell'array)
    while (base_temp != 0 and base_temp !=1 and base_temp != 2) or (farcitura_temp != 0 and farcitura_temp !=1 and farcitura_temp != 2) or (topping_temp != 0 and topping_temp !=1 and topping_temp != 2):
        base_temp = int(input("Premi 0 per il pan di spagna, premi 1 per la frolla, premi 2 per il soffice al cioccolato ")) #scelgo i tre elementi
        farcitura_temp = int(input("Premi 0 per la crema pasticcera, premi 1 per la marmellata di frutta, premi 2 per la crema al burro "))
        topping_temp = int(input("Premi 0 per la panna montata, premi 1 per la frutta fresca, premi 2 per le scaglie al cioccolato "))
        print("\nHai scelto una torta con una base di " + base[base_temp] + ", con una farcitura di " + farcitura[farcitura_temp] +" e un topping con " + topping[topping_temp])
        cambio = 2 #inizializzo il cambio qui per fare un check sul ciclo while e vedere se voglio cambiare ordine
        while cambio != 0 and cambio != 1:
            cambio = int(input("\nConfermi l'ordine o preferisci riselezionare gli ingredienti? Premi 1 se confermi, 0 se vuoi riselezionare gli ingredienti: "))
        if cambio == 0:
            base_temp = 3 #non esco dal ciclo while e riseleziono gli ingredienti
            farcitura_temp = 3
            topping_temp=3


    if asporto == False:
        prezzo_torte_ristorante.append(2+prezzo_base[base_temp]+prezzo_farcitura[farcitura_temp]+prezzo_topping[topping_temp]) #aggiungo alla lista la nuova torta creata ed il relativo prezzo
        torte_ristorante.append(base[base_temp]+farcitura[farcitura_temp]+topping[topping_temp])
    else:
        prezzo_torte_asporto.append(prezzo_base[base_temp]+prezzo_farcitura[farcitura_temp]+prezzo_topping[topping_temp]) #aggiungo alla lista la nuova torta creata ed il relativo prezzo
        torte_asporto.append(base[base_temp]+farcitura[farcitura_temp]+topping[topping_temp])

    conteggio += 1 #aumento il numero del tavolo

    finito = int(input("\nCi sono altri clienti? Premi 1 se ci sono o 0 se non ci sono: "))
    if finito == 0:
        break

   
totale_prezzo_ristorante = 0 #inizializzo il totale a zero, poi andrò a cambiare i valori nel for
totale_prezzo_asporto = 0
totale_torte = 0

for i in range(len(torte_ristorante)):
    #print("Il cliente " + clienti_ristorante[i] + " ha ordinato una torta con " + torte_ristorante[i]+ " pagando", prezzo_torte_ristorante[i], "euro")
    totale_prezzo_ristorante += prezzo_torte_ristorante[i]
    totale_torte += 1

for i in range(len(torte_asporto)):
    #print("Il cliente " + clienti_ristorante[i] + " ha ordinato una torta con " + torte_ristorante[i]+ " pagando", prezzo_torte_ristorante[i], "euro")
    totale_prezzo_asporto += prezzo_torte_asporto[i]
    totale_torte += 1


print("In totale, abbiamo guadagnato", totale_prezzo_ristorante, "euro al ristorante e", totale_prezzo_asporto, "euro da asporto, vendendo", totale_torte, "torte")
