print ("Bienvenue dans ce questionnaire :), répondez au question avec la lettre correspondant aux propositions")

def afficher_question (question,choix,reponse_correcte):
    print (question)

    print (f"{choix[0]}\n{choix[1]}\n{choix[2]}\n{choix[3]}\n")

    reponse = input ("Votre réponse : ")

    if reponse == reponse_correcte : 
        print ("Bien joué ! réponse correcte")
    else:
        print ("réponse incorrecte")

afficher_question ("Quelle est la capitale de Paris ?",["a - Paris", "b - Nairobi", "c - Copenhague", "d - Madrid"], "a")