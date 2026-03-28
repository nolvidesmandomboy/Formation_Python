#Fichier Texte

#Sur Python, on peut ouvrir, éditer, sauvegarder et fermer un fichier.

open("Mon_fichier.txt", "w")
#ici, le open permet d'ouvrir le fichier et à l'intérieur des parenthèses on a le nom du ficher et le mode (ici "w" signifie write donc on va écrire mais ça aurait pu être autre chose. Vu que c'est w, si le fichier existe ça va supprimer le contenu et nous donner la possibilité d'écrire un nouveau truc, au contraire si ça n'existe pas ça crée le nouveau fichier pour nous permettre d'écrire.)