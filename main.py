#cree par Tristan Matteau en 2023
#tp 2.0

import random

nbr_random = random.randint(0, 1000)

rejoue =

print("J’ai choisi un nombre au hasard entre 0 et 1000.")
print("À vous de le deviner...")

question = int(input("Entrez votre essai: "))
essai = 0



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
    print("voule-vous", quitter, "ou", rejouer,)
    question2 = int(input("entrer votre choix: "))

    if question2:
        print("quitter")
        exit()

    elif print("rejouer"):
        rejoue

    else:
        print("error!")
        exit()