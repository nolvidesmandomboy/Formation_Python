#Fonction recursive 
#Une fonction recursive est une fonction qui s'appelle elle même, pour ne pas qu'elle boucle à l'infini, on la casse avec une condition

def a (n,limit):
    if n > limit :
        return #-> condition pour casser la boucle infini
    print(n)
    a(n*n,limit)

a(2,100000)