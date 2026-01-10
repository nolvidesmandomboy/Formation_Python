#Fonction recursive 
#Une fonction recursive est une fonction qui s'appelle elle même, pour ne pas qu'elle boucle à l'infini, on la casse avec une condition

'''def a (n,limit):
    if n > limit :
        return #-> condition pour casser la boucle infini
    print(n)
    a(n*n,limit)

a(2,100000)

#On peut attribuer une fonction à une variable :

def ma_fonction():
    print("Ubigum")

c = "toto"
d = ma_fonction #<-- ici la fonction sans parenthèse permet de définir la variable B comme étant la fonction, on pourra donc directement appelé la fonction avec la variable b.


#callbacks 
def mult_callback (a,b):
    return a*b

def add_callback (a,b):
    return a+b

# Les calls backs permettent de creer d'autres fonctions qu'on rajoutera dans les paramètres de la fonction principale

def afficher_table (n,operateur_str,operation_callback):
    for i in range (1,10):
        print (f"{i} {operateur_str} {n} = {operation_callback(i,n)}")

afficher_table (9,"x",mult_callback)
d()

#Les fonctions lambdas

#On peut aussi directement écrire les fonctions lors de l'appel de celle-ci sans forcément écrire un callback, ce sont les fonctions lambas :

afficher_table (14,"+",lambda a,b : a + b) #<-- ici j'ai directement écrit la fonction dans le paramètre de l'appel comme ça ça m'évite de créer de nouvelles fonctions pour les callbacks'''

#Nombres variables de paramètres dans une fonction
# ça va nous permettre de faire des fonctions sans connaître à l'avance le nombre de paramètres qui y sont 

def somme (*nombres): #<-- ça permet ici de rentre le nombre de paramètres qu'on veut sans que ça me demande modifier la fonction
    resultat = 0
    for n in nombres :
        resultat += n
    print(resultat) 

def somme_des_notes (**nombres): #<- le ** permets de rajouter des clés à chacunes des valeurs, comme dans un dictionnaire, en général c'est utiliser pour faire la moyenne 
    resultat = 0
    for n in nombres.values() :
        resultat += n
    print(resultat) 


somme (5,2,4,6,8)
somme_des_notes (maths=12,geomatique=18,anglais=10)