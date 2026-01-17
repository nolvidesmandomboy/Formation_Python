def afficher_les_pizzas (liste_de_pizza):
    print(f"----------------Liste des pizzas---------------({len(liste_de_pizza)})")
    for pizza in liste_de_pizza :
        print (pizza)

pizza = ("Margherita", "Végétarienne", "4 fromages","Hawai")

afficher_les_pizzas (pizza)
