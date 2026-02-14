# LES FONCTIONS : PROJET QUESTIONNAIRE V3

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
        numero = []
        for i in range (0,len(self.choixreponses)):
            numero.append(i+1)
        #reponse = input(f"Votre réponse entre {min(numero)} et {max(numero)} : ")
        #reponse_int = int(reponse)
        reponse_int = self.demander_reponse_numerique_utlisateur(min(numero), max(numero))
        if self.choixreponses[reponse_int-1].lower() == self.__bonne_reponse__.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte
        

    def demander_reponse_numerique_utlisateur(self,min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return self.demander_reponse_numerique_utlisateur(min, max)

class Questionnaire:
    def __init__(self, questions=[]):
        self.question = questions
    
    def lancer_questionnaire(self):
        score = 0
        for question in self.question:
            if question.poser_question():
                score += 1
        print("Score final :", score, "sur", len(self.question))
 
q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q2 = Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
q2 = Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
liste_de_questions = [q1,q2]
questionnaire1 = Questionnaire (liste_de_questions)
questionnaire1.lancer_questionnaire()