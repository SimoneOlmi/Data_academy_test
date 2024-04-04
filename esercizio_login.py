print("Benvenuto sul sito! Per favore, registrati scegliendo nome utente e password\n"
      "Ti chiederemo anche il tuo colore preferito e il tuo animale preferito per sicurezza\n")

nome = input("Inserisci il tuo nome utente, per favore: ") #chiedo il nome
password = input("Inserisci la tua password, per favore: ") #chiedo la password

colore = input("Qual è il tuo colore preferito?\n") #setto il colore preferito
animale = input("Qual è il tuo animale preferito?\n") #setto l'animale preferito

accesso = [nome, password]

print("\nGrazie di esserti registrato! Accedi ora al sito utilizzando le tue credenziali\n")


nome_temp = input("Inserisci il tuo nome, per favore: ") #chiedo il nome
password_temp = input("Inserisci la tua password, per favore: ") #chiedo la password



accesso_temp = [nome_temp, password_temp]


if accesso[0] == accesso_temp[0] and accesso[1] == accesso_temp[1]: #controllo l'identità dell'utente
    print("Benvenuto " + accesso[0] +"\n")
    #uso la variabile check per selezionare che tipo di domanda andrò a fare all'utente
    check = int(input("Per ragioni di sicurezza, dovrai confermare la tua identità. Scegli 1" 
                  " se vuoi confermare la tua identità con il colore preferito, scegli 2"
                  " se vuoi confermare la tua identità con l'animale preferito\n"))
    if check == 1:
        colore_temp = input("Selezione il colore preferito che hai scelto al momento della tua registrazione\n")
        if colore_temp != colore: #se la risposta è sbagliata, il programma termina
            print("Identità non confermata. Verrai buttato fuori dal sito")
            quit()
    else:
        animale_temp = input("Selezione l'animale preferito che hai scelto al momento della tua registrazione\n")
        if animale_temp != animale: #se la risposta è sbagliata, il programma termina
             print("Identità non confermata. Verrai buttato fuori dal sito")
             quit()
    counter = 1 #inizializzo il counter per il numero di tentativi
    while True: #inizializzo un ciclo infinito
        
        #seleziono il tipo di operazione che voglio fare
        print("Hai ancora", 2-counter, "possibilità di errore\n")
        selezione = int(input("\nScrivi 1 se desideri cambiare nome utente\nScrivi 2" 
                          " se vuoi cambiare password\nScrivi 3 se vuoi visualizzare l'attuale"
                          " nome utente e password\nScrivi 0 se vuoi uscire dal sito\n"))
        
        if selezione == 0: #esco dal programma
            print("Esco dal programma\n")
            break
        elif selezione == 1:
            var_temp = input("Per cambiare il nome utente, digita la password\n")
            if var_temp == accesso[1]: #se la password è giusta, procedi al cambio nome
                nuovo_nome = input("Password corretta. Seleziona il nuovo nome utente: ")
                accesso[0] = nuovo_nome
            elif counter <2:
                counter += 1 #aumento il numero di tentativi possibili. Un altro fallimento farà finire il programma
                #rifaccio il check sull'animale o colore preferito come seconda possibilità, per una volta sola
                check = int(input("Per ragioni di sicurezza, dovrai confermare la tua identità. Scegli 1" 
                  " se vuoi confermare la tua identità con il colore preferito, scegli 2"
                  " se vuoi confermare la tua identità con l'animale preferito\n"))
                if check == 1:
                    colore_temp = input("Selezione il colore preferito che hai scelto al momento della tua registrazione\n")
                    if colore_temp != colore: #se la risposta è sbagliata, il programma ha aumentato il counter, ma non ti fa cambiare il nome
                        print("Identità non confermata.")
                        continue
                    else:
                        nuovo_nome = input("Password corretta. Seleziona il nuovo nome utente: ") #cambio il nome
                        accesso[0] = nuovo_nome
                else:
                    animale_temp = input("Selezione l'animale preferito che hai scelto al momento della tua registrazione\n")
                    if animale_temp != animale: #se la risposta è sbagliata, il programma ha aumentato il counter, ma non ti fa cambiare il nome
                        print("Identità non confermata.")
                        continue
                    else:
                        nuovo_nome = input("Password corretta. Seleziona il nuovo nome utente: ") #cambio il nome
                        accesso[0] = nuovo_nome
            else:
                print("Tentativo negato, troppi fallimenti. Verrai buttato fuori dal sito\n")
                quit()
        elif selezione == 2:
            var_temp = input("Per cambiare la password, digita la password attuale\n")
            if var_temp == accesso[1]: #se la password è giusta, procedi al cambio pwd
                nuova_password = input("Seleziona la nuova password ")
                accesso[1] = nuova_password
            elif counter <2:
                counter += 1 #aumento il numero di tentativi possibili. Un altro fallimento farà finire il programma
                #rifaccio il check sull'animale o colore preferito come seconda possibilità, per una volta sola
                check = int(input("Per ragioni di sicurezza, dovrai confermare la tua identità. Scegli 1" 
                  " se vuoi confermare la tua identità con il colore preferito, scegli 2"
                  " se vuoi confermare la tua identità con l'animale preferito\n"))
                if check == 1:
                    colore_temp = input("Selezione il colore preferito che hai scelto al momento della tua registrazione\n")
                    if colore_temp != colore: #se la risposta è sbagliata, il programma ha aumentato il counter, ma non ti fa cambiare la password
                        print("Identità non confermata.")
                        continue
                    else:
                        nuova_password = input("Password corretta. Seleziona la nuova password: ") #cambio la password
                        accesso[1] = nuova_password
                else:
                    animale_temp = input("Selezione l'animale preferito che hai scelto al momento della tua registrazione\n")
                    if animale_temp != animale: #se la risposta è sbagliata, il programma ha aumentato il counter, ma non ti fa cambiare la password
                        print("Identità non confermata.")
                        continue
                    else:
                        nuova_password = input("Password corretta. Seleziona il nuovo nome utente: ") #cambio la password
                        accesso[1] = nuova_password
            else:
                print("Tentativo negato, troppi fallimenti. Verrai buttato fuori dal sito\n") #se il counter supera 1, il sito ti butta fuori e il programma termina
                quit()
        elif selezione == 3:
            print("Il nome utente è " + accesso[0] + " e la password è " + accesso[1] + "\n") #stampo nome utente e password attuali
        else:
            "Numero non valido, riprova\n"
else:
    print("Nome utente o password invalidi, accesso negato")

