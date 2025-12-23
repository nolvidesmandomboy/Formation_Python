#Mon Code :
print("Bienvenue dans le convertisseur de pouces en centimètres et vice versa !")
while True :
    choix = input("Souhaitez vous convertir de pouces vers cm (a), de centimètres vers pouces (b) ou sortir (c) ? ")

    def convertisseur (unite1, unite2, facteur_conversion) : 
        valeur_str = (input (f"Rentrez votre valeur en {unite1} : "))
        try:
            valeur_float = float(valeur_str) # La conversion en float est faite directement ici, pas besoin de convertir la valeur plus tôt sinon on aura une erreur"
        except ValueError:
            print("ERREUR, veuillez utilisez une valeur numérique ")
            print ("(la décimale est un point et non une virgule)")
            return convertisseur (unite1, unite2, facteur_conversion)
        
        conversion = round (valeur_float*facteur_conversion, 2)
        print (f"{valeur_float} {unite1} vaut {conversion} {unite2}")

    if choix == "a" :
        convertisseur ("pouces", "centimètres", 2.54)
    elif choix == "b" :
        convertisseur ("centimètres", "pouces", 0.394)
    elif choix == "c" :
        print ("Au revoir !")
        break