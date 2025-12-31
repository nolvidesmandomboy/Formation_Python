def afficher_table_de_multiplication (nombre, nb_tab_min=1, nb_tab_max=10):
    print (f"Table de multiplication de {nombre}")
    if nb_tab_min == "" and nb_tab_max == "":
        nb_tab_min=1
        nb_tab_max=10
    for i in range (int(nb_tab_min),int(nb_tab_max+1)):
        print (f"{i} x {nombre} = {i*nombre}")


print ("Bienvenue dans cet exercie de table de multiplication")
print ("Le but ici est de vous afficher les tables de multiplication du ou des nombres que vous rentrerez")
Choix_numero = int(input ("De quel numero souhaitez vous connaître la table de multiplication ? "))
choix_min = input ("Vous pouvez aussi choisir d'où commence la table et où elle se termine (si vous n'en rentrez pas, la table sera par défaut de 1 à 10), choississez donc une valeur minimale (ou pas) ")
choix_max = input ("Et une valeur maximale : ")

afficher_table_de_multiplication (Choix_numero,choix_min,choix_max)

