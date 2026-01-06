print ("Bienvenue dans ce questionnaire :), répondez au question avec la lettre correspondant aux propositions\n")

def afficher_question (question,choix,reponse_correcte):
    print (question)

    print (f"{choix[0]}\n{choix[1]}\n{choix[2]}\n{choix[3]}\n")

    reponse = input ("Votre réponse : ")

    if reponse == reponse_correcte : 
        print ("Bien joué ! réponse correcte")
    else:
        print ("réponse incorrecte\n")

afficher_question ("Quelle est la capitale de Paris ?",["a - Paris", "b - Nairobi", "c - Copenhague", "d - Madrid"], "a")

afficher_question ("Comment s'appelle le président actuelle de la France",["a - Paul Biya", "b - Theodoro Obiang Nguema Mbasogo", "c - Macron", "d - Trump"], "c")

afficher_question ("Quel manga connu dans le monde entier a été crée par Masashi Kishimoto ?",["a - Berserk", "b - Naruto", "c - My Hero Academia", "d - DBZ"], "b")

afficher_question("Quelle planète est la plus proche du Soleil ?", ["a - Mercure", "b - Vénus", "c - Mars", "d - Jupiter"], "a")

afficher_question("Qui a peint la Joconde ?", ["a - Vincent Van Gogh", "b - Pablo Picasso", "c - Léonard de Vinci", "d - Claude Monet"], "c")

afficher_question("Quel langage est principalement utilisé pour le développement web côté serveur ?", ["a - HTML", "b - CSS", "c - Python", "d - JavaScript"], "c")