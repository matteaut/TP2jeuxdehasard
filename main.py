#cree par Tristan Matteau en 2023
#tp 2.0

import random

nbr_random = random.randint(0, 1000)
print(nbr_random)

print("J’ai choisi un nombre au hasard entre 0 et 1000.")
print("À vous de le deviner...")

question = int(input("Entrez votre essai: "))

essaie = 0



while question != nbr_random:
    essaie +=1
    if question > nbr_random:
        print("essaie plus petit")
        print("nombre d'essaie: ", essaie)
        question = int(input("Réessaye: "))

    elif question < nbr_random:
        print("essaie plus grand")
        print("nombre d'essaie: ", essaie)
        question = int(input("Réessaye: "))

    elif question == nbr_random:
        print("oui")
        question = int(input("Réessaye:"))

else:
    exit()



