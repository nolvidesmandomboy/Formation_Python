import time

print ("Bienvenue dans ce minuteur du temps de cuisson !")
print ("Que souhaitez-vous cuire ?")
print ("a - des oeufs à la coque (3 minutes)")
print ("b - des oeufs mollets (6 minutes)")
print ("c - des oeufs durs (10 minutes)")

choix = input ("votre choix ? (entre a, b et c) : ")

for i in range (5) : 
    time.sleep(1)
    print (".", end="", flush=True)

print("")
print("fin du programme")

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

print(f"{min:02d}")