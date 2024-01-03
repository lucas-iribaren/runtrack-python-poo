class Student: 
    def __init__(self, prenom, nom, numero_etudiant, nb_credit): 
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = numero_etudiant 
        self.__nb_credit = nb_credit
        self.__level = self.__studentEval()

    def get_nom (self):
        return self.__nom
    
    def get_prenom (self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__num_etudiant
    
    def get_nb_credit(self):
        return self.__nb_credit

    def get_level(self):
        return self.__level

    def set_nom(self, nom): 
        self.__nom = nom

    def set_prenom(self, prenom): 
        self.__prenom = prenom

    def set_numero_etudiant(self, numero_etudiant): 
        self.__num_etudiant = numero_etudiant

    def set_nb_credit(self, nb_credit):
        self.__nb_credit = nb_credit

    def set_level(self, level):
        self.__level = level

    def add_credits(self, ajout_credit):
        if ajout_credit > 0:
            self.__nb_credit = self.__nb_credit + ajout_credit  

    def __studentEval(self):
        if self.__nb_credit >= 90:
            return "Excellent"
        elif self.__nb_credit >= 80:
            return "Très bien"
        elif self.__nb_credit >= 70:
            return "Bien"
        elif self.__nb_credit >= 60:
            return  "Passable"
        elif self.__nb_credit < 60:
            return "Insuffisant"

    def studentInfo(self):
        print(f"\n Nom: {self.get_nom()}\n Prénom = {self.get_prenom()} \n id = {self.get_numero_etudiant()} \n Niveau = {self.get_level()}\n")


info_student = Student ("John", "Doe", 145, 76)
info_student.add_credits(10)
info_student.add_credits(10)
info_student.add_credits(10)
info_student.studentInfo()

print (f"Le nombre de crédits de {info_student.get_prenom()} {info_student.get_nom()} est de {info_student.get_nb_credit()} points \n")
