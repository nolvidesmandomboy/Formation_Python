import time

print ("Bienvenue dans ce minuteur du temps de cuisson !")

while True :
    print ("Que souhaitez-vous cuire ?")
    time.sleep(0.5)
    print ("a - des oeufs à la coque (3 minutes)")
    time.sleep(0.5)
    print ("b - des oeufs mollets (6 minutes)")
    time.sleep(0.5)
    print ("c - des oeufs durs (10 minutes)")
    time.sleep(0.5)
    print ("d - Quitter")

    time.sleep(0.5)
    choix = input ("Quel est votre choix ? (entre a, b, c et d) : ")

    def affichage_du_temps_de_cuisson (minutes,secondes,nom_de_loeuf):
        print (f"vous avez selectionner un {nom_de_loeuf} ! Durée estimée : {minutes} minutes")
        print ("cuisson en cours", end="")
        for i in range(10):
                time.sleep(1)
                print(".", end="", flush=True)
        print("\n")

        while True:
            if secondes == 0:
                minutes = minutes-1
                secondes = secondes+60

            if secondes> 0:
                secondes = secondes - 10
            print(f"Durée restante = {minutes:02d}:{secondes:02d}", end="")

            for i in range(10):
                time.sleep(1)
                print(".", end="", flush=True)

            print("\n")
            
            if minutes == 0 and secondes == 0:
                break
        
        print(f"fin de la cuisson !, votre {nom_de_loeuf} est prêt ! Bonne appétit ;)")

    d = 100
    min = d//60 # division entière (pas de virgules)
    sec = d-min*60

    if choix == "a" :
        d=180
        min =d//60
        sec = sec = d-min*60
        affichage_du_temps_de_cuisson(min, sec, "oeuf à la coque")

    elif choix == "b" :
        d=360
        min =d//60
        sec = sec = d-min*60
        affichage_du_temps_de_cuisson(min, sec, "oeuf mollet")

    elif choix == "c":
        d=600
        min =d//60
        sec = sec = d-min*60
        affichage_du_temps_de_cuisson(min, sec, "oeuf dur")

    elif choix == "d":
        print ("Au revoir ! à bientôt pour de nouvelles cuissons !")
        break

    else :
        print ("ERREUR, veuillez selectionner un des trois choix valides (a, b ou c)")