#Projet Pizza V2 

class Pizza:
    def __init__(self,nom="",prix=.0,ingredients=()):
        self.nom= nom
        self.prix=prix
        self.ingredients = ingredients

    def afficher_infos (self):
        print(f"PIZZA {self.nom} : {self.prix}€ ")
        print(f"ingrédients : {", ".join(self.ingredients)}")