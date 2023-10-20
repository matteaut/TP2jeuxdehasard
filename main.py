#cree par Tristan Matteau en 2023
#tp 2.0

import random

rejouer = True

while rejouer:
    nbr_random = random.randint(0, 1000)



    print("J’ai choisi un nombre au hasard entre 0 et 1000.")
    print("À vous de le deviner...")

    question = int(input("Entrez votre essai: "))
    essai = 0
    reponse = True

    while reponse:
        essai = essai+1
        if question > nbr_random:
            print("essaie plus petit")
            print("nombre d'essaie: ", essai)
            question = int(input("Réessaye: "))

        elif question < nbr_random:
            print("essaie plus grand")
            print("nombre d'essaie: ", essai)
            question = int(input("Réessaye: "))

        else:
            print(nbr_random, "Bonne Reponse")
            print("nombre d'essais: ", essai +1)
            print("voule-vous quitter ou rejouer")
            question2 = str(input("entrer votre choix 'Y' ou 'N': "))
            reponse = False

            if question2 == "N":
                print("Bye Bye")
                exit()

            elif question2 == 'Y':
                print("OK")
                rejouer = True





            else:
                print("error!")
                exit()

