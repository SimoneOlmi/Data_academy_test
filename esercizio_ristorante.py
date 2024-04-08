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
            print("Descrizione non disponibile al momento. Siate pazienti\n")    

    #metodo per aggiungere piatti al menù
    def aggiungi_al_menù(self):
        nome_piatto = input("Inserisci il nome del piatto che vorresti aggiungere: ")
        prezzo = int(input("Inserisci il nome del prezzo del piatto aggiunto: "))
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
        print(self.menù)



test = Ristorante("Trattoria di Simi", "Italiana")

test.metti_descrizione()

test.descrizione_ristorante()

test.togli_descrizione()

test.stato_apertura()

test.apertura_ristorante()

test.aggiungi_al_menù()

test.stampa_menù()

test.stato_apertura()