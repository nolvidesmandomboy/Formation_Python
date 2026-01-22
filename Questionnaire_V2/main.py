print ("Bienvenue dans ce questionnaire :), répondez au question avec la lettre correspondant aux propositions\n")

def afficher_question (question):
    global score #permet d'integrer la variable du programme principale dans la fonction sans la rentrer en parametre 

    titre_question =question[0]
    choix_reponses=question[1]
    reponse_correcte=question[3]

    print (titre_question)

    reponse_utilisateur = input ("Votre réponse : ")

    if reponse_utilisateur == reponse_correcte : 
        score = score + 1
        print ("Bien joué ! réponse correcte\n")
    else:
        print ("réponse incorrecte\n")

score = 0

question1 = (
    "Quelle est la capitale de Paris ?",
    ("a - Paris", "b - Nairobi", "c - Copenhague", "d - Madrid"),
    "Paris"
)

question2 = (
    "Comment s'appelle le président actuel de la France ?",
    ("a - Paul Biya", "b - Theodoro Obiang Nguema Mbasogo", "c - Macron", "d - Trump"),
    "Macron"
)

question3 = (
    "Quel manga connu dans le monde entier a été créé par Masashi Kishimoto ?",
    ("a - Berserk", "b - Naruto", "c - My Hero Academia", "d - DBZ"),
    "Naruto"
)

question4 = (
    "Quelle planète est la plus proche du Soleil ?",
    ("a - Mercure", "b - Vénus", "c - Mars", "d - Jupiter"),
    "Mercure"
)

question5 = (
    "Qui a peint la Joconde ?",
    ("a - Vincent Van Gogh", "b - Pablo Picasso", "c - Léonard de Vinci", "d - Claude Monet"),
    "Léonard de Vinci"
)

question6 = (
    "Quel langage est principalement utilisé pour le développement web côté serveur ?",
    ("a - HTML", "b - CSS", "c - Python", "d - JavaScript"),
    "Python"
)


afficher_question (question1)

print (f"votre score est de {score}")