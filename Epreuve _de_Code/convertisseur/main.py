#Mon Code :
choix = input("Souhaitez vous convertir de pouces vers cm (a) ou de centimètres vers pouces (b) ? ")

def convertisseur (choix_utilisateur) :
    if choix_utilisateur == "a" : 
        valeur = float (input ("Rentrez votre valeur en pouces (a ou b) : "))
        conversion = round (valeur*2.54, 2)
        print (f"{valeur} pouces vaut {conversion} centimètres")

    if choix_utilisateur == "b":
        valeur = float (input ("Rentrez votre valeur en centimètres : "))
        conversion = round (valeur*0.394, 2)
        print (f"{valeur} centimètres vaut {conversion} pouces")  

convertisseur (choix) 