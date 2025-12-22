#Donner une valeur à une variable 
'''nom = "victorin"
print ("je m'appelle " + nom)
print ("mon nom est bien "+ nom)

nom_de_famille = "Dupont"
Prenom = "Jean"
Profession = "Dévéloppeur"

print("Nom : "+ nom_de_famille)
print ("Prénom : " + Prenom)
print ("profesion : " + Profession)
#print ("identité : " + nom_de_famille + " " + Prenom + " (" + Profession + ")")
#print (f"identité : {nom_de_famille} {Prenom} ({Profession}) ")'''

#demander des données à l'utilisateur (avec des chaînes de caractères uniquement)
'''nom_ = input ("Quel est votre nom ? ")
age = input ("Quel est votre âge ? ")
print (f"Vous vous appelez {nom_} vous avez {age} ans")'''

#Variables numérique
'''nom_ = "ubigum"
age = 30
print(type(age)) -> permet de savoir le type de variable qu'on a si c'est une chaîne de caractères (str) ou un nombre (int)
print (f"Vous vous appelez {nom_} vous avez {age} ans")
str() permet de convertir un nombre en chaîne de caractère afin de le print()
print("Vous vous appelez " + nom_ + ", vous avez " + str(age) + " ans")
print (" l'an prochain, vous aurez " + str(age+1) + " ans")'''

#Convertir une chaîne en nombre
'''nom = input("Quel est ton nom ")
Age = input("quel est ton âge ? ")'''
#pour convertir une chaîne de caractères en nombres on utilise int()
'''age_prochain = int(Age) + 1
print("Vous vous appelez " + nom + ", vous avez " + str(Age) + " ans")
print ("L'an prochain, vous aurez " + str(age_prochain) + " ans")'''

#Gestion des erreurs 
'''nom = input("Quel est ton nom ")
Age = input("quel est ton âge ? ")
try :
    age_prochain = int(Age) + 1
except : 
    print ("Rentre un chiffre pas des lettres fdp")
else :
    print(f"vous vous appelez {nom} vous avez {Age} ans !")'''

#Boucle While
'''n = 0
while n < 20 :
    print ("valeur de n"+ str(n))
    n = n + 1
mot_de_passe = ""
while not mot_de_passe == "MOMO" :
    mot_de_passe = input("Quel est le fucking mot de passe ? ")

print ("c'est bon c'est correct")'''

#améliorer la boucle !!
'''nom = input("Quel est votre nom ? ")
age_prochain = 0
while age_prochain == 0 :
    age = input ("Quel est votre âge ? ")
    try :
        age_prochain = int(age) + 1
    except : 
        print ("ERREUR, vous devez écrire des chiffres")
print(f"Vous vous appelez {nom}, vous avez {age} ans")


nom = input("Quel est votre nom ? ") 
while nom == "" :
      print ("Mettez un nom svp")
      nom = input ("Quel est votre nom svp ? ")
age = 0
while age == 0 :
    age_str = input ("Quel est votre âge ? ")
    try :
        age = int(age_str) 
    except : 
        print ("ERREUR, vous devez écrire des chiffres")
print(f"Vous vous appelez {nom}, vous avez {age} ans")
print("l'an prochain vous aurez " + str(age + 1) + " ans")'''

#Fonctions
'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom


