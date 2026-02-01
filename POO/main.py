#Programmation impérative

'''def afficher_infos_personne (nom,age):
    print (f"La personne s'appelle {nom}, elle a {age} ans")

def demander_nom ():
    nom = input ("Quelle est votre nom ? ")
    return nom'''

#Programmation orientée objet

#Définition des classes 

'''class Personne:
    def __init__(self, nom="", age=0):
        self.nom = nom
        self.age = age 
        if self.nom == "":
            self.nom = self.demandernom()

    def sepresenter (self):
        info_personne = f"Bonjour je m'appelle {self.nom}"
        if self.age == 0:
             print (info_personne)
        else:
            print(f"{info_personne}, j'ai {self.age} ans")
            if self.estmajeur():
                print ("Je suis majeur")
            else:
                print ("je suis mineur")

    def estmajeur (self):
        if self.age >= 18:
            return True
        return False
    
    def demandernom (self):
        nom = input ("Nom de la personne : ")
        return nom
        

#Utilisation
personne1 = Personne("Jean") #Je crée une personne
personne2 = Personne ("Paul",15)
personne3 = Personne()
personne1.sepresenter()
personne2.sepresenter()
personne3.sepresenter()

#personne1.nom = "toto" #<- on peut altérer la valeur d'une valeur de la classe en dehors du code
#personne1.sepresenter()

#print ("Estmajeur2 : ", personne2.estmajeur())'''

# EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.genre:
            print("Genre : Masculin")
        else:
            print("Genre : Feminin")
            print()

        e_optionnel = ""

        if self.genre == False:
            e_optionnel = "e"

        if self.EstMajeur():
            print(f"Je suis majeur{e_optionnel}")
        else:
            print(f"Je suis mineur{e_optionnel}")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()