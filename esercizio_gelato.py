class Gelateria:

    opzioni = {"cono": 2.50, "coppetta": 3.00, "vaschetta da 1 kg": 8.00}

    def __init__(self):
        pass


    def visualizza_opzioni(self):
        print("Opzioni disponibili:\n")
        for chiave,valore in self.opzioni.items():
            print(f"{chiave}: {valore} euro")

    def totale_pagato(self, nome):
        print(f"Hai speso {self.opzioni[nome]} euro per la tua scelta")

    def benvenuto(self):
        print ("Benvenuto nella Gelateria. Puoi visualizzare le opzioni di vendita, scegliere gusti e vedere quanto hai pagato\n")
    

class Gusto (Gelateria):

    def __init__(self, gusti):
        super().__init__()
        self.gusti = list(gusti)
    
    def stampa_gusti(self):
        print("Gusti scelti:")
        for gusto in self.gusti:
            print(gusto)
    
    def scelta_gelato(self):
        print("Scegli i gusti che vuoi nel tuo gelato\n")
        for i in range(3):
            gusto = input(f"Scrivi il {i+1}o gusto: ")
            self.gusti.append(gusto)



x = Gusto([])


while True:
    x.benvenuto()
    scelta = input("Scrivi 'opzioni' per controllare le opzioni con i relativi prezzi.\nScrivi l'opzione scelta per sceglierla.\nScrivi 'esci' per uscire\n")
    if scelta.lower() == "esci":
        print("Arrivederci! Grazie per averci visitato\n")
        break
    elif scelta.lower() == 'opzioni':
        x.visualizza_opzioni()
    else:
        x.scelta_gelato()
        print("Hai scelto", scelta)
        x.stampa_gusti()
        x.totale_pagato(scelta)
        

