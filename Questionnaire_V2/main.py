print ("Bienvenue dans ce questionnaire :), répondez au question avec la lettre correspondant aux propositions\n")

def afficher_question (question):
    global score #permet d'integrer la variable du programme principale dans la fonction sans la rentrer en parametre 

    titre_question = question[0]
    choix_reponses = question[1]
    reponse_correcte = question[2]

    print (titre_question)
    #print (f"{choix_reponses[0]}\n{choix_reponses[1]}\n{choix_reponses[2]}\n{choix_reponses[3]}")

    for choix  in range(0, len(choix_reponses)) :
        print (f"{choix + 1}) {choix_reponses [choix]}")

    reponse_utilisateur_str = input (f"Votre réponse (entre 1 et {len(choix_reponses)}): ")
    reponse_utilisateur_int = int(reponse_utilisateur_str)

    if choix_reponses[reponse_utilisateur_int-1].lower() == reponse_correcte.lower() #or reponse_utilisateur_str.lower() == reponse_correcte.lower(): 
        score = score + 1
        print ("Bien joué ! réponse correcte\n")
    else:
        print ("réponse incorrecte\n")

score = 0

question1 = (
    "Quelle est la capitale de Paris ?",
    ("Paris", "Nairobi", "Copenhague", "Madrid"),
    "Paris"
)

question2 = (
    "Comment s'appelle le président actuel de la France ?",
    ("Paul Biya", "Theodoro Obiang Nguema Mbasogo", "Macron", "Trump"),
    "Macron"
)

question3 = (
    "Quel manga connu dans le monde entier a été créé par Masashi Kishimoto ?",
    ("Berserk", "Naruto", "My Hero Academia", "DBZ"),
    "Naruto"
)

question4 = (
    "Quelle planète est la plus proche du Soleil ?",
    ("Mercure", "Vénus", "Mars", "Jupiter"),
    "Mercure"
)

question5 = (
    "Qui a peint la Joconde ?",
    ("Vincent Van Gogh", "Pablo Picasso", "Léonard de Vinci", "Claude Monet"),
    "Léonard de Vinci"
)

question6 = (
    "Quel langage est principalement utilisé pour le développement web côté serveur ?",
    ("HTML", "CSS", "Python", "JavaScript"),
    "Python"
)


afficher_question (question1)

print (f"votre score est de {score}")