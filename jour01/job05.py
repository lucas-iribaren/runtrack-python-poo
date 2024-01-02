class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Exemple d'utilisation de la classe Point
point1 = Point(2, 3)

point1.afficherLesPoints()  # Affiche : Coordonnées du point : (2, 3)
point1.afficherX()          # Affiche : Coordonnée x : 2
point1.afficherY()          # Affiche : Coordonnée y : 3

point1.changerX(5)
point1.changerY(8)

point1.afficherLesPoints()  # Affiche : Coordonnées du point : (5, 8)