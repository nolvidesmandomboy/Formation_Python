#Les Fonctions

'''nom = "Nolvides"

print ("je m'appelle " + nom) # <-Ici on concatène la chaîne avec un paramètre (le nom)
print ("Je m'appelle", nom) # <- ici la fonction print a deux paramètres ("Je m'appelle" et le nom), séparé par la virgule

nom_ = input ("Votre nom : ") # <- retourne la valeur, c'est une fonction bloquante 
print ("votre nom est", nom_)'''

#Définition de la fonction
'''def afficher_info_personne (nom, age):
    print(f"La personne est {nom}, son age est de {age} ans")
    print(f"son prénom comporte {len(nom)} lettres")

#Rajout de paramètres
nom1 = input ("Quel est le nom de la personne 1 ?")
age1 = input ("Quelle est l'âge de la personne 1 ?")

#Appel de la fonction
afficher_info_personne(nom1,age1)'''

#Return
''' -> Sert à sortir d'une fonction et à renvoyer une valeur, ce n'est cependant pas obligatoire
 - Il est conseillé de mettre des return dans la fonction lorsqu'il y a des conditions, par exemple, dans le if pour sortir du code directement lorsqu'on rentre dans la condition
 
 - On ne peut pas mettre à la fois un return vide ou un return avec une valeur dans une fonction, ça peut créer des bugs ! 
 
 - Les returns ne sont à utiliser que dans une fonction'''

#Exercice 

'''def recuperer_et_afficher_infos_personne(numero):
    nom = input (f"Nom de la personne {numero} : ")
    age = input (f"Age de la personne {numero} : ")
    print (f"La personne {numero} est {nom}, son age est de {age} ans")
    print (f"son nom comporte {len(nom)} lettres")'''

#Hierarchie
def afficher_info_personnes (numero, nom, age) :
    print (f"La personne {numero} est {nom}, son age est de {age} ans")
    print (f"son nom comporte {len(nom)} lettres")

def recuperer_info_personnes (number) :
    nom_personne = input (f"Nom de la personne {number} : ")
    age_personne = input (f"Age de la personne {number} : ")
    return nom_personne # <- Permet de retourner les valeurs qui vont servir de paramètres dans la fonction afficher info personnes
    

def recuperer_et_afficher_infos_personne(numero_personne):
    recuperer_info_personnes (numero_personne)
    afficher_info_personnes (numero_personne,nom_personne,age_personne)
    

nb_de_personnes = 3

for i in range (nb_de_personnes):
    recuperer_et_afficher_infos_personne(i+1)

