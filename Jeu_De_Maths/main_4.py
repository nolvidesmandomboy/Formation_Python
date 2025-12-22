import random

'''nb_min = 1
nb_max = 20
nb_question = 5

def poser_question ():
    nb_hasard_1 = random.randint(nb_min,nb_max)
    nb_hasard_2 = random.randint(nb_min,nb_max)
    o = random.randint(0,2)
    operateur_str = "+"
    if o == 1 :
        operateur_str = "x"
    elif o == 2 :
        operateur_str = "-"
    reponse = int (input (f"Calculez {nb_hasard_1} {operateur_str} {nb_hasard_2} = "))
    calcul = nb_hasard_1 + nb_hasard_2
    if o == 1 :
        calcul = nb_hasard_1 * nb_hasard_2
    elif o == 2 :
        calcul = nb_hasard_1 - nb_hasard_2
    if reponse == calcul :
        return True

    return False 

nb_points = 0
for i in range (0,nb_question):
    print ("Question N°", i+1, "sur", nb_question )
    if poser_question():
        print ("Bien joué, vous avez trouvé la bonne réponse")
        nb_points += 1
    else : 
        print ("Perdu ! ")  
    print()

print (f"Vous avez : {nb_points}/{nb_question} points")

moyenne = int(nb_question/2)

if nb_points == nb_question :
    print ("Excellent bg !")
elif nb_points == 0 :
    print("Ben alors ? on révise pas ses maths ?")
elif nb_points > moyenne :
    print ("Pas mal en vrai")
elif nb_points < moyenne :
    print ("Tu peut mieux faire mieux")'''

