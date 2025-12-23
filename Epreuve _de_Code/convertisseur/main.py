#Mon Code :
choix = input("Souhaitez vous convertir de pouces vers cm (a) ou de centimètres vers pouces (b) ? ")

if choix == "a" : 
    valeur = float (input ("Rentrez votre valeur en pouces (a ou b) : "))
    conversion = round (valeur*2.54, 2)
    print (f"{valeur} vaut {conversion} centimètres")

if choix == "b":
    valeur = float (input ("Rentrez votre valeur en centimètres : "))
    conversion = round (valeur*0.394, 2)
    print (f"{valeur} vaut {conversion} pouces")   