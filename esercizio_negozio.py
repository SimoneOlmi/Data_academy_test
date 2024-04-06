

utenti = ["admin"] #inizializzo delle variabili qui
password = ["admin"]
pwd_amministratore = "pippo"
poteri_amministratore = False
accesso = False

numero_articoli = [10,10,10]

articoli = ["smartphone", "camicia", "anello"] #gli articoli del mio sito
prezzo_articoli = [900, 70, 1200] #i loro prezzi
compratore = [] #metterò qui chi compra
oggetti_comprati = [] #e cosa compra

totale_utente = [] #e quanto spenderà ogni utente.


while True:
#iniziamo con la registrazione
    registrazione_check = int(input("Benvenuto sul nostro sito. Sei già registrato? Premi 1 per continuare con la registrazione, 0 per andare direttamente al login e 2 per uscire\n"))
    if registrazione_check == 1:
        nome_utente = input("Per favore, inserisci il tuo nuovo nome utente: ")
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
        pwd = input("Per favore, inserisci la tua password: ") #scelgo una password
        password.append(pwd)
    elif registrazione_check == 2:
        break
    else:
        #andiamo al login. ora vediamo se sono utenti normali o amministratori.
        amministratore_check = int(input("Effettua il login al sito. Se sei un amministratore, premi 1\n"))
        if amministratore_check == 1:
            test_ingresso = input("Inserisci la password dell'amministratore. In caso di password errata, il sito si chiuderà\n") #controllo che l'utente sia davvero un amministratore
            if test_ingresso != pwd_amministratore:
                quit()
            else:
                poteri_amministratore = True #attivo i poteri di amministratore, che mi permetteranno di accedere a più funzionalità.
        nome_login = input("Inserisci il tuo nome con cui ti sei registrato: ")
        password_login = input("Inserisci la password con cui ti sei registrato: ")
        for i in range(len(utenti)): #controllo se l'utente esiste
            if nome_login == utenti[i] and password_login == password[i]: #controllo se esiste nome utente e password
                accesso = True #flaggo l'accesso e il ciclo non riinizia
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
                        compro = int(input("Cosa vuoi comprare? Premi 1 per lo smartphone, premi 2 per la camicia, premi 3 per l'anello, premi 4 per confermare l'ordine, premi 0 per annullare\n"))
                        if compro == 0: #torno alla prossima iterazione del ciclo
                            continue
                        elif compro == 1: #compro smartphone
                            quantità = int(input("Quanti smartphone vuoi?"))
                            if quantità < numero_articoli[0]: #ci sono abbastanza smartphone
                                numero_articoli[0] -= quantità
                                totale = quantità * prezzo_articoli[0] #aggiungo al totale il prezzo
                                acquisti += str(quantità) + articoli[0]
                            else:
                                print("Non ci sono abbastanza smartphone\n")
                                continue
                        elif compro == 2:
                            quantità = int(input("Quante camicie vuoi?")) #compro camicie
                            if quantità < numero_articoli[1]:
                                numero_articoli[1] -= quantità
                                totale = quantità * prezzo_articoli[1]
                                acquisti += str(quantità) + articoli[1]
                            else:
                                print("Non ci sono abbastanza camicie\n")
                                continue
                        elif compro == 3:
                            quantità = int(input("Quanti anelli vuoi?")) #compro anelli
                            if quantità < numero_articoli[2]:
                                numero_articoli[2] -= quantità
                                totale = quantità * prezzo_articoli[2]
                                acquisti += str(quantità) + articoli[2]
                            else:
                                print("Non ci sono abbastanza anelli\n")
                                continue
                        else:
                            print("Stai comprando: ", acquisti, "\n")
                            carrello = int(input("Premi 1 per confermare l'ordine, 0 per annullare e tornare al menù\n")) #procedo alla conferma ordine
                            if carrello == 1:
                                print("Ti ringrazio per l'acquisto. Ritornerai al menù principale.")
                                compratore.append(nome_login)
                                totale_utente.append(totale)
                            else:
                                continue



            










        
