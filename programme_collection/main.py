print("hello word")
#Les Tuples 

personne = ("Mélanie", "Victor", "Thomas", "Nicolas") #<- c'est un tuple, contrairement aux listes, c'est avec des parenthèses et c'st fixe, on ne peut pas le modifier ni rajouter des éléments c'est immutable

print (personne[3]) # <- on appelle les éléments du tuple et de la liste de la même manière

for i in range (0,len(personne)):
    print (personne[i])

for i in personne:
    print (i) #<- ici i va directement prendre les éléments de personnes

personne_ = ["Carlos", "Victoria", "Alison", "Samira"]

del personne_ [2] #<-- Permet de supprimer des éléments d'une liste

print (personne_)