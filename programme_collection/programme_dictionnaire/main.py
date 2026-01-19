#print("Hello word")

#------Partie 1-----------

'''personne = {'nom' : 'Mélanie', "age" : 19, "Taille" : 1.60} 

print(personne)

personne["nom"] = "Claire" #<- on peut directement remplacer une valeur d'un dictionnaire

print (personne)

personne ["poste"] = "Développeur.se" #<- on peut rajouter une clé directement

print (personne)

for i in personne :
    print(f"Clef : {i}, Valeur : {personne[i]}") #<- les dictionnaires étant aussi des collections, on peut les boucler'''

#------Partie 2-----------

personnes = [
    ("Mélanie",19,1.75),
    ("Paul",45,1.85),
    ("Jules",13,1.55),
    ("Michel",25,2.05)
]

def obtenir_information (nom,liste_de_noms):
    for i in liste_de_noms :
        if nom in liste_de_noms :
            print (liste_de_noms[nom])

obtenir_information ("Jules",personnes)