# Creare una classe Vendite con all'interno  di questa classe ci metto una lista vuota che rappresenta l'importo totale per giorno. farò un metodo calcolo totale
# che sommerà ogni elemento della lista vendite per giorno. Farò un metodo calcola media, che calcolerà la media aritmetica di ogni elemento nella lista vendite totale.
# Farò un metodo che calcola il giorno di vendite massimo, restituendo il giorno e il valore in cui si è venduto di più.
# Farò poi una classe figlio Giorno. come attributi la classe giorno prenderà il giorno della vendita e l'importo del giorno. 
# Mi serve un metodo aggiungi vendite, che devo ancora decidere se mettere nella classe padre o nella classe figlio. Andrò comunque a richiamare questo metodo con un oggetto
# della classe figlio, aggiungendo il valore di vendita e il giorno.

class Vendite:

    

    def __init__(self):
        self.importo_per_giorno = []
        self.giorni_e_importi = {}

    def totale(self):
        totale = 0
        for i in range(len(self.importo_per_giorno)):
            totale += self.importo_per_giorno[i]
        return totale
    
    def media(self):
        totale = 0
        try:
            for i in range(len(self.importo_per_giorno)):
                totale += self.importo_per_giorno[i]
            return totale/len(self.importo_per_giorno)
        except ZeroDivisionError:
            print("Non ci sono elementi nella lista, impossibile fare la media")
 
    
    def vendite_massimo(self):
        temp = self.importo_per_giorno[0]
        giorno = 1
        for i in range(len(self.importo_per_giorno)-1):
            if self.importo_per_giorno[i]<self.importo_per_giorno[i+1]:
                temp = self.importo_per_giorno[i+1]
                giorno = i+2
        return [giorno, temp]
        
    
class Giorno(Vendite):

    def __init__(self, giorno, importo, vendite):
        self.giorno = giorno
        self.importo = importo
        self.vendite = vendite
    
    def aggiungi_vendite(self, importo):
        self.vendite.importo_per_giorno.append(importo)
    
    def registro_vendite(self, giorno, importo):
        self.vendite.giorni_e_importi[giorno] = importo



giorno = 1
totale = 0
vendite = Vendite()
test = Vendite()

while True:
    try:
        importo = int(input("Inserisci l'importo per il giorno "))
    except ValueError:
        print("Devi inserire un numero intero! riprova")
        continue
    else:
        totale += importo
    
    passo = input("Ci sono altri importi per la giornata?\n")
    if passo.lower() == 'no':
        x = Giorno(giorno, totale, vendite)
        x.aggiungi_vendite(totale)
        x.registro_vendite(giorno, totale)
        giorno += 1
        totale = 0
        esco = input("Ci sono altri giorni da inserire?\n")
        if esco.lower() == 'no':
            break


print(f"Di seguito elenchiamo il giorno con il relativo totale del giorno\n{vendite.giorni_e_importi}\nDi seguito, elenco il totale vendite: {vendite.totale()}\nDi seguito"
      f" elenco la media dei giorni: {vendite.media()}")

for i in range(len(vendite.importo_per_giorno)):
    if vendite.importo_per_giorno[i] > vendite.media():
        print("il giorno", i+1, "si è guadagnato sopra alla media, per un totale di:", vendite.importo_per_giorno[i])
        
print("Il giorno dove si sono guadagnati di più e il relativo importo sono:", vendite.vendite_massimo())