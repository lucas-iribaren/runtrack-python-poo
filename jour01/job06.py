class Animal:
    def __init__(self):
        self.age = 0

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

mon_animal = Animal()

# Afficher l'âge initial
print("Âge initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()
print("# Age de l'animal après appel de la méthode vieillir")

# Afficher le nouvel âge
print("Nouvel âge de l'animal :", mon_animal.age)

# Nommer l'animal
mon_animal.nommer("Bouboule")
print("L'animal se nomme", mon_animal.prenom)