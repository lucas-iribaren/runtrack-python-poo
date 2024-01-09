class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.__en_marche
    def get_reservoir(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
    def set_reservoir(self, niveau):
        self.__reservoir = niveau

    def demarrer(self):
        niveau_reservoir = self.__verifier_plein()
        if niveau_reservoir > 5:
            self.__en_marche = True
            print("La voiture a été démarrée.")
        else:
            print("Impossible de démarrer. Le réservoir est trop bas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")

    def __verifier_plein(self):
        return self.__reservoir
    

ma_voiture = Voiture(marque="Renault", modele="Clio IV", annee=2018, kilometrage=13000)

print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()}")
print(f"En marche: {ma_voiture.get_en_marche()}")

ma_voiture.demarrer()
ma_voiture.arreter()

ma_voiture.set_reservoir(3)
ma_voiture.demarrer()
