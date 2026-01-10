#Fonction recursive 
#Une fonction recursive est une fonction qui s'appelle elle même, pour ne pas qu'elle boucle à l'infini, on la casse avec une condition

def a (n,limit):
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