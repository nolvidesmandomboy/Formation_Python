# On crée la tortue avec les deux codes en bas 
import turtle
t = turtle.Turtle()

'''t.forward(100) # permet d'avancer et le 100 entre parenthèse désigne le nombre de pixels
t.left(90)# tourner de 90 degrés
t.backward (50) #Reculer'''

def escalier(taille, nb_de_marche):
    for i in range (0,nb_de_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)    
        t.right(90)
    t.forward(taille)


def carre (taille):
    for i in range (0,4):
        t.forward(taille)
        t.left(90)
        

def carres_dif (taille_depart, nb_de_carres):
    for i in range (0,nb_de_carres):
        taille = (i + 1) * taille_depart
        carre(taille)

carres_dif (10,10)
# En lançant le code uniquement avec les deux lignes une page s'ouvre brièvement mais on souhaite que ça reste ouvert, ducoup on utilise la ligne en bas

turtle.done()