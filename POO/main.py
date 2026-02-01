#Programmation impérative

'''def afficher_infos_personne (nom,age):
    print (f"La personne s'appelle {nom}, elle a {age} ans")

def demander_nom ():
    nom = input ("Quelle est votre nom ? ")
    return nom'''

#Programmation orientée objet

#Définition des classes 

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age 

    def sepresenter (self):
        print(f"Bonjour je m'appelle {self.nom}, j'ai {self.age} ans") 

#Utilisation
personne1 = Personne("Jean",40) #Je crée une personne
personne2 = Personne ("Paul",15)
personne1.sepresenter()
personne2.sepresenter()

#personne1.nom = "toto" #<- on peut altérer la valeur d'une valeur de la classe en dehors du code
#personne1.sepresenter()