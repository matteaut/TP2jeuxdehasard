#cree par Tristan Matteau en 2023
#tp 2

import random

nbr_random = random.randint(0, 1000)
print(nbr_random)

print("J’ai choisi un nombre au hasard entre borne_minimal et borne_maximal.")
print("À vous de le deviner...")


question = int(input("Entrez votre essai: "))
print(question)

if question > nbr_random:
    print("esseye plus petit")
    question = input(str("Entrez votre essai: "))
    print(question)

elif question == nbr_random:
    print("oui")
    exit()

else:
    print("esseye plus grand")
    question = input(str("Entrez votre essai: "))
    print(question)