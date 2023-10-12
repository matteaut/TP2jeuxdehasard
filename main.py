#cree par Tristan Matteau en 2023
#tp 2.0

import random

nbr_random = random.randint(0, 1000)

rejouer = True

print("J’ai choisi un nombre au hasard entre 0 et 1000.")
print("À vous de le deviner...")

question = int(input("Entrez votre essai: "))
essai = 0

quitter = exit()

while rejouer == True:
        while question != nbr_random:
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
            print("nombre d'essaie: ", essai +1)
            print("voule-vous quitter ou rejouer",)


            question2 = str(input("entrer votre choix: "))

            if question2 == quitter:
                print("quitter")
                exit()

            elif question2 == rejouer:
                print("rejouer")


            else:
                print("error!")
                exit()

            if question2 == quitter:
                exit()

            else:
                print("error!")
                exit()

