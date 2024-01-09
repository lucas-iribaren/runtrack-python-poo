class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False

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

    def demarrer(self):
        self.__en_marche = True
        print("La voiture a été démarrée.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")

# Exemple d'utilisation
ma_voiture = Voiture(marque="Renault", modele="Clio IV", annee=2018, kilometrage=13000)

print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()}")
print(f"En marche: {ma_voiture.get_en_marche()}")

ma_voiture.demarrer()
ma_voiture.arreter()
