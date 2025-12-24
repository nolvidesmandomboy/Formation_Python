import time

for i in range (5) : 
    time.sleep(1)
    print (".", end="", flush=True)

print("")
print("fin du programme")

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60