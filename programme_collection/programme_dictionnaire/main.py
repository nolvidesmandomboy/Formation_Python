print("Hello word")

personne = {'nom' : 'Mélanie', "age" : 19, "Taille" : 1.60} 

print(personne)

personne["nom"] = "Claire" #<- on peut directement remplacer une valeur d'un dictionnaire

print (personne)

personne ["poste"] = "Développeur.se" #<- on peut rajouter une clé directement

print (personne)

for i in personne :
    print(f"Clef : {i}, Valeur : {personne[i]}") #<- les dictionnaires étant aussi des collections, on peut les boucler