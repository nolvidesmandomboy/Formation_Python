#Projet Pizza V2 

class Pizza:
    def __init__(self,nom="",prix=.0,ingredients=(),not_vegetarienne=True):
        self.nom= nom
        self.prix=prix
        self.ingredients = ingredients
        self.not_vegetarienne = not_vegetarienne

    def afficher_infos (self):
        infos_nom_prix = f"PIZZA {self.nom} : {self.prix}€"
        if self.not_vegetarienne :
            print (infos_nom_prix) 
        else :
            print (f"{infos_nom_prix} - végétarienne")

        print(f"ingrédients : {", ".join(self.ingredients)}")
        print()


pizza1 = Pizza ("Reine", 9.2, ("jambon", "champignons", "mozzarella","tomate"))

pizza2 = Pizza ("Orientale", 11.0, ("merguez", "poivrons", "oignons", "mozzarella"))

pizza3 = Pizza ("Végétarienne", 9.5, ("courgettes", "aubergines", "poivrons", "mozzarella"),False)

pizza4 = Pizza ("Hawaïenne", 9.8, ("jambon", "ananas", "mozzarella","tomate"))

pizza = (pizza1,pizza2,pizza3,pizza4)

for pizzas in pizza :
    """if pizzas.not_vegetarienne :
        pizzas.afficher_infos()"""
    if "tomate" in pizzas.ingredients:
        pizzas.afficher_infos()