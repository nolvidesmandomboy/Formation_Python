print("hello word")
#Les Tuples 

'''personne = ("Mélanie", "Victor", "Thomas", "Nicolas") #<- c'est un tuple, contrairement aux listes, c'est avec des parenthèses et c'st fixe, on ne peut pas le modifier ni rajouter des éléments c'est immutable

print (personne[3]) # <- on appelle les éléments du tuple et de la liste de la même manière

for i in range (0,len(personne)):
    print (personne[i])

for i in personne:
    print (i) #<- ici i va directement prendre les éléments de personnes

personne_ = ["Carlos", "Victoria", "Alison", "Samira"]

del personne_ [2] #<-- Permet de supprimer des éléments d'une liste

print (personne_)

def modifier_valeur(b):
    b = 10

def modifier_valeur_liste(c):
    c[9]=12

a = 5
liste = [1,2,3,4,5,6,7,8,9,10]
print(a)
modifier_valeur(a)
print (a) #<- la valeur reste la même ici vu que la variable qui a changé est locale à la fonction donc tant que je ne la printe pas directement dans la fonction, elle restera la même 
modifier_valeur_liste(liste)
print (liste)#<- la liste est un conteneur, donc contrairement aux variables lorsqu'on la modifie dans la fonction, elle est aussi modifiée à l'extérieur

def obtenir_infos ():
    return "Melanie",19,"Etudiante",1.75

infos = obtenir_infos()

#print (f"Prénom : {str(infos[0])}")
#print (f"Age : {str(infos[1])} ans")
#print (f"Activité : {str(infos[2])}")
#print (f"Taille : {str(infos[3])} m")

#nom,age,taff,taille = obtenir_infos() #<- on peut directement affecter des variables aux valeurs retournés dans la fonction

#print (f"Prénom : {nom}, age : {age} ans, activité : {taff}, taille : {taille} m")

def afficher_infos(nom,age,taff,taille):
    print (f"Prénom : {nom}, age : {age} ans, activité : {taff}, taille : {taille} m")

afficher_infos(*infos) #<- le * permet d'ouvrir le tuple et d'affecter chacune des valeurs qu'il a comme étant un paramètre de la fonction, si je ne l'avais pas mis il l'aurait compté comme étant le premier paramètre uniquement

#Les slices 
personne = ("Mélanie", "Victor", "Thomas", "Nicolas","Jamy","Anais","Sophia","Bebeto") 

for i in personne[0:3]: #<- le slice permet de choisir les éléments du tuple de 0 à n = [start:stop:step]
    print (i)

print()

for i in personne[::2]: #le step ici permet de sauter n élément. Par défaut c'est 1, et à chaque fois qu'on rajoute 1 on saute d'1 pas en plus, bien sur ça s'applique aussi aux chaînes de caractères
    print (i)

#Exercice : Demander le nom des personnes 

nom = []

def afficher_nom_personnes (liste_de_noms) :
    liste_de_noms.sort()
    for i in liste_de_noms :
        print(f"Le nom de la personne {liste_de_noms.index(str(i))+1} : {i}") #Le .index ici permet d'avoir accès à la position de l'élément dans la liste

while True:
    reponse = input ("Quelle est le nom de la personne ? Réponse : ") 
    nom.append (reponse)
    if reponse == "":
        nom.remove("")
        break

afficher_nom_personnes (nom)'''

#Exercice 2 : Algorithme "Valeur la plus petite"

distance_chauffeur = [12.5, 8.3, 15.0, 4.7, 22.1, 9.8, 13.4, 18.6, 7.2, 5.9, 11.0, 14.3, 19.7, 3.5, 27.8, 16.4, 20.2, 6.1, 10.5, 23.9, 0.3, 0.7, 1.2, 0.9, 0.4, 0.15, 0.8]

distance_minimal = distance_chauffeur[0] #On considère toujours le premier élément de la liste comme le plus petit et ensuite avec une boucle for on comparera avec les autres pour voir qui est plus petit 

for distance in distance_chauffeur :
    if distance < distance_minimal:
        distance_minimal = distance
    
    print (f"distance minimale : {distance_minimal}")

