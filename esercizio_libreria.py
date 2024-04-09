# Creo una classe libreria. creo al suo interno un attributo catalogo, un dizionario con chiave isbn e valori autore e titolo (lista dentro dizionario). aggiungo il metodo 
# aggiungi libro, che andrà ad associarmi un nuovo isbn unico (checko con un if se è già presente un isbn uguale all'interno) legato a valori titolo e autore.
# rendo libro padre di libreria? Da pensarci
# rimuovi libro è come aggiungi libro, ma cerco per chiave del dizionario 
# cerca per titolo creo un ciclo for per la lunghezza di tutti i miei libri e cerco se il titolo è == al mio input. questo metodo ha un parametro titolo_cercato
# creo una classe libro con init titolo, autore, isbn. Fare un metodo print che stampa i tre parametri. 



        

class Libreria:
    


    catalogo = {}

    def aggiungi_libro(self, libro):

        if libro.isbn not in self.catalogo:
            self.catalogo[libro.isbn] = [libro.titolo, libro.autore]
        
        else:
            print("Il libro è già presente nel catalogo.")
    
    def rimuovi_libro(self, isbn):
        if isbn in self.catalogo:
            del self.catalogo[isbn]
        else:
            print("Il libro non è presente nel catalogo")
    
    def cerca_per_titolo(self, titolo):
        lista_libri = {}
        for chiave,valore in self.catalogo.items():
            if titolo == self.catalogo[chiave][0]:
                lista_libri[chiave] = titolo
        return lista_libri
    
    def mostra_catalogo(self):
        print("Catalogo della libreria:")
        for isbn, info in self.catalogo.items():
            print(f"Titolo: {info[0]}, Autore: {info[1]}, ISBN: {isbn}")


class Libro (Libreria):
    
    def __init__(self, titolo, autore, isbn):
        self.titolo  = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f"Il libro {self.titolo}, scritto da {self.autore}, ha codice identificativo: {self.isbn}")



isbn = 0
while True:
    print("Inseriamo dei libri nel nostro catalogo, prima di aprire la libreria agli utenti\n")
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    isbn +=1

    book = Libro(titolo, autore, isbn)

    book.aggiungi_libro(book)

    esco = input("Vuoi aggiungere un altro libro? ")
    if esco.lower() == 'no':
        break

while True:
    scelgo = input("Benvenuto nella nostra libreria!\nPuoi visualizzare il nostro catalogo col comando 'catalogo'\nPuoi cercare un libro nella nostra libreria col comando 'cerca'\n"
                   "Puoi uscire dal nostro sito col comando 'esci'\n")
    if scelgo.lower() == 'esci':
        print("Grazie per essere stato con noi. Alla prossima!")
        break
    elif scelgo.lower() == 'catalogo':
        book.mostra_catalogo()
    elif scelgo.lower() == 'cerca':
        cerco = input("Inserisci il titolo che stai ricercando: ")
        print(book.cerca_per_titolo(cerco))
    else:
        print("Comando non valido. Ritornerai alla pagina di inizio")
        continue







