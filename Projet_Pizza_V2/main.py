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
    def __init__(self, numero_de_pizza=int):
        self.numero_de_pizza = numero_de_pizza
        super().__init__(f"Personnalisée n°{numero_de_pizza}", 0, ())
        self.demander_ingredients_a_l_utilisateur()
        self.calculer_le_prix()
    
    def demander_ingredients_a_l_utilisateur(self):
        self.prix_de_base = 5
        self.prix_par_ingredients = 1.2
        while True : 
            self.ingredients = list(self.ingredients)
            ingredients = input(f"Ajouter un ingrédient pour la pizza personnalisée n°{self.numero_de_pizza} (ou ENTER pour terminer) : ")
            if ingredients == "":
                return
            self.ingredients.append (ingredients)
            print (f"Vous avez {len(self.ingredients)} ingrédient(s) {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        prix_pizza_personnalisee = self.prix_de_base + self.prix_par_ingredients * len(self.ingredients)
        self.prix = prix_pizza_personnalisee



pizza1 = Pizza ("Reine", 9.2, ("jambon", "champignons", "mozzarella","tomate"))

pizza2 = Pizza ("Orientale", 11.0, ("merguez", "poivrons", "oignons", "mozzarella"))

pizza3 = Pizza ("Végétarienne", 9.5, ("courgettes", "aubergines", "poivrons", "mozzarella"),False)

pizza4 = Pizza ("Hawaïenne", 9.8, ("jambon", "ananas", "mozzarella","tomate"))

#pizzapersonalise = PizzaPersonnalisee()

pizza = (pizza1,pizza2,pizza3,pizza4,PizzaPersonnalisee(numero_de_pizza=1),PizzaPersonnalisee(numero_de_pizza=2))
    
def tri (e):
    return e.nom

pizza=list(pizza)
#pizza.sort(key=tri) #<- permet de faire un tri selon un critère personalisé

for pizzas in pizza :
    pizzas.afficher_infos()



