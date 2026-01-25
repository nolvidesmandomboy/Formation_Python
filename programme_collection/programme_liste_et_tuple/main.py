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

afficher_infos(*infos) #<- le * permet d'ouvrir le tuple et d'affecter chacune des valeurs qu'il a comme étant un paramètre de la fonction, si je ne l'avais pas mis il l'aurait compté comme étant le premier paramètre uniquement'''

#Les slices 
'''personne = ("Mélanie", "Victor", "Thomas", "Nicolas","Jamy","Anais","Sophia","Bebeto") 

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

'''distance_chauffeur = [12.5, 8.3, 15.0, 4.7, 22.1, 9.8, 13.4, 18.6, 7.2, 5.9, 11.0, 14.3, 19.7, 3.5, 27.8, 16.4, 20.2, 6.1, 10.5, 23.9, 0.3, 0.7, 1.2, 0.9, 0.4, 0.15, 0.8]

noms_chauffeurs = [ "Melanie", "Lucas", "Sarah", "Nina", "Adam", "Yanis", "Lina", "Sofia", "Noah", "Emma","Hugo", "Chloé", "Léo", "Maya", "Ethan", "Inès", "Tom", "Lola", "Jules", "Manon", "Elyas", "Nora", "Iris", "Milan", "Ava", "Liam", "Zoé"]


distance_minimal = distance_chauffeur[0] #On considère toujours le premier élément de la liste comme le plus petit et ensuite avec une boucle for on comparera avec les autres pour voir qui est plus petit 

for distance in distance_chauffeur :
    if distance < distance_minimal:
        distance_minimal = distance

index_min = 0
nom_chauffeur_min = 0
distance_minimal = distance_chauffeur[0]
for i in range (len(distance_chauffeur)) :
    distance = distance_chauffeur [i]
    if distance < distance_minimal:
        distance_minimal = distance
        index_min = i
        nom_chauffeur_min = noms_chauffeurs[i]
    
print (f"distance minimale : {distance_minimal} km")
print (f"index de la distance minimale : {distance_chauffeur.index(0.15)}")
print (f"index de la distance minimale : {index_min}")
print (f"nom du chauffeur à la distance minimale : {nom_chauffeur_min}")'''

#APPEND, Extend, Insert, +=

noms = ["jean","sophie","Martin","jacques","Simi"]

'''noms_supplementaires = ["christophe", "Zoé"]

def tri_personnalise (nom): #création d'une fonction pour le tri personnalisée
    return len(nom)

noms.append(noms_supplementaires) #<- ça rajoute à la liste nom la liste contenant les chaînes de caractères des noms supplémentaires et non pas directirecment les noms supplémentaires.

noms.extend(noms_supplementaires) #<- permet d'ajouter les éléments de la liste individuellement et non pas comme une liste

noms += noms_supplementaires #<- ça fonctionne exactement comme l'extend

noms.insert(0,noms_supplementaires) #<- permet d'insérer un élément en lui attribuant un place dans la liste

noms = noms_supplementaires + noms #<- se comporte exactement comme le Insert et ne prends pas la liste mais les éléments de la liste individuellement

slice_noms=noms[:] #<- les deux points ici vont prendre toute la liste et permettent de choisir des éléments en spécifiant la place de départ (à gauche des deux points), et la place d'arrivée (à droite des deux point)

slice_noms[1] = "Fesses" #<- Ici faire une modification ne va pas modifier aussi la liste noms, car dans slice_nms c'est une copie de la liste qu'on a faites. Du coup là on aura deux listes différentes.

print (noms)
print(slice_noms)'''

#Sort et Sorted

'''noms.sort() #<-agit directement sur la liste originale 

noms_supplementaires.sort(key=tri_personnalise) #<- va permettre de faire le tri selon un paramètre personnalisé. Le key va être la clé qui va appliqué la fonction qu'on donne à chacun des éléments pour pouvoir faire le tri. Ici typiquement, quand on mets la fonction tri_personnalise comme key, il va retourner ce que la fonction demande de retourner (ici le nombre de caractères du coup vu que c'est len) et l'appliquer pour chaque éléments de la liste afin de faire le tri

noms_tries = sorted (noms) #<- permet de créer une nouvelle liste triée qui n'affecte pas la liste originale

print (noms)
print (noms_tries)
print(noms_supplementaires)'''

#Min, Max, in, sum

'''ages = [12,15,34,55]

print (min(ages))
print(min(noms)) #<- représente la chaîne de caracère selon l'ordre alphabétique'''

#Join et split

'''noms_join = ", ".join(noms) #<- permet de concaténer tous les éléments en chaîne de caractères d'une liste avec un séparation en chaîne de caractère qu'on défini au départ
print(noms_join)
noms_split = noms_join.split(", ") #<- permet de faire le contraire de join, et de mettre des chaînes de caractères dans une liste avec un séparateur
print (noms_split)'''

# comprehension de liste 

'''longueur_noms = [len(nom) for nom in noms] #Permet de directement afficher des trucs de la liste sans passer par des créations de variables et de boucle au préalable. On peut aussi y rajouter des condition à droite comme à gauche

print (longueur_noms)'''

#Isdigit

nom = "toto2"

'''for ch in nom:
    if ch.isdigit() == True: #<- ça permet de savoir si la chaîne de caractères est composé uniquement de nombres, mais lorsque c'est mélangé chaîne de caractère/nombre, il faut faire une boucle comme là ou faire une fonction
        print ("Il y a un nombre")

def contient_un_chiffre(chaine):
    for ch in chaine:
        if ch.isdigit():
            return True'''

#Exercice 

def element_dans_liste (elementstr,liste):
    liste = [e.lower() for e in liste]
    if elementstr.lower() in liste:
        return elementstr in liste 
    
if element_dans_liste("martin",noms):
    print ("Présent !!!")
else:
    print ("absent")