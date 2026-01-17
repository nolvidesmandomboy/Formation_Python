def afficher_les_pizzas (liste_de_pizza):
    print(f"----------------Liste des pizzas---------------({len(liste_de_pizza)})")
    if liste_de_pizza == ():
        print ("AUCUNE PIZZA")
        return

    for pizza in liste_de_pizza :
        print (pizza)
    print (f"Première pizza : {liste_de_pizza[0]} ")
    print (f"Derinère pizza : {liste_de_pizza[-1]} ")

pizza = ("Margherita", "Végétarienne", "4 fromages","Hawai")
vide = ()

afficher_les_pizzas (pizza)
afficher_les_pizzas(vide)


