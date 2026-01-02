print ("Bienvenue dans ce questionnaire :), répondez au question avec la lettre correspondant aux propositions")

print ("Quelle est la capitale de la France ? ")

print ("a - Nairobi \nb - Paris \nc- New York \nd - Malabo")

reponse = input ("Votre réponse : ")

if reponse == "a" : 
    print ("Bien joué ! réponse correcte")
elif reponse in ["b","c","d"]:
    print ("réponse incorrecte")
else :
    print ("écrivez une réponse qui se trouve parmi les choix proposés svp")