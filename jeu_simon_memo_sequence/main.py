import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

sequence_aleatoire = str (random.randint (0,9)) + str(random.randint(0,9)) + str(random.randint (0,9)) + str(random.randint (0,9))

print("Bonjour, bienvenue dans ce jeu de mémorisation !")
time.sleep (1)
choix_ = input ("Prêt(e) ? (répondre oui ou non) : ")

if choix_ == "oui" :
    print ("Retenez cette séquence :")
    time.sleep (1)
    print(sequence_aleatoire)
    time.sleep (3)
    clear_screen()