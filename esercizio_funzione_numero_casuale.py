from random import *

def numero_casuale(): #funzione numero casuale
    return randint(1, 100)


def check(numero, numero_casuale): #funzione che checka se il numero è giusto o no
    if numero == numero_casuale:
        print("Hai indovinato, complimenti!")
    elif numero > numero_casuale:
        print("Il numero è troppo alto")
    elif numero < numero_casuale:
        print("Il numero è troppo basso")
    else:
        print("Numero non valido")

numero_casuale = numero_casuale()

while True:
    resa = int(input("Vuoi giocare o vuoi arrenderti? Premi 1 per giocare, 2 per arrenderti\n"))
    if resa == 2:
        break

    numero = int(input("Scegli un numero da 1 a 100 per il nostro gioco!\n"))
    

    check(numero, numero_casuale)

    if numero == numero_casuale:
        break

