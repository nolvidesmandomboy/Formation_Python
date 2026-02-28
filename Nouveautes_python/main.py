#Nouveauté de Python
#Union de dictionnaire

'''dict1 = {"Jean":(20,"dévéloppeur"),"Mark":(45,"Architecte")}
dict2 = {"Emilie":(35,"danseuse"),"Jenifer":(18,"étudiante en psychologie criminelle")}

dict1.update(dict2) #<- la fonction update ici permet d'agreger le contenu d'un dictionnaire à un jour qui est mis à jour
print(dict1)
repectoire_complet = dict1 | dict2 #<- permet de concatener les deux dictionnaires directement 
print (repectoire_complet)

#Supprimer le suffixe ou le préfixe d'une phrase 

phrase = "Emilie a mangé un gateau"
print(phrase.removeprefix("Emilie"))
print(phrase.removesuffix("gateau"))'''
'''
removeprefix ou removesuffix permettent de retirer des mots au début ou à la fin d'une phrase dans une chaîne de caractères
'''

#Correspandance sturctuelle 

#Switch Case / Match Case

'''while True :
    phrase = input ("Parlez-moi : ")
    if phrase == "Bonjour":
        phrase = input ("Bonjour comment allez-vous ? ")
        print ("Passez une bonne journée !")
    elif phrase == "ça va ?":
        phrase = input ("ça va bien et vous ?")
    elif phrase == "Bye":
        phrase == "Au revoir"
        break
    else:
        print("Je n'ai pas compris")'''
# le match case fonctionne de la même façon que le elseif et est utilisé lorsqu'on un nombre important de conditions à faire sur une même donnée
'''while True:
    phrase = input("Parlez-moi : ")
    match phrase:
        case "Bonjour" | "Hello" | "salut" :
            print("Bonjour comment allez-vous ? ")
        case "bien" | "ça va ?":
            print("Je viens bien et vous ? ")
        case "bye":
            print("Au revoir")
            break
        case _: #<- le underscore ici représente le "Else de la condition if précédente, et englobe donc tous les autres cas"
            print("Je n'ai pas compris")'''

#Nouvel exemple
personne1 = {"nom":"Paul","infos":(20,"Ingénieur")}
personne2 = {"nom" : "Marc", "age" : 30} #Ici on a donc deux données qu'on imagine issue d'une base de données contenant certaines données similaires mais stucturés différemment
personnes = (personne1,personne2)

for personnes in personnes:
    match personnes:
        case {"nom" : nom, "infos" : (age,metier)}: #<- ici on mets dans le case la forme qui corresponds à la condition (ici un dictionnaire), puis la clé que le dictionnaire doit doit avoir et les variables qui doivent être ressortie. Ici, si le dictionnaire a une clé "nom", on stocke la donnée dans une variable "nom"
            print(f"{nom}, {age} ans, {metier}")
        case _:
            print("format non supporté")