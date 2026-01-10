#Fonction recursive 
#Une fonction recursive est une fonction qui s'appelle elle même, pour ne pas qu'elle boucle à l'infini, on la casse avec une condition

def a (n,limit):
    if n > limit :
        return #-> condition pour casser la boucle infini
    print(n)
    a(n*n,limit)

a(2,100000)

#On peut attribuer une fonction à une variable :
'''
def ma_fonction()
    print("Ubigum")

a = "toto"
b = ma_fonction <-- ici la fonction sans parenthèse permet de définir la variable B comme étant la fonction, on pourra donc directement appelé la fonction avec la variable b.
'''