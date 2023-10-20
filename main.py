#cree par Tristan Matteau en 2023
#tp 2.0

import random

rejouer = True


#debut de la boucle permettant de jouer et de rejouer.
while rejouer:
    nbr_random = random.randint(0, 1000)


#debut des questions que le programme va poser.
    print("J’ai choisi un nombre au hasard entre 0 et 1000.")
    print("À vous de le deviner...")

    question = int(input("Entrez votre essai: "))
    essai = 0
    reponse = True

#debut de la boucle permettant de compter le nombre d'essaie que vous utiliser avant de trouver le bon nombre.
    while reponse:
        essai = essai+1
        if question > nbr_random:
            print("essaie plus petit")
            print("nombre d'essaie: ", essai)
            question = int(input("Réessaye: "))

        elif question < nbr_random:
            print("essaie plus grand")
            print("nombre d'essaie: ", essai)
            question = int(input("Réessaye:"))


#si la reponse est bonne le programme donne les option de rejouer(Y) ou de quitter(N).
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

