import time

print ("Bienvenue dans ce minuteur du temps de cuisson !")
print ("Que souhaitez-vous cuire ?")
print ("a - des oeufs à la coque (3 minutes)")
print ("b - des oeufs mollets (6 minutes)")
print ("c - des oeufs durs (10 minutes)")

choix = input ("votre choix ? (entre a, b et c) : ")

def affichage_du_temps_de_cuisson (minutes,secondes,nom_de_loeuf):
    print (f"vous avez selectionner un {nom_de_loeuf} ! Durée estimée : {minutes} minutes")
    print ("cuisson en cours \n", end="")
    for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)

    while True:
        if secondes == 0:
            minutes = minutes-1
            secondes = secondes+60

        if secondes> 0:
            secondes = secondes - 10
        print(f"Durée restante = {minutes:02d}:{secondes:02d}\n", end="")

        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
        
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