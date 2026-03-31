#Fichier Texte

#Sur Python, on peut ouvrir, éditer, sauvegarder et fermer un fichier.

#f = open("Mon_fichier.txt", "w")
'''ici, le open permet d'ouvrir le fichier et à l'intérieur des parenthèses on a le nom du ficher et le mode (ici "w" signifie write donc on va écrire mais ça aurait pu être autre chose. Vu que c'est w, si le fichier existe ça va supprimer le contenu et nous donner la possibilité d'écrire un nouveau truc, au contraire si ça n'existe pas ça crée le nouveau fichier pour nous permettre d'écrire.)

Il faut faire aussi attention à ce que dans le terminal le chement soit le même que le fichier dans lequel on va éxécuter le script, c'est là qu'il va être enregistrer.
'''
#f.write("Salut c'est Ninho ! X)")

#f.close()

#Le fichier write doit bien être mis avant le close, c'est pas possible de modifier le fichier une fois que c'est fermer.

#Exercice 1

'''l = []

for i in range (0,10) :
    l.append(f"{str(i+1)}\n")

print (l)
    
fichier = open ("nombres.txt", "w")

fichier.writelines (l)

fichier.close()'''

#Lire un fichier texte
'''f = open("Mon_fichier.txt", "r")

texte = f.read() #<- permet de lire l'intégralité du fichier, on peut aussi spécifier le nombre de caractères à lire dans le fichier directement dans les parenthèses 
print(texte) 

f.close()'''

#Gestion des erreurs 
try :
    f = open("Mon_fichierss.txt", "r")
except FileNotFoundError :
    print("ERREUR, le fichier n'a pas été trouvé")
else:
    lecture = f.read()
    f.close()