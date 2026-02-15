import copy #<- c'est ça qui permettra de faire des copies 
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
'''class Personne:
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
personne2.SePresenter()'''

# POO EXERCICE DE MISE EN SITUATION 2
'''class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age 
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        print("Je suis majeur") if self.EstMajeur() else print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie", 17)
personne2.SePresenter()'''

# POO EXERCICE DE MISE EN SITUATION 3

# ---
'''class Chat:
    def __init__(self, nom = "inconnu"):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __init__(self, nom):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat()
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean'''

#Exercice - Présenter toutes les personnes

'''liste_personnes = [personne1,personne2,personne3]

for i in liste_personnes:
    i.sepresenter()'''

# POO EXERCICE DE MISE EN SITUATION 4

# ---
'''class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)
        return 

# ---
noms = []
for i in range (3):
    noms.append(input(f"nom de la personne {i+1}: "))


Personne(noms[1]).SePresenter()

for p in range (len(noms)):
    Personne(noms[p]).SePresenter()
    print()'''

#Héritage 
'''class Etre_vivant:
    Espece_etre_vivant = "Espèce non identifiée"

    def afficher_info_etre_vivant(self):
        # Si l'objet possède un attribut 'nom' et qu'il n'est pas vide
        if hasattr(self, "nom") and self.nom != "": #<- le "hasattr" permet de savoir si un object a un attribut (retourne True si oui False si non) donc ici, on cherche à savoir si self a un attribut "nom"
            print(f"{self.nom} est de l'espèce : {self.Espece_etre_vivant}")
        else:
            print("L'être vivant est de cette espèce : " + self.Espece_etre_vivant)



class Personne (Etre_vivant): #<- permet de faire heriter cette classe d'une autre class, du coup elle va bénéficier du code de cette autre classe
    Espece_etre_vivant = "Humain" #<- il faut cependant garder les variables de classes pour différencier si besoin
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
    
class chat (Etre_vivant):
    Espece_etre_vivant = "Chat"

class Etudiant (Personne):
    def __init__(self, nom="", age=0,etudes=""):
        super().__init__(nom, age)#<- permet de récupérer l'init de la class parent et ensuite de faire l'init de la classe enfant (ici la classe Etudiant)
        self.etudes = etudes
    
    def sepresenter(self):
        super().sepresenter() #<- permet de récuperer le code de la class parent et d'écrire le code à la suite pour qu'il soit éxécuté sans être écrasé
        print (f"Je fais des études en {self.etudes}")
        
    
personne1  = Personne("Chloé",14)
personne1.sepresenter()
personne1.afficher_info_etre_vivant()'''
'''personne2 = Personne("jean")
personne2.sepresenter()
personne2.afficher_info_etre_vivant()'''
'''chat1 = chat()
chat1.afficher_info_etre_vivant()
etudiant1 = Etudiant ("Tom",23,"commerces")
etudiant1.sepresenter()'''

#Isinstance
'''class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age= age

        if not isinstance(age, int): # if isinstance(var,type) permet d'interroger si la variable var est du type qu'on a rentrer en paramètre
            print("l'âge doit être une nombre") #<- si on laisse comme ça, ça va s'afficher mais on aura toujours une erreur en lançant le programme, pour ne pas avoir d'erreur il faudra remmettre l'âge à 0 par exemple
            self.age = 0
    
    def afficher_infos(self):
        print(f"je m'appelle {self.nom}, j'ai {self.age}")'''

#Polymorphisme

'''class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Chat (EtreVivant):
    def afficher_infos(self):
        print("je suis un chat")

class Personne (EtreVivant):
    def afficher_infos(self):
        print("je suis une personne")

e = [EtreVivant(),Chat(),Personne()]

for l in e : 
    l.afficher_infos() #<- on peut mettre plusieurs classe dans une même liste et appeler une méthode commune à ceux-ci, ça s'appelle le polymorphisqme.'''

#Copie d'objets et __str__

'''class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age= age
    
    def afficher_infos(self):
        print(f"je m'appelle {self.nom}, j'ai {self.age}")
    
    def __eq__ (self,other):
        return self.nom == other.nom and self.age == other.age
    
    def __str__(self): #<- cette fonction permets de retourner sous forme de chaîne de caractère les éléments que l'on souhaite lorsqu'on appelle directement l'objet sans appeler des méthodes
        return str(self.__dict__)
    
personne1 = Personne ("Jean", 20)
personne1.afficher_infos()

personne2 = copy.copy(personne1) #copy.copy permet de faire une copie des éléments d'un objet dans un autre objet, même si on modifie l'objet original, la copie sera aussi modifiée 
personne2.afficher_infos()

print (personne2)

print (personne1 == personne2)
print (personne1 is personne2)

print (personne1.__dict__ == personne2.__dict__)'''

# Méthodes d’instance, de classe et statiques

'''class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom

    # Méthode d'instance
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)

    # premier charactère en majuscule puis minuscules
    # méthode statique
    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print("Méthode de classe : " + cls.TYPE)


personne1 = Personne("jean")
personne1.se_presenter()

print(Personne.formater_chaine("toTo"))

Personne.methode_de_classe()'''