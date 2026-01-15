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
print (liste)#<- la liste est un conteneur, donc contrairement aux variables lorsqu'on la modifie dans la fonction, elle est aussi modifiée à l'extérieur'''

def obtenir_infos ():
    return "Melanie",19,"Etudiante",1.75

infos = obtenir_infos()

#print (f"Prénom : {str(infos[0])}")
#print (f"Age : {str(infos[1])} ans")
#print (f"Activité : {str(infos[2])}")
#print (f"Taille : {str(infos[3])} m")

nom,age,taff,taille = obtenir_infos() #<- on peut directement affecter des variables aux valeurs retournés dans la fonction

print (f"Prénom : {nom}, age : {age} ans, activité : {taff}, taille : {taille} m")

