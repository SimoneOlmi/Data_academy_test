class Punto:

    def __init__(self, x, y):

        self.x = x #li metto perché non voglio un punto iniziale nell'origine
        self.y = y

    def muovi(self, dx, dy): #muovo il punto iniziale

        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):
        
        return (self.x**2+self.y**2)**(0.5) #calcolo la distanza del punto dall'origine
    


class Libro:

    def __init__(self, titolo, autore, pagine): #inizializzo gli attributi
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine") #stampo la descrizione







#seleziono le coordinate del punto di partenza
x = int(input("Seleziona la x del punto di partenza: "))
y = int(input("Seleziona la y del punto di partenza: "))

punto = Punto(x,y) #chiamo punto l'oggetto di coordinate x,y

#seleziono di quanto voglio spostare le coordinate del punto
dx = int(input("Scegli di quanto muovere il punto lungo l'asse delle x: "))
dy = int(input("Scegli di quanto muovere il punto lungo l'asse delle y: "))

#muovo il punto in maniera permanente
punto.muovi(dx,dy)

#stampo la distanza dall'origine
print("La distanza dall'origine del punto è\n")

print(punto.distanza_da_origine())



#chiamo l'oggetto moby dick con titolo moby dick, autore melville, e pagine 800
moby_dick = Libro("Moby Dick", "Melville", "800")

#stampo la descrizione
moby_dick.descrizione()