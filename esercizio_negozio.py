import operator


def registrazione(nome_utente, pwd):
     while True:
            flag_nome_utente = False #inizializzo questa variabile come false. Se diventa true, vuol dire che il nome utente c'è già
            for i in range(len(utenti)):
                if nome_utente == utenti[i]:
                    print("Nome utente già in uso. Scegline un altro")
                    flag_nome_utente = True
                    nome_utente = input("Per favore, inserisci il tuo nuovo nome utente: ") #riscelgo il nome utente
            if flag_nome_utente == False:
                utenti.append(nome_utente) #aggiungo l'utente alla lista utenti
                break
     password.append(pwd)

def login (nome_login, password_login):
    for i in range(len(utenti)): #controllo se l'utente esiste
            if nome_login == utenti[i] and password_login == password[i]: #controllo se esiste nome utente e password
                return True #flaggo l'accesso e il ciclo non riinizia
    return False




utenti = ["admin"] #inizializzo delle variabili qui
password = ["admin"]
pwd_amministratore = "pippo"
poteri_amministratore = False
accesso = False

numero_articoli = [10,10,10]
quantità_comprata = [0,0,0]

articoli = ["smartphone", "camicia", "anello"] #gli articoli del mio sito
prezzo_articoli = [900, 70, 1200] #i loro prezzi
compratore = [] #metterò qui chi compra
oggetti_comprati = [] #e cosa compra

totale_utente = [] #e quanto spenderà ogni utente.


