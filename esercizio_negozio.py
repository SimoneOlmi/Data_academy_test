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
                        if sto_comprando != "esci" and sto_comprando != "carrello":
                            compro = articoli.index(sto_comprando)

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
                                continue
                        else:
                            print("Quanti", articoli[compro], "desideri? Al momento ne sono presenti in negozio", numero_articoli[compro])
                            quantità = int(input())
                            if quantità < numero_articoli[compro]:
                                quantità_comprata[compro] += quantità
                                totale += quantità*prezzo_articoli[compro]
                                acquisti += " " +str(quantità) +" " + articoli[compro]
                            else:
                                print("Non ci sono abbastanza", articoli[compro], "\n")
                                continue

                else: #la parte dell'admin
                    cosa_fare = int(input("Benvenuto admin. Cosa vuoi fare? 1 per aggiungere un articolo, 2 per modificare gli articoli presenti,"
                                          " 3 per vedere i guadagni del sito, 4 per visualizzare l'inventario, 0 per uscire"))
                    if cosa_fare == 0:
                        break
                    if cosa_fare == 4:
                        for i in range(len(articoli)):
                            print("Ci sono", numero_articoli[i], articoli[i], " ", prezzo_articoli[i], "euro ognuno\n")
                        continue




            










        
