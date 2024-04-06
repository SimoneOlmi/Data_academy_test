#definisco le 3 aree con 3 funzioni diverse
def area_triangolo(base,altezza):
    return base*altezza/2

def area_rettangolo(base,altezza):
    return base*altezza

def area_quadrato(lato):
    return lato**2

aree = []

while True:
    esco = int(input("Benvenuto nel programma! Vuoi fare dei calcoli di aree o uscire dal programma? Premi 1 per la prima opzione, 0 per uscire\n")) #condizione di uscita
    if esco == 0:
        break
    else:
        base = float(input("Selezione la base della tua figura geometrica: ")) #inizializzo base ed altezza (per il quadrato, la base sarà il lato)
        altezza = float(input("\nSeleziona l'altezza della tua figura geometrica: "))

        figura = int(input("Quale area vuoi calcolare? Scegli 1 per il triangolo, 2 per il rettangolo e 3 per il quadrato\n")) #scelgo la figura

        if figura == 1: #in base alla figura scelta, calcolo l'area
            area = area_triangolo(base,altezza)
            print("L'area del triangolo è: ", area_triangolo(base,altezza), "cm quadri")

        elif figura == 2:
            area = area_rettangolo(base,altezza)
            print("L'area del rettangolo è: ", area_rettangolo(base,altezza), "cm quadri")

        elif figura == 3:
            area = area_quadrato(base)
            print("L'area del quadrato è:", area_quadrato(base), "cm quadri")
        else:
            print("Hai inserito un numero non valido.\n") #se sbaglio numero, mi dà un errore e rincomincia il ciclo
        aree.append(area)

