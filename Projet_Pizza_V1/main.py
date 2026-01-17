def pizza_existe (collection,rajout):
    if rajout.lower() in collection : #<- le lower ici permet de mettre tout la chaîne de caractère en miniscule et du coup de quand même détecter si un élément est dans la liste même si il est en majuscule
        return True
    
def tri_personnalisee (e):
    return len(e)

def ajouter_pizza_utilisateur (collection):
    rajout = input ("Pizza à rajouter : ")
    if pizza_existe (collection,rajout):
        print ("Cette pizza existe déjà")
        print()
        return
    collection.append(rajout)

def afficher_les_pizzas (liste_de_pizza):
    print(f"----------------Liste des pizzas---------------({len(liste_de_pizza)})")

    '''liste_de_pizza.sort(reverse=True,key=tri_personnalisee) # <- on peut mettre des paramètres dans la fonction sort, parmi ceux-ci y a le reverse qui permet d'inverser les valeurs et key qui permet de personnaliser les tri'''
    if liste_de_pizza == ():
        print ("AUCUNE PIZZA")
        return

    for pizza in liste_de_pizza :
        print (pizza)
    print (f"Première pizza : {liste_de_pizza[0]} ")
    print (f"Derinère pizza : {liste_de_pizza[-1]} ")

pizza = ["margherita", "végétarienne", "4 fromages","hawai"]
vide = ()

ajouter_pizza_utilisateur (pizza)
afficher_les_pizzas (pizza)


