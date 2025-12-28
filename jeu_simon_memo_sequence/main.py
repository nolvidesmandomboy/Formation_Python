import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

sequence_aleatoire = str (random.randint (0,9)) + str(random.randint(0,9)) + str(random.randint (0,9)) + str(random.randint (0,9))
score = 0
boucle = True

print("Bonjour, bienvenue dans ce jeu de mémorisation !")
time.sleep (1)

while True :
    choix_ = input ("Prêt(e) ? (répondre oui ou non) : ")

    if choix_ == "oui" :
        while boucle == True :
            print ("Retenez cette séquence :")
            time.sleep (1)
            print(sequence_aleatoire)
            time.sleep (3)
            clear_screen()
            reponse = input ("Quelle est la séquence de chiffre ? ")
            if reponse == sequence_aleatoire :
                score = score + 2
                print (f"Bien joué ! votre score est de {score}, retenez cette sequence")
                sequence_aleatoire = sequence_aleatoire + str(random.randint(0,9))
            elif reponse != sequence_aleatoire :
                print (f"Mauvaise réponse ! la bonne séquencee était : {sequence_aleatoire}")
                print (f"Votre score final : {score} points")
                jeu = True
                while jeu == True :
                    demande = input ("On recommence ? ")
                    if demande == "oui" :
                        continue
                    elif demande == "non":
                        print ("Au revoir, à bientôt !")
                        jeu = False
                        boucle = False
                    else :
                        print ("ERREUR, écrivez oui ou non pour répondre")
    elif choix_ == "non":
        choix_sortie = input ("Souhaitez vous sortir ? ")
        if choix_sortie == "oui":
            print ("Au revoir !")
            break
    else :
        print ("ERREUR, écrivez une réponse valide (oui ou non)")
        