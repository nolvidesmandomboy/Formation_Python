import time
def afficher_table_de_multiplication (nombre, nb_tab_min=1, nb_tab_max=10):
    print (f"Table de multiplication de {nombre}")
    if nb_tab_min == "" :
        nb_tab_min=1
        nb_tab_max=nb_tab_max
    elif  nb_tab_max == "":
        nb_tab_min=nb_tab_min
        nb_tab_max=10
    for i in range (int(nb_tab_min),int(nb_tab_max)+1):
        nombre = int(nombre)
        print (f"{i} x {nombre} = {i*nombre}")
        time.sleep(0.5)

def gestion_des_erreurs (number,nb_min,nb_max):
    if number == int :
        return False
    if nb_min == int :
        return False   
    if nb_max == int :
        return False
    return True
    

print ("Bienvenue dans cet exercie de table de multiplication")
time.sleep(1)
print ("Le but ici est de vous afficher les tables de multiplication du ou des nombres que vous rentrerez")
time.sleep(2)
Choix_numero = (input ("De quel numero souhaitez vous connaître la table de multiplication ? "))
choix_min = input ("Vous pouvez aussi choisir d'où commence la table et où elle se termine (si vous n'en rentrez pas, la table sera par défaut de 1 à 10), choississez donc une valeur minimale (ou pas) ")
choix_max = input ("Et une valeur maximale : ")
gestion_des_erreurs (Choix_numero,choix_min,choix_max)
#afficher_table_de_multiplication (Choix_numero,choix_min,choix_max)

