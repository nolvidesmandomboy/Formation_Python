import random 
def demander_nombre(nb_min, nb_max) :
    nb_magique_int = 0
    while nb_magique_int == 0 :
        nb_magique_str = input (f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
        try :
            nb_magique_int = int(nb_magique_str)
        except :
            print ("Vous devez rentrer un nombre")
        else:
           if nb_magique_int < nb_min or nb_magique_int > nb_max:
               print (f"vous devez rentrer un nombre entre {nb_min} et {nb_max}")
    return nb_magique_int
    
        
nombre_min = 1
nombre_max = 10
nombre_magique = random.randint (nombre_min, nombre_max)
nb_vie = 4

#Avec Boucle While
'''nombre = 0
vies = nb_vie
while nombre != nombre_magique and vies > 0 :
    print (f"il vous reste {vies} vies")
    nombre = demander_nombre (nombre_min,nombre_max)
    if nombre == nombre_magique :
        print ("Bravo ! Vous avez gagné")
    elif nombre >= nombre_min and nombre < nombre_magique :
        print ("Le nombre magique est plus grand, veuillez réessayer")
        vies -= 1
    elif nombre <= nombre_max and nombre > nombre_magique:
        print ("Le nombre magique est plus petit, veuillez réessayer")
        vies -= 1
  
if vies == 0 :
    print (f"Vous avez épuisé vos nombres de vies, le nombre magique était {nombre_magique} ")'''

#Avec Boucle For
gagne = False
for i in range (0, nb_vie):
    vies = nb_vie - i
    print (f"il vous reste {vies} vies")
    nombre = demander_nombre (nombre_min,nombre_max)
    if nombre == nombre_magique :
        print ("Bravo ! Vous avez gagné")
        gagne = True
        break
    elif nombre >= nombre_min and nombre < nombre_magique :
        print ("Le nombre magique est plus grand, veuillez réessayer")
    elif nombre <= nombre_max and nombre > nombre_magique:
        print ("Le nombre magique est plus petit, veuillez réessayer")
  
if not gagne:
    print (f"Vous avez épuisé vos nombres de vies, le nombre magique était {nombre_magique} ")
     
        




   


            
            
