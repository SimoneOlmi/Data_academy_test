"""
Creo una classe Ristorante. In questa classe ci metto un metodo __init__ con parametri: self, nome e tipo di cucina. ci metto
un booleano descrizione=False che mi flagga se la descrizione del ristorante è attiva o no. Ci metto poi un attributo di classe inizializzato 
False per flaggare il ristorante come chiuso. Creo poi un dizionario vuoto {} in cui andrò poi a mettere prezzo e piatto.
Creo un metodo apertura ristorante che mi cambia il flag del ristorante in True, un metodo chiusura che me lo setta a False, un metodo setta_descrizione
che mi setta la descrizione True, un metodo Togli_descrizione che mi mette la descrizione false. Poi metto un metodo stato_apertura che mi dice che il ristorante è
aperto se il parametro è True, il contrario se False. Aggiungi al menù sarà un metodo che prende come parametro il nome ed il prezzo del piatto e me lo inserisce nel dizionario
definito prima. La stessa cosa con il metodo togli dal menù, ma andrò a toglierlo. Infine, stampa menù stamperà tutte le chiavi del nome del piatto col rispettivo valore di prezzo. 

"""

class Ristorante:

    apertura = False
    descrizione = False

    #metodo costruttore con due parametri e un dizionario vuoto
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina

        self.menù = {}

    #metodo apertura ristorante che mi flagga True quando chiamato
    def apertura_ristorante(self):
        self.apertura = True

    #metodo chiusura ristorante che mi flagga false quando chiamato
    def chiusura_ristorante(self):
        self.apertura = False
    
    #metodo metti descrizione che mi flagga true quando chiamato
    def metti_descrizione(self):
        self.descrizione = True
    
    #metodo togli descrizione che mi flagga false quando chiamato
    def togli_descrizione(self):
        self.descrizione = False

    #iniziamo con lo stato dell'apertura del ristorante
    def stato_apertura(self):
        if self.apertura == True:
            print("Il ristorante è aperto! Benvenuto\n")
        elif self.apertura == False:
            print("Il ristorante è chiuso. Ci dispiace\n")

    #stampo la descrizione del ristorante, se il flag è true
    def descrizione_ristorante(self):
        if self.descrizione == True:
            print("Il Ristorante", self.nome,"è un'accogliente osteria situata nel cuore di una pittoresca piazza nel centro storico.\nOffriamo un'autentica esperienza culinaria" , self.tipo_cucina,"celebrando le tradizioni e i sapori della cucina casalinga", self.tipo_cucina,".\nCon ingredienti freschi e di alta qualità provenienti direttamente dai mercati locali, i nostri piatti sono preparati con cura e passione.\nDal classico risotto alla milanese alle fragranti pizze appena sfornate, ogni piatto è un omaggio alla ricca cultura gastronomica",self.tipo_cucina,".\nSiamo orgogliosi di offrire un ambiente familiare e accogliente, dove gli ospiti possono gustare piatti deliziosi e creare ricordi indimenticabili con amici e familiari.\nBenvenuti a", self.nome,", dove il buon cibo e la convivialità si incontrano!\n")
        else:
            print("Descrizione non disponibile al momento. Siate pazienti!\n")    

    #metodo per aggiungere piatti al menù
    def aggiungi_al_menù(self):
        nome_piatto = input("Inserisci il nome del piatto che vorresti aggiungere: ")
        prezzo = float(input("Inserisci il nome del prezzo del piatto aggiunto: "))
        self.menù[nome_piatto] = prezzo
    
    #metodo per rimuovere piatto dal menù
    def togli_dal_menù(self):
        nome_piatto = input("Inserisci il nome del piatto da rimuovere dal menù: ")
        if nome_piatto not in self.menù:
            print("Il piatto selezionato non è presente nel menù\n")
        else:
            del self.menù[nome_piatto]
    
    #metodo per stampare il menù
    def stampa_menù(self):
        for chiave, valore in self.menù.items():
            print(f"{chiave}: {valore}")

    #trasferisco il menù
    def copia_menù(self):
        return self.menù