while True:
#iniziamo con la registrazione
    registrazione_check = int(input("Benvenuto sul nostro sito. Sei già registrato? Premi 1 per continuare con la registrazione, 2 per andare direttamente al login e 0 per uscire\n"))
    if registrazione_check == 1:
        nome_utente = input("Per favore, inserisci il tuo nuovo nome utente: ")
        pwd = input("Per favore, inserisci la tua password: ") #scelgo una password
        #chiamo la funzione registrazione
        registrazione(nome_utente,pwd)
    elif registrazione_check == 0:
        print("Grazie per averci visitato. Buona giornata!\n")
        break
    else:
        #andiamo al login. ora vediamo se sono utenti normali o amministratori.
        amministratore_check = int(input("Effettua il login al sito. Se sei un amministratore, premi 1, altrimenti premi 0\n"))
        if amministratore_check == 1:
            test_ingresso = input("Inserisci la password dell'amministratore. In caso di password errata, il sito si chiuderà\n") #controllo che l'utente sia davvero un amministratore
            if test_ingresso != pwd_amministratore:
                break
            else:
                poteri_amministratore = True #attivo i poteri di amministratore, che mi permetteranno di accedere a più funzionalità.
        nome_login = input("Inserisci il tuo nome con cui ti sei registrato: ") #andiamo ad inserire le credenziali
        password_login = input("Inserisci la password con cui ti sei registrato: ")

        accesso = login(nome_login, password_login) #funzione di login per vedere se l'utente esiste
        if accesso == False:
            print("Accesso negato. Per favore, registrati o rifai il login")
            continue
        else: #entro nel sito
            totale = 0
            acquisti = ""
            while True:
                
                if poteri_amministratore == False: #sono un cliente
                    #iniziamo a comprare o a guardare gli articoli
                    cosa_fare = int(input("Benvenuto! Cosa vuoi fare? Premi 1 per visualizzare gli articoli nell'inventario, premi 2 per acquistare articoli dall'inventario"
                                          ", premi 0 per uscire dal sito\n"))
                    if cosa_fare == 1: #guardo cosa sto vendendo
                        for i in range(len(articoli)):
                            print("Ci sono", numero_articoli[i], articoli[i], " ", prezzo_articoli[i], "euro ognuno\n")
                        continue
                    elif cosa_fare == 0: #esco dal sito
                        print("Grazie per essere stato con noi. Arrivederci\n")
                        break
                    else:
                        sto_comprando = input("Scrivi il nome dell'articolo che vorresti comprare. Se vuoi tornare al menù, digita 'esci', se vuoi andare al carrello"
                                              " digita 'carrello'\n")
                        if sto_comprando != "esci" and sto_comprando != "carrello" and sto_comprando in articoli:
                            compro = articoli.index(sto_comprando)
                        elif sto_comprando not in articoli and (sto_comprando != "esci" and sto_comprando != "carrello"):
                            print("Articolo non valido. Ritornerai alla pagina iniziale\n")
                            continue

                        if sto_comprando == "esci": #torno alla prossima iterazione del ciclo
                            continue
                        elif sto_comprando == "carrello":
                            print("Stai comprando: ", acquisti, "\n")
                            carrello = int(input("Premi 1 per confermare l'ordine, 0 per annullare e tornare al menù\n")) #procedo alla conferma ordine
                            if carrello == 1:
                                print("Ti ringrazio per l'acquisto. Ritornerai al menù principale.")
                                compratore.append(nome_login) #aggiungo il nome di chi compra
                                totale_utente.append(totale) #aggiungo il totale per utente
                                totale = 0
                                numero_articoli = list(map(operator.sub, numero_articoli, quantità_comprata)) #sottraggo la quantità comprata alla quantità presente
                                acquisti = ""
                            else:
                                for i in range(len(quantità_comprata)):
                                    quantità_comprata[i] = 0 #resetto la lista perché ho annullato il carrello
                                continue
                        else:
                            print("Quanti", articoli[compro], "desideri? Al momento ne sono presenti in negozio", numero_articoli[compro])
                            quantità = int(input())
                            if quantità < numero_articoli[compro]: #mi assicuro di avere gli oggetti nell'inventario
                                quantità_comprata[compro] += quantità #aggiungo alla lista quantità comprata, che mi servirà per rimuovere dal carrello
                                totale += quantità*prezzo_articoli[compro]
                                acquisti += " " +str(quantità) +" " + articoli[compro]
                                print("\nArticoli aggiunti al carrello! Torna nel carrello per confermare l'acquisto\n")
                            else:
                                print("Non ci sono abbastanza", articoli[compro], "\n")
                                continue

                else: #la parte dell'admin
                    guadagno = 0
                    cosa_fare = int(input("Benvenuto admin. Cosa vuoi fare? 1 per aggiungere un articolo, 2 per modificare gli articoli presenti,"
                                          " 3 per vedere i guadagni del sito, 4 per visualizzare l'inventario, 0 per uscire\n"))
                    if cosa_fare == 0:
                        break
                    elif cosa_fare == 4:
                        for i in range(len(articoli)):
                            print("Ci sono", numero_articoli[i], articoli[i], " ", prezzo_articoli[i], "euro ognuno\n")
                        continue
                    elif cosa_fare == 3:
                        for i in range(len(totale_utente)):
                            print( "L'utente", compratore[i], "ha speso", totale_utente[i]) #stampo l'utente che ha comprato e quanto ha speso
                            guadagno += totale_utente[i] #controllo il guadagno totale sommando ogni transazione
                        print("In totale, in negozio abbiamo guadagnato", guadagno, "euro.\n")
                    elif cosa_fare == 1:
                        nuovo_articolo = input("Inserire il nuovo articolo da aggiungere all'inventario. Digitare 'esci' per annullare\n")
                        if nuovo_articolo == "esci":
                            continue
                        nuovo_articolo_quantità = int(input("Quanti articoli inserire nell'inventario? "))
                        nuovo_articolo_prezzo = int(input("Qual è il prezzo del nuovo articolo? "))

                        articoli.append(nuovo_articolo) #ora aggiungo il nuovo articolo alla mia lista
                        prezzo_articoli.append(nuovo_articolo_prezzo)
                        numero_articoli.append(nuovo_articolo_quantità)
                        quantità_comprata.append(0) #non scordo di aggiungere 0 alla quantità comprata di articoli
                    elif cosa_fare == 2:
                        decisione = int(input("Premi 1 per rimuovere un oggetto, 2 per modificare la quantità di un oggetto, 3 per modificare il prezzo di un oggetto, 0 per tornare al menù\n"))
                        if decisione == 1: #rimuovo un oggetto
                            oggetto_da_rimuovere = input("Scrivi il nome dell'oggetto da rimuovere: ")
                            if oggetto_da_rimuovere not in articoli: #se non c'è tra gli articoli, torno al menù
                                print("Articolo non trovato. Tornerai al menù\n")
                                continue
                            indice_oggetto_da_rimuovere = articoli.index(oggetto_da_rimuovere) #trovo l'indice dell'oggetto da rimuovere
                            articoli.remove(oggetto_da_rimuovere) #tolgo l'oggetto
                            prezzo_articoli.remove(prezzo_articoli[indice_oggetto_da_rimuovere])
                            quantità_comprata.remove(quantità_comprata[indice_oggetto_da_rimuovere])
                            numero_articoli.remove(numero_articoli[indice_oggetto_da_rimuovere])
                        elif decisione == 0:
                            continue
                        elif decisione == 2:
                            oggetto_da_modificare = input("Scrivi il nome dell'oggetto da modificare: ")
                            if oggetto_da_modificare not in articoli: #se non c'è tra gli articoli, torno al menù
                                print("Articolo non trovato. Tornerai al menù\n")
                                continue
                            nuova_quantità = int(input("Scegli la nuova quantità: "))
                            indice_quantità_da_modificare = articoli.index(oggetto_da_modificare)
                            numero_articoli[indice_quantità_da_modificare] = nuova_quantità
                        elif decisione == 3:
                            oggetto_da_modificare = input("Scrivi il nome dell'oggetto da modificare: ")
                            if oggetto_da_modificare not in articoli: #se non c'è tra gli articoli, torno al menù
                                print("Articolo non trovato. Tornerai al menù\n")
                                continue
                            nuovo_prezzo = int(input("Scegli il nuovo prezzo: "))
                            indice_quantità_da_modificare = articoli.index(oggetto_da_modificare)
                            prezzo_articoli[indice_quantità_da_modificare] = nuovo_prezzo
                        else:
                            continue

#da implementare: funzioni generiche per comandi specifici



            










        
