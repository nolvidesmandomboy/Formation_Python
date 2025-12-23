#Mon Code :
print("Bienvenue dans le convertisseur de pouces en centimètres et vice versa !")
jeu = True
while jeu == True :
    choix = input("Souhaitez vous convertir de pouces vers cm (a), de centimètres vers pouces (b) ou sortir (c) ? ")

    def convertisseur (choix_utilisateur) :
        if choix_utilisateur == "a" : 
            valeur = float (input ("Rentrez votre valeur en pouces (a ou b) : "))
            conversion = round (valeur*2.54, 2)
            print (f"{valeur} pouces vaut {conversion} centimètres")

        if choix_utilisateur == "b":
            valeur = float (input ("Rentrez votre valeur en centimètres : "))
            conversion = round (valeur*0.394, 2)
            print (f"{valeur} centimètres vaut {conversion} pouces")  

    if choix == "c" :
        print ("Au revoir !")
        jeu = False
    else :
        convertisseur (choix)