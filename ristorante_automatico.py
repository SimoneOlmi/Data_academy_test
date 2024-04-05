num_tavoli = 10 #numero massimo di tavoli

conteggio = 0

#inizializzo i clienti
clienti = []
tavoli = [*range(1,num_tavoli)]
torte = []
prezzo_torte = []

base = ["pan di spagna ", "Frolla ", "Soffice al Cioccolato "] #inizializzo le tre componenti della torta.
farcitura = ["Crema pasticcera ", "Marmellata di frutta ", "Crema al burro "]
topping = ["panna montata", "frutta fresca", "scaglie di cioccolato"]

prezzo_base = [2,4,6] #i prezzi delle tre componenti
prezzo_farcitura = [4,5,6]
prezzo_topping = [6,9,12]



#inizializzo il ciclo per il mio massimo di tavoli (5)
while conteggio < num_tavoli:

    base_temp = 3 #inizializzo le variabili temporanee per assicurarmi che nel secondo ciclo while entri
    farcitura_temp = 3
    topping_temp=3

    #inizializzo il nome dell'utente
    nome_cliente = input("Benvenuto nel ristorante! Per favore, inserisci il tuo nome: ")
    clienti.append(nome_cliente) #aggiungo ai clienti il nuovo cliente

    print("Benvenut* " + clienti[conteggio]+" il tuo tavolo è il numero ", tavoli[conteggio], "\n") #giusto un print di benvenuto
          
    print("Per favore, scegli tre ingredienti per la base della tua torta\n")

    #faccio un ciclo while per essere sicuro che il numero sia giusto (non deve essere un numero al di fuori dell'array)
    while (base_temp != 0 and base_temp !=1 and base_temp != 2) or (farcitura_temp != 0 and farcitura_temp !=1 and farcitura_temp != 2) or (topping_temp != 0 and topping_temp !=1 and topping_temp != 2):
        base_temp = int(input("Premi 0 per il pan di spagna, premi 1 per la frolla, premi 2 per il soffice al cioccolato ")) #scelgo i tre elementi
        farcitura_temp = int(input("Premi 0 per la crema pasticcera, premi 1 per la marmellata di frutta, premi 2 per la crema al burro "))
        topping_temp = int(input("Premi 0 per il pan di spagna, premi 1 per la frolla, premi 2 per il soffice al cioccolato "))

    prezzo_torte.append(prezzo_base[base_temp]+prezzo_farcitura[farcitura_temp]+prezzo_topping[topping_temp]) #aggiungo alla lista la nuova torta creata ed il relativo prezzo
    torte.append(base[base_temp]+farcitura[farcitura_temp]+topping[topping_temp])

    conteggio += 1 #aumento il numero del tavolo

    finito = int(input("\nCi sono altri clienti? Premi 1 se ci sono o 0 se non ci sono: "))
    if finito == 0:
        break


totale_prezzo = 0 #inizializzo il totale a zero, poi andrò a cambiare i valori nel for
totale_torte = 0

for i in range(len(torte)):
    print("Il cliente " + clienti[i] + " ha ordinato una torta con " + torte[i]+ " pagando", prezzo_torte[i], "euro")
    totale_prezzo += prezzo_torte[i]
    totale_torte += 1

print("In totale, abbiamo guadagnato", totale_prezzo, "euro, vendendo", totale_torte, "torte")