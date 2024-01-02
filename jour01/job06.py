class Animal:
    def __init__(self, prenom):
        self.age = 0
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

mon_animal = Animal(prenom="Nom_de_l'animal")

# Afficher l'âge initial
print("Âge initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()
print("# Age de l'animal apres appel de la méthode vieillir")

# Afficher le nouvel âge
print("Nouvel âge de l'animal :", mon_animal.age)