def demander_age() : 
    age_int = 0
    while age == 0 :
        age_str = input ("Quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print ("ERREUR, vous devez écrire des chiffres")
    return age_int

#demander le nom 
nom = demander_nom()

#demander l'âge
age = demander_age()

#Afficher les résultats 
print(f"Vous vous appelez {nom}, vous avez {age} ans")
print("l'an prochain vous aurez " + str(age + 1) + " ans")'''

#Variable globale 
'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom

age = 0
def demander_age() : 
    global age
    while age == 0 :
        age_str = input ("Quel est votre âge ? ")
        try :
            age = int(age_str) 
        except : 
            print ("ERREUR, vous devez écrire des chiffres")

#demander le nom 
nom = demander_nom()

#demander l'âge
age = demander_age()

#Afficher les résultats 
print(f"Vous vous appelez {nom}, vous avez {age} ans")
print("l'an prochain vous aurez " + str(age + 1) + " ans")'''

#Paramètres

'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom

def afficher_resultats (nom,age) :
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print("l'an prochain vous aurez " + str(age + 1) + " ans")

def demander_age(nom_personne) : 
    age_int = 0
    while age_int == 0 :
        age_str = input (nom_personne + ", quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print ("ERREUR " + nom_personne + ", vous devez écrire des chiffres")
    return age_int

#demander le nom 
nom1 = demander_nom()
nom2 = demander_nom()
#demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#Afficher les résultats 
afficher_resultats(nom1,age2)
afficher_resultats(nom2,age2)'''

# Condition et variable booléen
'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom

def afficher_resultats (nom,age) :
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print("l'an prochain vous aurez " + str(age + 1) + " ans")


    if age >= 18 :
        print("vous êtes majeurs")
    else :
        print("vous êtes mineurs")
    

def demander_age(nom_personne) : 
    age_int = 0
    while age_int == 0 :
        age_str = input (nom_personne + ", quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print ("ERREUR " + nom_personne + ", vous devez écrire des chiffres")
    return age_int

#demander le nom 
nom1 = demander_nom()
nom2 = demander_nom()
#demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#Afficher les résultats 
afficher_resultats(nom1,age1)
afficher_resultats (nom2, age2)'''

#Formule perso essaie 1
'''def demnder_l_age(reponse_nom):
    age_int = 0
    while age_int == 0:
        age_str = input (reponse_nom + " Quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print(f"ERREUR " + {reponse_nom} + ", vous devez écrire des chiffres")
    return age_int

def demander_le_nom():
    nom_ = input("quel est ton nom ? ")
    while not nom_ == str(nom_):
        print ("écrivez des lettres, pas des chiffres ou des caractères spéciaux")
    return nom_ 

def demander_le_sexe(reponse_nom):
    sexe_ = input (reponse_nom + "Quel est votre sexe ? ")
    return sexe_
    
def afficher_resultats (nom,age,sexe):
    print(f"vous vous appelez {nom}, vous avez {age} ans")
    if sexe == "Femme" or "femme":
        print ("Vous êtes une femme")
    else:
        print ("vous êtes un homme")


nom1 = demander_le_nom()
age1 = demnder_l_age(nom1)
sexe1 = demander_le_sexe(nom1)
nom2 = demander_le_nom()
age2 = demnder_l_age(nom2)
sexe2 = demander_le_sexe(nom2)

afficher_resultats(nom1,age1,sexe1)
afficher_resultats(nom2,age2,sexe2)'''

#condition elif

'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom

def afficher_resultats (nom,age) :
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print("l'an prochain vous aurez " + str(age + 1) + " ans")

    if age == 1 or age == 2:
        print ("Oohh un bébé ! tu veux une sucette ?")
    elif age > 60:
        print ("Vous êtes sénior ma nigga")
    elif age < 10 :
        print ("vous êtes enfant")
    elif age >= 12 or age < 18:
        print ("t'es encore un ado mon petit")
    elif age == 17 :
        print("vous êtes presque majeurs") 
    elif age == 18 : 
        print ("vous êtes tout juste majeur !")
    elif age > 18 :
        print("vous êtes majeurs") 
    elif age > 60:
        print ("Vous êtes sénior ma nigga")
    else :
        print("vous êtes mineurs")
    

def demander_age(nom_personne) : 
    age_int = 0
    while age_int == 0 :
        age_str = input (nom_personne + ", quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print ("ERREUR " + nom_personne + ", vous devez écrire des chiffres")
    return age_int

#demander le nom 
nom1 = demander_nom()
nom2 = demander_nom()
#demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#Afficher les résultats 
afficher_resultats(nom1,age1)
afficher_resultats (nom2, age2)'''

#La boucle for 
'''def demander_nom () :
    reponse_nom = input("Quel est votre nom ? ") 
    while reponse_nom == "" :
        print ("Mettez un nom svp")
        reponse_nom = input ("Quel est votre nom svp ? ")
    return reponse_nom

def afficher_resultats (nom,age) :
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print("l'an prochain vous aurez " + str(age + 1) + " ans")

    if age == 1 or age == 2:
        print ("Oohh un bébé ! tu veux une sucette ?")
    elif age > 60:
        print ("Vous êtes sénior ma nigga")
    elif age < 10 :
        print ("vous êtes enfant")
    elif age >= 12 or age < 18:
        print ("t'es encore un ado mon petit")
    elif age == 17 :
        print("vous êtes presque majeurs") 
    elif age == 18 : 
        print ("vous êtes tout juste majeur !")
    elif age > 18 :
        print("vous êtes majeurs") 
    elif age > 60:
        print ("Vous êtes sénior ma nigga")
    else :
        print("vous êtes mineurs")
    

def demander_age(nom_personne) : 
    age_int = 0
    while age_int == 0 :
        age_str = input (nom_personne + ", quel est votre âge ? ")
        try :
            age_int = int(age_str) 
        except : 
            print ("ERREUR " + nom_personne + ", vous devez écrire des chiffres")
    return age_int

for i in range (0,3):
    nom = demander_nom ()
    age = demander_age (nom)
    afficher_resultats(nom,age)'''


