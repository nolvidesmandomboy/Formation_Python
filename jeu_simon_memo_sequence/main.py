import random
import time
import os


print("Bonjour, bienvenue dans ce jeu de mémorisation !")

time.sleep (1)
print ("Retenez cette séquence :")
sequence_aleatoire = random.randint (0,9)
for i in range (5):
    print (sequence_aleatoire, end="",flush=True)