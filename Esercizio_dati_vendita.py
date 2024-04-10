# Creare una classe Vendite con all'interno  di questa classe ci metto una lista vuota che rappresenta l'importo totale per giorno. farò un metodo calcolo totale
# che sommerà ogni elemento della lista vendite per giorno. Farò un metodo calcola media, che calcolerà la media aritmetica di ogni elemento nella lista vendite totale.
# Farò un metodo che calcola il giorno di vendite massimo, restituendo il giorno e il valore in cui si è venduto di più.
# Farò poi una classe figlio Giorno. come attributi la classe giorno prenderà il giorno della vendita e l'importo del giorno. 
# Mi serve un metodo aggiungi vendite, che devo ancora decidere se mettere nella classe padre o nella classe figlio. Andrò comunque a richiamare questo metodo con un oggetto
# della classe figlio, aggiungendo il valore di vendita e il giorno.

class Vendite:

    
    # inizializzo una lista vuota dove farò operazioni e un dizionario vuoto che andrò poi a stampare
    def __init__(self):
        self.importo_per_giorno = []
        self.giorni_e_importi = {}
    #qui svolgo il totale della lista una volta che è riempita
    def totale(self):
        totale = 0
        for i in range(len(self.importo_per_giorno)):
            totale += self.importo_per_giorno[i]
        return totale
    #qui svolgo la media della lista una volta che riempita. Se Vuota, mi ritorna None
    def media(self):
        totale = 0
        try:
            for i in range(len(self.importo_per_giorno)):
                totale += self.importo_per_giorno[i]
            return totale/len(self.importo_per_giorno)
        except ZeroDivisionError:
            print("Non ci sono elementi nella lista, impossibile fare la media")
 
    #Trova il giorno ed il valore in cui le vendite sono state massime
    def vendite_massimo(self):
        temp = self.importo_per_giorno[0]
        giorno = 1
        for i in range(len(self.importo_per_giorno)-1):
            if self.importo_per_giorno[i]<self.importo_per_giorno[i+1]:
                temp = self.importo_per_giorno[i+1]
                giorno = i+2
        return [giorno, temp]
        
    
class Giorno(Vendite):
    #inizializzo con giorno e importo. Ho dovuto aggiungere l'oggetto vendite perché altirmenti non mi vedeva le liste e i dizionari della classe padre
    def __init__(self, giorno, importo, vendite):
        self.giorno = giorno
        self.importo = importo
        self.vendite = vendite
    #qui ho dovuto usare vendite come oggetto per poter appendere valori alla lista. Il valore che appendo lo passo da importo
    def aggiungi_vendite(self, importo):
        self.vendite.importo_per_giorno.append(importo)
    #qui ho dovuto usare vendite come oggetto per poter accedere al dizionario della classe padre, ed aggiungo giorno ed importo relativo
    def registro_vendite(self, giorno, importo):
        self.vendite.giorni_e_importi[giorno] = importo



giorno = 1 #inizializzo il primo giorno
totale = 0 #inizializzo il totale con 0
vendite = Vendite() #oggetto che andrà a modificare la classe
test = Vendite() #oggetto di debug

while True:
    try: #qui uso try per assicurarmi che sto passando un valore intero
        importo = int(input("Inserisci l'importo per il giorno "))
    except ValueError: #se non è intero, stampa questo e rincomincia il ciclo
        print("Devi inserire un numero intero! riprova")
        continue
    else:
        totale += importo #aggiungo al totale l'importo del giorno
    
    passo = input("Ci sono altri importi per la giornata?\n")
    if passo.lower() == 'no': #se non ci sono altri importi per la giornata, definisco l'oggetto di Giorno e aggiungo alle liste/dizionari il totale ed il giorno
        x = Giorno(giorno, totale, vendite)
        x.aggiungi_vendite(totale)
        x.registro_vendite(giorno, totale)
        giorno += 1 #aumento il giorno di 1
        totale = 0 #resetto il totale
        esco = input("Ci sono altri giorni da inserire?\n") #condizione di uscita
        if esco.lower() == 'no':
            break



#qui stampo varie quantità: totale, media, il dizionario, i giorni in cui l'importo supera la media ed il valore massimo
print(f"Di seguito elenchiamo il giorno con il relativo totale del giorno\n{vendite.giorni_e_importi}\nDi seguito, elenco il totale vendite: {vendite.totale()}\nDi seguito"
      f" elenco la media dei giorni: {vendite.media()}")

for i in range(len(vendite.importo_per_giorno)):
    if vendite.importo_per_giorno[i] > vendite.media():
        print("il giorno", i+1, "si è guadagnato sopra alla media, per un totale di:", vendite.importo_per_giorno[i])
        
print("Il giorno dove si sono guadagnati di più e il relativo importo sono:", vendite.vendite_massimo())