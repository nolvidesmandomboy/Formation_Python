#Projet Pizza V2 

class Pizza:
    def __init__(self,nom="",prix=.0,ingredients=()):
        self.nom= nom
        self.prix=prix
        self.ingredients = ingredients

    def afficher_infos (self):
        print(f"PIZZA {self.nom} : {self.prix}€ ")
        print(f"ingrédients : {", ".join(self.ingredients)}")
        print()


pizza1 = Pizza ("Reine", 9.2, ("jambon", "champignons", "mozzarella"))

pizza2 = Pizza ("Orientale", 11.0, ("merguez", "poivrons", "oignons", "mozzarella"))

pizza3 = Pizza ("Végétarienne", 9.5, ("courgettes", "aubergines", "poivrons", "mozzarella"))

pizza4 = Pizza ("Hawaïenne", 9.8, ("jambon", "ananas", "mozzarella"))

pizza = (pizza1,pizza2,pizza3,pizza4)

for pizzas in pizza :
    pizzas.afficher_infos()