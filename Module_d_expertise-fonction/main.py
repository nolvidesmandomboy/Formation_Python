#Les Fonctions

'''nom = "Nolvides"

print ("je m'appelle " + nom) # <-Ici on concatène la chaîne avec un paramètre (le nom)
print ("Je m'appelle", nom) # <- ici la fonction print a deux paramètres ("Je m'appelle" et le nom), séparé par la virgule

nom_ = input ("Votre nom : ") # <- retourne la valeur, c'est une fonction bloquante 
print ("votre nom est", nom_)'''

#Définition de la fonction
def afficher_info_personne (nom, age):
    print(f"La personne est {nom}, son age est de {age} ans")
    print(f"son prénom comporte {len(nom)} lettres")

#Rajout de paramètres
nom1 = input ("Quel est le nom de la personne 1 ?")
age1 = input ("Quelle est l'âge de la personne 1 ?")

#Appel de la fonction
afficher_info_personne(nom1,age1)

#Return
''' -> Sert à sortir d'une fonction et à renvoyer une valeur, ce n'est cependant pas obligatoire
 Il est conseillé de mettre des return dans la fonction lorsqu'il y a des conditions, par exemple, dans le if pour sortir du code directement lorsqu'on rentre dans la condition'''
