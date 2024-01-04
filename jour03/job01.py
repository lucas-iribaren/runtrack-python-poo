class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom
    def get_nb_habitants(self):
        return self.__nb_habitants
    
    def set_nom(self, nom):
        self.__nom = nom
    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants


class Personne:
    def __init__(self, nom, age, obj_class_ville):
        self.__nom = nom
        self.__age = age
        self.__obj_class_ville = obj_class_ville

    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_obj_class_ville(self):
        return self.__obj_class_ville
    
    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_obj_class_ville(self, obj_class_ville):
        self.__obj_class_ville = obj_class_ville
    
    def ajouterPopulation(self):
        populations = self.__obj_class_ville.get_nb_habitants()
        self.__obj_class_ville.set_nb_habitants(populations +1) 

Paris = Ville("Paris", 1000000)
print(f"Population de {Paris.get_nom()}: {Paris.get_nb_habitants()}")
Marseille = Ville("Marseille", 861635)
print(f"Population de {Marseille.get_nom()}: {Marseille.get_nb_habitants()}")

John = Personne("John",45,Paris)
Myrtille = Personne("Myrtille", 4,Paris)
Chloé = Personne("Chloé",18, Marseille)

John.ajouterPopulation()
Myrtille.ajouterPopulation()
Chloé.ajouterPopulation()

print(f"Mis à jour des habitants de {Paris.get_nom()}: {Paris.get_nb_habitants()}")
print(f"Mis à jour des habitants de {Marseille.get_nom()}: {Marseille.get_nb_habitants()}")
