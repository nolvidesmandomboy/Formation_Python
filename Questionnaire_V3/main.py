# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

class Question:
    def __init__(self, titre_question=str,choix_reponses=(),bonne_reponse=str):
        self.__titre_question__ = titre_question
        self.choixreponses = choix_reponses
        self.__bonne_reponse__ = bonne_reponse
    
    def poser_question(self):
        print("QUESTION")
        print("  " + self.__titre_question__)
        for i in range(len(self.choixreponses)):
            print("  ", i+1, "-", self.choixreponses[i])

        print()
        resultat_response_correcte = False
        #reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
        numero = []
        for i in range (0,len(self.choixreponses)):
            numero.append(i+1)
        reponse = input(f"Votre réponse entre {min(numero)} et {max(numero)} : ")
        reponse_int = int(reponse)
        if self.choixreponses[reponse_int-1].lower() == self.__bonne_reponse__.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte
        

'''def demander_reponse_numerique_utlisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max)'''
    

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''



'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

#lancer_questionnaire(questionnaire)
 
q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q1.poser_question()