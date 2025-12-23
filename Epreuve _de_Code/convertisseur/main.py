#Mon Code :
print("Bienvenue dans le convertisseur de pouces en centimètres et vice versa !")
jeu = True
while jeu == True :
    choix = input("Souhaitez vous convertir de pouces vers cm (a), de centimètres vers pouces (b) ou sortir (c) ? ")

    def convertisseur (unite1, unite2, facteur_conversion) : 
        valeur = float (input (f"Rentrez votre valeur en {unite1} : "))
        conversion = round (valeur*facteur_conversion, 2)
        print (f"{valeur} {unite1} vaut {conversion} {unite2}")

    if choix == "a" :
        convertisseur ("pouces", "centimètres", 2.54)
    elif choix == "b" :
        convertisseur ("centimètres", "pouces", 0.394)
    elif choix == "c" :
        print ("Au revoir !")
        jeu = False