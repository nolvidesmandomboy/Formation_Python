#Nouveauté de Python
#Union de dictionnaire

dict1 = {"Jean":(20,"dévéloppeur"),"Mark":(45,"Architecte")}
dict2 = {"Emilie":(35,"danseuse"),"Jenifer":(18,"étudiante en psychologie criminelle")}

dict1.update(dict2) #<- la fonction update ici permet d'agreger le contenu d'un dictionnaire à un jour qui est mis à jour
print(dict1)
repectoire_complet = dict1 | dict2 #<- permet de concatener les deux dictionnaires directement 
print (repectoire_complet)

#Supprimer le suffixe ou le préfixe d'une phrase 

phrase = "Emilie a mangé un gateau"
print(phrase.removeprefix("Emilie"))
print(phrase.removesuffix("gateau"))
'''
removeprefix ou removesuffix permettent de retirer des mots au début ou à la fin d'une phrase dans une chaîne de caractères
'''

#Correspandance sturctuelle 

#Switch Case / Match Case

phrase = input ("Parlez-moi : ")
if phrase == "Bonjour":
    phrase = input ("Bonjour comment allez-vous ? ")
    print ("Passez une bonne journée !")
elif phrase == "ça va ?":
    phrase = input ("ça va bien et vous ?")
else:
    print("Je n'ai pas compris")