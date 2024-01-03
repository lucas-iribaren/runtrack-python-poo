class Rectangle:
    def __init__(self,longueur, largeur):
        self.__rectangle_longueur = longueur
        self.__rectangle_largeur = largeur
        
    def get_largeur(self):
        return self.__rectangle_largeur
    
    def get_longueur(self):
        return self.__rectangle_longueur
    
    def set_largeur(self, largeur):
        self.__rectangle_largeur = largeur

    def set_longueur(self, longueur):
        self.__rectangle_longueur = longueur

mon_rectangle = Rectangle(10, 5)

print(mon_rectangle.get_longueur(), mon_rectangle.get_largeur())

mon_rectangle.set_longueur(11)
mon_rectangle.set_largeur(6)

print(mon_rectangle.get_longueur(), mon_rectangle.get_largeur())
