class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.nb_credit = 0
        
    def add_credits(self, nb_credit):
        if nb_credit > 0:
            self.nb_credit += nb_credit
            
    def afficher_nb_credit(self):
        print(f"Le nombre de crédits pour {self.nom} {self.prenom} est de {self.nb_credit} points.")
            

# Instanciation de l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

# Affichage du nombre de crédits total de John Doe
john_doe.afficher_nb_credit()
class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien."
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom: ", self.__nom)
        print("Prénom: ", self.__prenom)
        print("Identifiant: ", self.__num_etudiant)
        print("Niveau: ", self.__level)

john_doe = Student("Doe", "John", 145)
john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)
john_doe.studentInfo()