import time

print ("Bienvenue dans ce minuteur du temps de cuisson !")
print ("Que souhaitez-vous cuire ?")
print ("a - des oeufs à la coque (3 minutes)")
print ("b - des oeufs mollets (6 minutes)")
print ("c - des oeufs durs (10 minutes)")

choix = input ("votre choix ? (entre a, b et c) : ")

# mettre les min et le afficher temps qu'il reste

def cuisson (minutes,secondes,nom_de_loeuf):
    print ("cuisson en cours")
    while True:
        if secondes == 0:
            minutes = minutes-1
            secondes = secondes+60

        if secondes> 0:
            secondes = secondes - 10
        print(f" Durée restante = {minutes:02d}:{secondes:02d}")

        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
        

        if minutes == 0 and secondes == 0:
            break
    
    print(f"fin de la cuisson !, votre {nom_de_loeuf} est prêt !")

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

    


if choix == "a" :
    d=180
    min =d//60
    sec = sec = d-min*60
    cuisson(min, sec, "des oeufs à la coque")