#inizializzo tre ristoranti per il mio sito di cibo di consegna a casa
ristorante_vegetariano = Ristorante("NaturaSì", "vegetariana")

ristorante_italiano = Ristorante("Trattoria di Simi", "italiana")

ristorante_americano = Ristorante("McDonald", "americana")

#Apro i ristoranti
ristorante_vegetariano.apertura_ristorante()
ristorante_italiano.apertura_ristorante()
ristorante_americano.apertura_ristorante()

quantità_piatti_vegetariano = {}
quantità_piatti_italiano = {}
quantità_piatti_americano = {}
totale_ristoranti = [0,0,0]

#inizializzo un ciclo infinito in cui vado ad inserire i piatti del ristorante vegetariano
while True:
    print("Inserisci i piatti all'interno del ristorante vegetariano")
    ristorante_vegetariano.aggiungi_al_menù()
    esco = input("Se hai finito di inserire piatti, digita 'esci'\n")
    if esco.lower() == 'esci':
        break

menù_vegetariano = ristorante_vegetariano.copia_menù()
for chiave,valori in menù_vegetariano.items():
    quantità_piatti_vegetariano[chiave] = 10 #aggiungo 10 quantità per ogni piatto


totale = 0
#inizializzo un ciclo infinito in cui vado ad inserire i piatti del ristorante italiano
while True:
    print("Inserisci i piatti all'interno del ristorante italiano")
    ristorante_italiano.aggiungi_al_menù()
    esco = input("Se hai finito di inserire piatti, digita 'esci'\n")
    if esco.lower() == 'esci':
        break

menù_italiano = ristorante_italiano.copia_menù()
for chiave,valori in menù_italiano.items():
    quantità_piatti_italiano[chiave] = 10 #aggiungo 10 quantità per ogni piatto

while True:
    print("Inserisci i piatti all'interno del ristorante americano")
    ristorante_americano.aggiungi_al_menù()
    esco = input("Se hai finito di inserire piatti, digita 'esci'\n")
    if esco.lower() == 'esci':
        break

menù_americano = ristorante_americano.copia_menù()
for chiave,valori in menù_americano.items():
    quantità_piatti_americano[chiave] = 2 #aggiungo 10 quantità per ogni piatto

#il cliente è qua e ora decide cosa pappare
while True:
    seleziono_ristorante = input("Benvenuto sul nostro sito! Per favore, indica se desideri mangiare vegetariano, italiano o americano. Se desideri uscir dal sito, scrivi 'esci'\n")

    #se non vuole mangiare niente, esce
    if seleziono_ristorante.lower() == 'esci':
        break
    while True:
        #se sceglie il ristorante americano
        if seleziono_ristorante.lower() == 'americano':
            flag_americano = False
            for chiave,valore in menù_americano.items():
                if menù_americano[chiave] !=0: #se tutti sono nulli, il ristorante chiude
                    flag_americano = True #se almeno uno è diverso da zero, il ristorante rimane aperto
            if flag_americano == False:
                ristorante_americano.chiusura_ristorante() #chiudo il ristorante e torno indietro
                ristorante_americano.stato_apertura()
                break
            ristorante_americano.descrizione_ristorante()
            ristorante_americano.stato_apertura()
            ristorante_americano.stampa_menù()
            scelgo = input("Inserire il nome del piatto desiderato. Se non si vuole ordinare niente, scrivere 'indietro'") #scelgo il nome del piatto
            quantità = int(input("Quanti ne vuoi? ")) #seleziono la quantità
            if scelgo.lower() == 'indietro': #torno alla selezione dei ristoranti
                break
            else:
                if quantità < quantità_piatti_americano.get(scelgo): #se la quantità è minore della quantità presente
                    prezzo_piatto = menù_americano.get(scelgo)
                    totale += prezzo_piatto
                else:
                    print("Non ci sono abbastanza porzioni. Provare con un nuovo ordine\n")
                    continue
            
                
        # elif seleziono_ristorante.lower() == 'vegetariano':
        #     ristorante_vegetariano.descrizione_ristorante()
        #     ristorante_vegetariano.stato_apertura()
        #     ristorante_vegetariano.stampa_menù()

