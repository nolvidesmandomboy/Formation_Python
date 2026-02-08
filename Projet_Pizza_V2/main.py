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

class PizzaPersonnalisee(Pizza):
    def __init__(self):
        super().__init__("Personnalisé", 0, ())
        self.demander_ingredients_a_l_utilisateur()
    
    def demander_ingredients_a_l_utilisateur(self):
        while True : 
            self.ingredients = list(self.ingredients)
            ingredients = input("Ajouter un ingrédient (ou ENTER pour terminer) : ")
            if ingredients == "":
                return
            self.ingredients.append (ingredients)
            print (f"Vous avez {len(self.ingredients)} ingrédients")


pizza1 = Pizza ("Reine", 9.2, ("jambon", "champignons", "mozzarella","tomate"))

pizza2 = Pizza ("Orientale", 11.0, ("merguez", "poivrons", "oignons", "mozzarella"))

pizza3 = Pizza ("Végétarienne", 9.5, ("courgettes", "aubergines", "poivrons", "mozzarella"),False)

pizza4 = Pizza ("Hawaïenne", 9.8, ("jambon", "ananas", "mozzarella","tomate"))

pizzapersonalise = PizzaPersonnalisee()

pizza = (pizza1,pizza2,pizza3,pizza4,pizzapersonalise)
    
def tri (e):
    return e.nom

pizza=list(pizza)
#pizza.sort(key=tri) #<- permet de faire un tri selon un critère personalisé

for pizzas in pizza :
    pizzas.afficher_infos()



